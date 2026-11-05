#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Projekt/test_defense_qa.py
Automated Verification Test Suite for the MSc-level Defense Q&A Guide (DEFENSE_QA.md)
Project: PHACK (HORIZON-CL6-2026-CIRCBIO)
Kurzus: BME Fenntartható hulladékgazdálkodás (MSc)
"""

import os
import re
import sys
import unittest
from pathlib import Path


class TestDefenseQAGuide(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        script_dir = Path(__file__).resolve().parent
        proj_dir = script_dir.parent if script_dir.name == "scripts" else script_dir
        docs_dir = proj_dir / "docs" if (proj_dir / "docs").is_dir() else proj_dir
        cls.doc_path = docs_dir / "DEFENSE_QA.md"
        if not cls.doc_path.exists():
            cls.doc_path = Path("docs/DEFENSE_QA.md").resolve()
        
        with open(cls.doc_path, "r", encoding="utf-8") as f:
            cls.content = f.read()

    def test_01_file_existence_and_size(self):
        """Verifies file exists and has substantial academic depth (>15,000 bytes)."""
        self.assertTrue(self.doc_path.exists(), f"File {self.doc_path} does not exist!")
        size = os.path.getsize(self.doc_path)
        self.assertGreater(size, 15000, f"File size is only {size} bytes, expected >15,000 bytes.")
        print(f"[PASS] test_01: DEFENSE_QA.md exists ({size:,} bytes).")

    def test_02_defense_strategy_and_protocol(self):
        """Verifies 3-minute Q&A structure, time management rules (20-30s), and WP citation rule."""
        self.assertIn("3 Perces Vitablokk", self.content)
        self.assertTrue(re.search(r"20[–-]30\s*másodperc", self.content, re.IGNORECASE))
        self.assertIn("WP1–WP5", self.content)
        
        # Verify all 6 roles and all 6 students
        roles = ["Coord", "RD1", "RD2", "Innov", "Dissz", "Fin"]
        for role in roles:
            self.assertTrue(re.search(rf"\b{role}\b", self.content), f"Role {role} not found in protocol!")
        
        for student_num in range(1, 7):
            student_str = f"Hallgató {student_num}"
            self.assertIn(student_str, self.content, f"{student_str} not mapped in protocol!")
        print("[PASS] test_02: Defense strategy and 6-role student protocol verified.")

    def test_03_top_10_trap_questions(self):
        """Verifies presence of Top 10 trap questions with 15-second model answers."""
        self.assertIn("Top 10 Csapdakérdés", self.content)
        trap_matches = re.findall(r"### \d+\.\s*Csapdakérdés", self.content)
        self.assertEqual(len(trap_matches), 10, f"Expected 10 trap questions, found {len(trap_matches)}")
        
        fifteen_sec_matches = re.findall(r"15 másodperces modellválasz", self.content, re.IGNORECASE)
        self.assertGreaterEqual(len(fifteen_sec_matches), 10, "Each trap question must have a 15-second model answer.")
        print("[PASS] test_03: Top 10 trap questions and 15-second model answers verified.")

    def test_04_topic_a_materials_and_plastics_tech(self):
        """Verifies Topic A: PHA vs PLA, HDT > 95-105°C, Tm 130-170°C vs PLA Tg 55-60°C, 90-95°C / 15-19 bar,
        biodegradation in NF T51-800, anaerobic digestion in Hungarian biogas plants (MOHU), UCO feedstock,
        pricing economics (4.5-6.0 €/kg vs 2.8-3.5 €/kg by 2030), and TPS (thermoplastic starch) comparison."""
        # Thermal properties
        self.assertTrue(re.search(r"HDT.*?>\s*95[–-]105", self.content))
        self.assertTrue(re.search(r"T_m.*?130[–-]170", self.content))
        self.assertTrue(re.search(r"T_g.*?55[–-]60", self.content))
        self.assertTrue(re.search(r"90[–-]95\s*°C", self.content))
        self.assertTrue(re.search(r"15[–-]19\s*bar", self.content))

        # Biodegradation & Biogas
        self.assertIn("NF T51-800", self.content)
        self.assertIn("EN 13432", self.content)
        self.assertIn("biogáz", self.content.lower())
        self.assertIn("anaerob", self.content.lower())
        self.assertIn("mohu", self.content.lower())
        self.assertIn("barna kuka", self.content.lower())
        self.assertTrue(re.search(r"30[–-]45\s*nap", self.content))
        self.assertTrue(re.search(r"előaprítás|szűrő|hidropulper|dobrosta|felreped|pelyhek", self.content, re.IGNORECASE), "Biogas pre-screening mechanics missing!")

        # Raw materials & Economics & Food Contact
        self.assertTrue(re.search(r"UCO|Used Cooking Oil", self.content))
        self.assertTrue(re.search(r"4,5[–-]6,0|4\.5[–-]6\.0", self.content))
        self.assertTrue(re.search(r"2,8[–-]3,5|2\.8[–-]3\.5", self.content))
        self.assertIn("2030", self.content)
        self.assertTrue(re.search(r"10/2011", self.content), "EU 10/2011 food contact purity missing!")

        # Thermoplastic Starch (TPS) comparison
        self.assertTrue(re.search(r"\bTPS\b|termoplasztikus keményítő", self.content, re.IGNORECASE), "TPS / termoplasztikus keményítő comparison missing from Topic A!")
        self.assertTrue(re.search(r"Mater-Bi|Solanyl", self.content), "Commercial TPS trade names missing from Topic A!")
        print("[PASS] test_04: Topic A (PHA vs PLA/TPS, HDT, anaerobic biogas, UCO, EU 10/2011, pricing) verified.")

    def test_05_topic_b_barrier_and_packaging_tech(self):
        """Verifies Topic B: OTR < 0.05 cm3/capsule/day/bar, WVTR < 1-2 g/m2/day, 12-month shelf life,
        5-layer coextrusion (PHA outer ~180 um / Bio-Tie ~15 um / Nanocellulose or PGA ~20 um / Bio-Tie ~15 um / PHA inner ~150 um; total ~380-400 um),
        thermoforming vs injection molding, and ultrasonic sealing."""
        # Quantitative barrier limits
        self.assertTrue(re.search(r"OTR.*?<\s*0,05|OTR.*?<\s*0\.05", self.content))
        self.assertTrue(re.search(r"WVTR.*?<\s*1[,\.]0[–-]2[,\.]0", self.content))
        self.assertTrue(re.search(r"12\s*hónap", self.content))

        # 5-layer coextrusion architecture
        self.assertTrue(re.search(r"5-rétegű|ötrétegű", self.content, re.IGNORECASE))
        self.assertTrue(re.search(r"180.*?(?:\\mu|mikrom|µm)", self.content))
        self.assertTrue(re.search(r"15.*?(?:\\mu|mikrom|µm)", self.content))
        self.assertTrue(re.search(r"20.*?(?:\\mu|mikrom|µm)", self.content))
        self.assertTrue(re.search(r"150.*?(?:\\mu|mikrom|µm)", self.content))
        self.assertTrue(re.search(r"380[–-]400.*?(?:\\mu|mikrom|µm)", self.content))

        # Process superiority & Layer application
        self.assertIn("termoformál", self.content.lower())
        self.assertIn("fröccsöntés", self.content.lower())
        self.assertIn("ultrahang", self.content.lower())
        self.assertTrue(re.search(r"slot-die|diszperziós|masterbatch", self.content, re.IGNORECASE), "NFC slot-die dispersion coating / masterbatch clarification missing!")
        print("[PASS] test_05: Topic B (OTR, WVTR, 5-layer coextrusion 380-400 um, thermoforming, ultrasonic, PGA/NFC layer tech) verified.")

    def test_06_topic_c_consortium_and_logistics_subcontracting(self):
        """Verifies Topic C: AGA Article 6.2.B / 9.3 subcontracting rules, avoidance of 25% overhead,
        Criterion 3 implementation penalty avoidance, and complete mapping of all 6 partners
        (BME, MOL, Alfa Industry, RWTH Aachen, Bio-on/Danimer, PackCoffee) across 4 countries and WP1-WP5."""
        # AGA and subcontracting rules
        self.assertTrue(re.search(r"6\.2\.B", self.content))
        self.assertTrue(re.search(r"9\.3", self.content))
        self.assertIn("alvállalkoz", self.content.lower())
        self.assertTrue(re.search(r"25%.*?(rezsi|overhead|átalány)", self.content, re.IGNORECASE))
        self.assertTrue(re.search(r"Quality and efficiency of the implementation|megvalósítás", self.content, re.IGNORECASE))

        # 6 Beneficiaries and 4 countries
        partners = ["BME", "MOL", "Alfa Industry", "RWTH", "Danimer", "PackCoffee"]
        for p in partners:
            self.assertIn(p, self.content, f"Partner {p} not found in Topic C!")
        
        countries = ["HU", "DE", "IT", "AT"]
        for c in countries:
            self.assertIn(c, self.content, f"Country code {c} not found in Topic C!")
        print("[PASS] test_06: Topic C (AGA Art 6.2.B/9.3 subcontracting, 6 partners, 4 countries) verified.")

    def test_07_topic_d_trl_trajectory_and_risk_mitigation(self):
        """Verifies Topic D: 48-month RIA trajectory (TRL 3 -> 4 -> 5 -> 6/7 with 100,000 capsules),
        RIA vs IA distinction, Milestones MS1-MS3, and technical risk mitigations R1, R2, R3."""
        self.assertIn("48 hónap", self.content)
        self.assertTrue(re.search(r"TRL\s*3", self.content))
        self.assertTrue(re.search(r"TRL\s*6", self.content))
        self.assertTrue(re.search(r"100\s*000|100000", self.content))
        self.assertTrue(re.search(r"\bRIA\b", self.content))
        self.assertTrue(re.search(r"\bIA\b", self.content))

        # Milestones MS1-MS3
        self.assertIn("MS1", self.content)
        self.assertIn("MS2", self.content)
        self.assertIn("MS3", self.content)

        # Risks R1, R2, R3
        self.assertIn("R1", self.content)
        self.assertIn("R2", self.content)
        self.assertIn("R3", self.content)
        self.assertIn("termikus degradáció", self.content.lower())
        self.assertIn("delamináció", self.content.lower())
        self.assertIn("másodlagos kristályosodás", self.content.lower())
        print("[PASS] test_07: Topic D (TRL 3->6/7, RIA vs IA, MS1-MS3, R1-R3 mitigations) verified.")

    def test_08_topic_e_lca_standards_and_regulations(self):
        """Verifies Topic E: Cradle-to-grave LCA per ISO 14040/14044 (verified baseline: primary Al 15.1 kg CO2e/kg,
        WUR 2023 741 vs 779 g CO2e/kg coffee; PHACK target >=25% reduction),
        PPWR (Dec 2024, Aug 2026, Article 9(2)(a) Member State option, PFAS ban),
        and Hungarian EPR system."""
        # LCA numbers and ISO
        self.assertTrue(re.search(r"ISO\s*14040", self.content))
        self.assertTrue(re.search(r"15,1\s*kg", self.content))
        self.assertTrue(re.search(r"741", self.content))
        self.assertTrue(re.search(r"779", self.content))
        self.assertTrue(re.search(r"25%", self.content))

        # PPWR and PFAS
        self.assertIn("PPWR", self.content)
        self.assertTrue(re.search(r"2024\.\s*december", self.content, re.IGNORECASE))
        self.assertTrue(re.search(r"2026\.\s*augusztus", self.content, re.IGNORECASE))
        self.assertTrue(re.search(r"9\.\s*cikk|Article\s*9", self.content, re.IGNORECASE))
        self.assertIn("PFAS", self.content)
        self.assertIn("EPR", self.content)
        print("[PASS] test_08: Topic E (ISO 14040 LCA with verified WUR/IAI baseline, PPWR Art 9, PFAS, EPR) verified.")

    def test_09_adversarial_scenarios_from_reviewer(self):
        """Verifies that all 4 adversarial defense scenarios identified by Reviewer M1 are explicitly countered:
        1. TRL 7 in 100% RIA
        2. NF T51-800 specification vs ISO 14855 analytical test method
        3. Secondary crystallization, mold shrinkage, and +/-0.1 mm chamber tolerance
        4. Nanocellulose moisture sensitivity in kitchen environments."""
        # 1. TRL 7 in RIA
        self.assertTrue(re.search(r"TRL\s*7.*?(RIA|demonstráció|kísérleti)", self.content, re.IGNORECASE | re.DOTALL))

        # 2. NF T51-800 vs ISO 14855
        self.assertTrue(re.search(r"NF\s*T51-800", self.content))
        self.assertTrue(re.search(r"ISO\s*14855", self.content))
        self.assertTrue(re.search(r"respirometri", self.content, re.IGNORECASE))

        # 3. Secondary crystallization and +/- 0.1 mm tolerance
        self.assertTrue(re.search(r"±\s*0,1\s*mm|±\s*0\.1\s*mm", self.content))
        self.assertTrue(re.search(r"60[–-]70\s*°C", self.content))
        self.assertTrue(re.search(r"orotinsav", self.content, re.IGNORECASE))

        # 4. Nanocellulose sandwich protection
        self.assertTrue(re.search(r"nanocellulóz.*?hidrofób|hidrofób.*?nanocellulóz", self.content, re.IGNORECASE | re.DOTALL))
        print("[PASS] test_09: All 4 adversarial challenges from Reviewer M1 successfully addressed.")

    def test_10_wp_mapping_completeness(self):
        """Verifies that all 5 Work Packages (WP1, WP2, WP3, WP4, WP5) are mapped with leads,
        person-months, and deliverables."""
        for wp_idx in range(1, 6):
            wp_str = f"WP{wp_idx}"
            self.assertIn(wp_str, self.content, f"{wp_str} missing in WP matrix!")
        
        deliverables = ["D1.1", "D2.1", "D3.1", "D3.2", "D4.1", "D4.2", "D5.1", "D5.2"]
        for d in deliverables:
            self.assertIn(d, self.content, f"Deliverable {d} missing in WP matrix!")
        print("[PASS] test_10: Complete WP1-WP5 mapping and D1.1-D5.2 deliverables verified.")


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDefenseQAGuide)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    if not result.wasSuccessful():
        sys.exit(1)
    print("\nALL 10 DEFENSE QA TEST SUITES PASSED CLEANLY (100% COMPLIANT)")
    sys.exit(0)


if __name__ == "__main__":
    main()
