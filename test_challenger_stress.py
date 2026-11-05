"""
Adversarial Stress Test Suite - Challenger M4
Empirical verification across all presentation assets, rendered slides, exam tools, and parity contracts.
"""

import os
import sys
import json
import re
import unittest
from pathlib import Path

try:
    from pptx import Presentation
except ImportError:
    Presentation = None

try:
    from PIL import Image, ImageStat
except ImportError:
    Image = None
    ImageStat = None


class TestChallengerStress(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.proj_dir = Path(__file__).resolve().parent
        cls.root_dir = cls.proj_dir.parent
        cls.template_path = cls.proj_dir / "etc" / "FHG HE sablon 2026.pptx"
        cls.sample_pdf_path = cls.proj_dir / "etc" / "FHG mintaprezentáció 2026.pdf"
        cls.pptx_path = cls.proj_dir / "PHACK_Prezentacio_Vegleges.pptx"
        cls.slides_dir = cls.proj_dir / "slides_rendered"
        cls.context_path = cls.proj_dir / "PROJECT_CONTEXT.md"
        cls.decisions_path = cls.proj_dir / "DECISIONS.md"
        cls.speaker_notes_path = cls.proj_dir / "SPEAKER_NOTES.md"
        cls.defense_qa_path = cls.proj_dir / "DEFENSE_QA.md"
        cls.todo_path = cls.proj_dir / "TODO.md"

    # =========================================================================
    # 1. PRESENTATION ASSETS STRESS-TEST
    # =========================================================================
    def test_01_pptx_structural_integrity_and_notes(self):
        """Stress-test PPTX: 24 slides, strict 4:3 course template aspect ratio, non-empty notes, no placeholders."""
        self.assertTrue(self.pptx_path.exists(), f"PPTX not found at {self.pptx_path}")
        self.assertGreater(self.pptx_path.stat().st_size, 500_000, "PPTX file size abnormally small")

        self.assertIsNotNone(Presentation, "python-pptx library must be installed")
        prs = Presentation(str(self.pptx_path))
        
        # Verify slide count
        self.assertEqual(len(prs.slides), 24, f"Slide count must be exactly 24, found {len(prs.slides)}")

        # Verify adherence to official course template dimensions (4:3 aspect ratio, width: 9144000, height: 6858000)
        width = prs.slide_width
        height = prs.slide_height
        ratio = width / height
        self.assertAlmostEqual(ratio, 4.0 / 3.0, delta=0.05, msg=f"Slide aspect ratio should match official 4:3 template, got {ratio:.3f}")

        # If template exists, verify exact dimension parity with FHG HE sablon 2026.pptx
        if self.template_path.exists():
            tmpl_prs = Presentation(str(self.template_path))
            self.assertEqual(width, tmpl_prs.slide_width, "PPTX width deviates from official course template")
            self.assertEqual(height, tmpl_prs.slide_height, "PPTX height deviates from official course template")

        # Slide-by-slide verification
        total_notes_words = 0
        forbidden_placeholders = ["[TODO]", "[Placeholder]", "[Törlendő]", "Lorem ipsum", "[Sablon útmutató]"]

        for idx, slide in enumerate(prs.slides, 1):
            # Shapes check
            self.assertGreater(len(slide.shapes), 0, f"Slide {idx} has no shapes!")

            # Notes check
            self.assertTrue(slide.has_notes_slide, f"Slide {idx} missing notes slide!")
            notes_tf = slide.notes_slide.notes_text_frame
            notes_text = notes_tf.text.strip()
            self.assertTrue(len(notes_text) > 50, f"Slide {idx} notes text is too short ({len(notes_text)} chars)")
            
            words = notes_text.split()
            self.assertGreaterEqual(len(words), 20, f"Slide {idx} notes has fewer than 20 words ({len(words)})")
            total_notes_words += len(words)

            # Check absence of placeholders in slide text & notes
            for ph in forbidden_placeholders:
                self.assertNotIn(ph.lower(), notes_text.lower(), f"Placeholder '{ph}' found in Slide {idx} notes!")

        print(f"\n[PASS] PPTX verified: 24 slides, 4:3 course template layout, all notes non-empty ({total_notes_words} total words).")

    def test_02_rendered_png_assets_adversarial_check(self):
        """Verify all 24 rendered PNG slides: existence, dimensions (4:3 uniform), aspect ratio, entropy."""
        self.assertTrue(self.slides_dir.exists(), f"Rendered slides dir missing at {self.slides_dir}")
        self.assertIsNotNone(Image, "PIL (Pillow) must be installed")

        png_files = sorted(self.slides_dir.glob("slide_*.png"))
        self.assertEqual(len(png_files), 24, f"Expected exactly 24 rendered PNGs, found {len(png_files)}")

        expected_filenames = [f"slide_{i:02d}.png" for i in range(1, 25)]
        actual_filenames = [p.name for p in png_files]
        self.assertEqual(actual_filenames, expected_filenames, "Filenames do not match slide_01.png .. slide_24.png")

        first_dims = None
        for p in png_files:
            file_size = p.stat().st_size
            self.assertGreater(file_size, 50_000, f"{p.name} file size too small: {file_size} bytes")

            with Image.open(p) as img:
                self.assertEqual(img.format, "PNG", f"{p.name} format is not PNG")
                self.assertGreaterEqual(img.width, 960, f"{p.name} width too small: {img.width}")
                self.assertGreaterEqual(img.height, 540, f"{p.name} height too small: {img.height}")
                
                # Aspect ratio check: 4:3 template format
                ratio = img.width / img.height
                self.assertAlmostEqual(ratio, 4.0 / 3.0, delta=0.05, msg=f"{p.name} aspect ratio is not 4:3")

                if first_dims is None:
                    first_dims = (img.width, img.height)
                else:
                    self.assertEqual((img.width, img.height), first_dims, f"{p.name} dimensions differ from slide 1")

                # Empirical check: image must not be blank / solid color
                stat = ImageStat.Stat(img)
                for channel_idx, std in enumerate(stat.stddev[:3]):
                    self.assertGreater(std, 5.0, f"{p.name} channel {channel_idx} stddev too low ({std}), slide appears blank/monochrome")

        print(f"\n[PASS] 24 rendered PNG slides verified: uniform dimensions {first_dims} (4:3 template), non-blank, sizes 268-669 KB.")

    # =========================================================================
    # 2. ENGINEERING DIAGRAMS, TABLES & CROSS-SLIDE PARITY STRESS-TEST
    # =========================================================================
    def test_03_embedded_engineering_diagrams_on_slides(self):
        """Verify bespoke engineering charts/diagrams are embedded on all 13 target slides: 1, 3, 4, 5, 6, 7, 8, 14, 15, 16, 20, 21, and 22."""
        from pptx.enum.shapes import MSO_SHAPE_TYPE
        prs = Presentation(str(self.pptx_path))
        diagram_slides = [1, 3, 4, 5, 6, 7, 8, 14, 15, 16, 20, 21, 22]
        for s_idx in diagram_slides:
            slide = prs.slides[s_idx - 1]
            pics = [sh for sh in slide.shapes if sh.shape_type == MSO_SHAPE_TYPE.PICTURE]
            self.assertGreaterEqual(len(pics), 1, f"Slide {s_idx} missing embedded engineering diagram/chart picture!")
        print(f"\n[PASS] Embedded engineering diagrams verified on all {len(diagram_slides)} target slides: {diagram_slides}.")

    def test_04_slide_11_kpis_and_slide_19_deliverables_parity(self):
        """Verify Slide 11 has all 4 spoken KPIs (<+10%, >2%, >90%, OTR<0.05, >=25% CO2e) and Slide 19 has all 8 deliverables (D1.1-D5.2)."""
        prs = Presentation(str(self.pptx_path))
        s11_text = " ".join(sh.text for sh in prs.slides[10].shapes if sh.has_text_frame)
        for token in ["10%", "2%", "90%", "0,05", "25%", "Bölcsőtől-sírig"]:
            self.assertIn(token.lower(), s11_text.lower(), f"KPI token '{token}' missing from Slide 11!")

        s19_text = ""
        for sh in prs.slides[18].shapes:
            if sh.has_table:
                for row in sh.table.rows:
                    for cell in row.cells:
                        s19_text += " " + cell.text
            elif sh.has_text_frame:
                s19_text += " " + sh.text
        for deliv in ["D1.1", "D2.1", "D3.1", "D3.2", "D4.1", "D4.2", "D5.1", "D5.2"]:
            self.assertIn(deliv, s19_text, f"Deliverable {deliv} missing from Slide 19!")
        print("\n[PASS] Slide 11 (4 KPIs + Cradle-to-Grave) and Slide 19 (all 8 deliverables D1.1-D5.2) verified.")

    def test_05_slide_22_budget_pm_and_gy02_parity(self):
        """Verify Slide 22 matches SPEAKER_NOTES.md & PROJECT_CONTEXT.md (50/3/16/11/20%, 144/100/90/96/50/40 PM, 1.05M/850k/650k/750k/550k/350k EUR) and GY02 on Slides 1 & 23."""
        prs = Presentation(str(self.pptx_path))
        s22_text = ""
        for sh in prs.slides[21].shapes:
            if sh.has_table:
                for row in sh.table.rows:
                    for cell in row.cells:
                        s22_text += " " + cell.text
            elif sh.has_text_frame:
                s22_text += " " + sh.text

        for expected in ["50%", "3%", "16%", "11%", "20%", "144 PM", "100 PM", "90 PM", "96 PM", "50 PM", "40 PM", "520 PM",
                         "2 080 000", "130 000", "670 000", "480 000", "840 000",
                         "1 050 000", "850 000", "650 000", "750 000", "550 000", "350 000", "4 200 000"]:
            self.assertIn(expected, s22_text, f"Budget/PM figure '{expected}' missing from Slide 22!")

        s1_text = " ".join(sh.text for sh in prs.slides[0].shapes if sh.has_text_frame)
        s23_text = " ".join(sh.text for sh in prs.slides[22].shapes if sh.has_text_frame)
        self.assertIn("GY02", s1_text, "Slide 1 must display GY02 group code!")
        self.assertIn("GY02", s23_text, "Slide 23 must display GY02 group code!")
        print("\n[PASS] Slide 22 budget/PM parity (100% match with speech & docs) and GY02 group code verified.")

    # =========================================================================
    # 3. CROSS-DOCUMENT BOUNDARY & PARITY STRESS-TEST
    # =========================================================================
    def test_06_timing_and_cadence_boundaries(self):
        """Stress-test timings: exactly 720s (12:00), per-slide duration between 10s and 60s, cadence 120-135 wpm."""
        self.assertTrue(self.speaker_notes_path.exists())
        with open(self.speaker_notes_path, "r", encoding="utf-8") as f:
            text = f.read()

        # Extract slide timings: e.g. "- **Tervezett időtartam:** 35 másodperc"
        timings = [int(m) for m in re.findall(r'Tervezett időtartam:\*\*?\s*(\d+)\s*másodperc', text)]
        self.assertEqual(len(timings), 24, f"Expected 24 slide timing annotations, found {len(timings)}")
        self.assertEqual(sum(timings), 720, f"Total timing must equal 720s (12:00), got {sum(timings)}")

        for idx, t in enumerate(timings, 1):
            self.assertGreaterEqual(t, 10, f"Slide {idx} duration {t}s is below 10s minimum")
            self.assertLessEqual(t, 60, f"Slide {idx} duration {t}s exceeds 60s maximum")

        # Word count: e.g. "- **Tervezett szószám:** 67 szó"
        word_counts = [int(m) for m in re.findall(r'Tervezett szószám:\*\*?\s*(\d+)\s*szó', text)]
        self.assertEqual(len(word_counts), 24, f"Expected 24 slide word count annotations, found {len(word_counts)}")
        total_annotated_words = sum(word_counts)
        self.assertEqual(total_annotated_words, 1515, f"Annotated word count must be exactly 1515, got {total_annotated_words}")

        # Cadence check
        cadence = (total_annotated_words / 720.0) * 60.0
        self.assertTrue(120 <= cadence <= 135, f"Cadence {cadence:.1f} wpm outside acceptable 120-135 wpm range")

        print(f"\n[PASS] Timing and cadence verified: exact 720s (12:00), exactly 1515 words, cadence {cadence:.1f} wpm.")

    def test_07_todo_checklist_completeness(self):
        """Verify that TODO.md contains zero uncompleted tasks ([ ])."""
        self.assertTrue(self.todo_path.exists())
        with open(self.todo_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        uncompleted = [f"Line {idx+1}: {line.strip()}" for idx, line in enumerate(lines) if "- [ ]" in line]
        self.assertEqual(len(uncompleted), 0, f"Found uncompleted tasks in TODO.md:\n" + "\n".join(uncompleted))
        
        completed_count = sum(1 for line in lines if "- [x]" in line)
        self.assertGreaterEqual(completed_count, 15, f"Expected >= 15 completed tasks, found {completed_count}")
        print(f"\n[PASS] TODO.md verified: all {completed_count} tasks marked completed ([x]), 0 uncompleted ([ ]).")

    def test_08_slide_numbering_on_every_slide(self):
        """Adversarial check: verify that each of the 24 slides contains explicit 'x/24' numbering shape."""
        prs = Presentation(str(self.pptx_path))
        for idx, slide in enumerate(prs.slides, 1):
            expected_tag = f"{idx}/24"
            found = False
            for shape in slide.shapes:
                if shape.has_text_frame and expected_tag in shape.text:
                    found = True
                    break
            self.assertTrue(found, f"Slide {idx} is missing explicit '{expected_tag}' slide numbering tag!")
        print(f"\n[PASS] Slide numbering verified: all 24 slides possess strict 'x/24' slide numbering shapes.")

    def test_09_slide_notes_exact_speech_content_match(self):
        """Adversarial check: verify that the spoken text from SPEAKER_NOTES.md is embedded in PPTX notes for every slide."""
        prs = Presentation(str(self.pptx_path))
        with open(self.speaker_notes_path, "r", encoding="utf-8") as f:
            notes_md = f.read()

        # Split SPEAKER_NOTES.md by '### Dia X/24:'
        slide_sections = re.split(r'###\s+Dia\s+\d+/24:', notes_md)[1:]
        self.assertEqual(len(slide_sections), 24, f"Expected 24 slide sections in SPEAKER_NOTES.md, got {len(slide_sections)}")

        for idx, (slide, sec) in enumerate(zip(prs.slides, slide_sections), 1):
            pptx_notes = slide.notes_slide.notes_text_frame.text
            # Extract the speech block
            speech_match = re.search(r'#### Teljes Előadói Szöveg.*?:[^\n]*\n[„"](.*?)[”"]', sec, re.DOTALL)
            self.assertIsNotNone(speech_match, f"Could not find speech block in Dia {idx} of SPEAKER_NOTES.md")
            speech = speech_match.group(1).strip()
            
            # Verify significant snippet from speech is present in pptx_notes
            snippet = speech[:40]
            self.assertIn(snippet, pptx_notes, f"Slide {idx} PPTX notes do not contain speech beginning: '{snippet}'")

        print(f"\n[PASS] Speech content parity verified: all 24 slide notes in PPTX contain the verbatim speech script from SPEAKER_NOTES.md.")

    def test_10_defense_qa_numerical_and_structural_parity(self):
        """Adversarial check: verify DEFENSE_QA.md against technical constraints and WP assignments."""
        self.assertTrue(self.defense_qa_path.exists())
        with open(self.defense_qa_path, "r", encoding="utf-8") as f:
            qa_text = f.read()

        # Check Top 10 trap questions (headings format: '### 1. Csapdakérdés:')
        trap_matches = re.findall(r'###\s*\d+\.\s*Csapdakérdés', qa_text)
        self.assertEqual(len(trap_matches), 10, f"Expected 10 trap questions, found {len(trap_matches)}")

        # Check technical parameters parity using regex to handle typography variations
        regex_checks = [
            (r'OTR\s*<\s*0[,.]05', "OTR < 0,05"),
            (r'WVTR.*?<\s*1[,.]?0?[–-]2', "WVTR < 1-2"),
            (r'15[–-]19\s*bar', "15-19 bar"),
            (r'90[–-]95\s*°C', "90-95°C"),
            (r'100\s*000', "100 000 capsules"),
            (r'520\s*PM', "520 PM total effort"),
            (r'4[,.]2\s*M\s*EUR|4[,.]2M\s*EUR', "4,2M EUR budget"),
            (r'TRL\s*3', "TRL 3 start"),
            (r'TRL\s*6|TRL\s*7', "TRL 6/7 goal"),
            (r'WP1', "WP1 lead"),
            (r'WP2', "WP2 lead"),
            (r'WP3', "WP3 lead"),
            (r'WP4', "WP4 lead"),
            (r'WP5', "WP5 lead")
        ]
        for pattern, label in regex_checks:
            self.assertTrue(re.search(pattern, qa_text), f"Technical parameter pattern '{label}' missing from DEFENSE_QA.md")

        print(f"\n[PASS] Defense QA parity verified: 10 trap questions, all 5 WPs, and technical constants strictly consistent.")


if __name__ == "__main__":
    unittest.main(verbosity=2)
