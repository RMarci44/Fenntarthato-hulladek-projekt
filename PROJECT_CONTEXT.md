# PHACK – Projekt Kontextus és Pályázati Adatlap

Ez a dokumentum rögzíti a **Fenntartható hulladékgazdálkodás** MSc kurzus keretében készített innovációs pályázati projekt részleteit, műszaki adatait és oktatói követelményeit.

---

## 📌 Alapadatok

| Paraméter | Érték |
|---|---|
| **Projekt neve / Akronim** | **PHACK** (PHA Coffee Capsule Packaging) |
| **Pályázat címe** | Biológiailag lebomló PHA-alapú kávékapszula és élelmiszercsomagolási rendszer |
| **Gyakorlat és Projektkód** | **GY02 gyakorlat, P01 projekttéma** |
| **Pályázati felhívás** | HORIZON-CL6-2026-CIRCBIO: Circular bio-based packaging |
| **Támogatási forma** | Research and Innovation Action (RIA) |
| **Futamidő** | 48 hónap (4 év) |
| **Összköltségvetés** | 4 200 000 EUR (100% EU támogatási intenzitás, 520 PM) |
| **TRL Ugrás** | **TRL 3** (laboratóriumi elvigazolás) ➔ **TRL 6** (M36, MS3: ipari pilot, 100 000 db legyártva, D3.2) ➔ **TRL 7** (M44–M48: üzemi töltősori validáció, barista teszt, akkreditált komposztálhatósági igazolás, D4.1) |
| **Prezentáció fájl** | `PHACK_Prezentacio_Vegleges.pptx` (24 dia) |
| **Dokumentumok** | Kiindulópont: `FELKESZULESI_UTMUTATO.md`; beszédszöveg: `SPEAKER_NOTES.md`; vita: `DEFENSE_QA.md`; források és ellenőrzöttség: `FORRASOK.md`; döntések: `DECISIONS.md`; státusz: `TODO.md` |
| **Csoportlétszám** | 6 hallgató (Koordinátor, RD1, RD2, Innováció/Piac, Disszemináció, Pénzügy/Menedzsment) |

---

## 🔬 Műszaki & Technológiai Lényeg

### 1. A Probléma
Évente az EU-ban nagyságrendileg több tízmilliárd (WUR-becslés: ~53 milliárd) alumínium és nem lebomló műanyag kávékapszula használódik el; a használtnak csak mintegy negyedét gyűjtik vissza (NL), a többi jellemzően égetőbe vagy lerakóba kerül (legalább 10 milliárd db/év). Az újrahasznosítás a zacc mechanikai szétválasztásának nehézsége miatt gyenge.

### 2. A Megoldás
- **Alapanyag:** 100%-ban természetes eredetű, baktériumok által bioszintetizált **Polihidroxialkanoát (PHA)** (pl. cukorrépa-melaszból és mezőgazdasági melléktermékekből).
- **Előny a PLA-val szemben:** 
  - A PLA csak ipari komposztálóban (58°C felett) bomlik, és alacsony a hőállósága (~55°C).
  - A **PHA otthoni kerti talajban (20-25°C) és édes/tengervízben is lebomlik** 6–12 hónapon belül!
  - Hőállósága >95°C (akár 120°C-ig alakstabil), elviseli a kávéfőzés 15–19 bar nyomását és forró vizét.
  - A használt kapszula a kávézaccal együtt komposztálható, nincs mikroműanyag-képződés (víz, CO₂, biomassza a végtermék).
- **Gyártási eljárás:** 
  - Kétcsigás kompoundálás (természetes nukleálószerekkel – pl. orotinsav, talkum, nanocellulóz – és bio-lágyítókkal).
  - Ipari síkfólia koextrúzió (0,38–0,40 mm [0,35–0,45 mm] 5-rétegű bio-barrier szalag: PHA külső 180 µm / Bio-Tie 15 µm / Nanocellulóz vagy PGA záróréteg 20 µm / Bio-Tie 15 µm / PHA belső 150 µm).
  - Nagysebességű precíziós termoformálás temperált (60–70°C) szerszámban (<3,5 mp ciklusidő) és ultrahangos fedőfólia-hegesztés (20–35 kHz).

---

## 🤝 A Teljes Értékláncot Lefedő Konzorcium

| # | Szervezet | Típus | Ország | Szerepkör az Értékláncban | Költségkeret |
|---|---|---|---|---|---|
| **1** | **BME Polimertechnika Tanszék** | RTO | HU | Projektkoordinátor, receptúrafejlesztés, laboratóriumi vizsgálatok | 1 050 000 EUR (144 PM) |
| **2** | **MOL Nyrt.** | IND | HU | Ipari kompoundálás, síkfólia extrúzió, méretnövelés | 850 000 EUR (100 PM) |
| **3** | **Alfa Industry Kft.** | SME | HU | Szerszámkészítés, termoformálás, prototípus és kisszériás gyártás | 650 000 EUR (90 PM) |
| **4** | **RWTH Aachen University** | RTO | DE | Biodegradációs vizsgálatok (EN 13432), talajtoxicitás, teljes LCA | 750 000 EUR (96 PM) |
| **5** | **Danimer / Bio-on EU PHA Pilot (Kaneka PHBH ref.)** | IND | IT | Ipari fermentációs PHA/PHBH alapanyag előállítása bio-hulladékból | 550 000 EUR (50 PM) |
| **6** | **PackCoffee Europe Barista Alliance** | ASSO/IND | AT | Iparági szövetség, töltősori tesztek (400 db/perc), UH hegesztés, barista validáció | 350 000 EUR (40 PM) |

> **Fontos oktatói szempont (`info.txt`):** Logisztikai céget tilos partnerként bevonni (nincs érdemi K+F szerepe); ha szükséges, alvállalkozóként jelenhet meg.

---

## ⚙️ Munkacsomagok (Work Packages)

- **WP1: Igényfelmérés, alapanyag specifikáció és szabályozás (M1–M12)** – Vezető: RWTH (68 PM)
- **WP2: PHA kompoundálás és receptúrafejlesztés (M6–M24)** – Vezető: BME (144 PM)
- **WP3: Síkfólia extrúzió és kísérleti termoformálás (M18–M36)** – Vezető: MOL (136 PM)
- **WP4: Biodegradáció, élelmiszerbiztonság és LCA elemzés (M24–M44)** – Vezető: RWTH (96 PM)
- **WP5: Projektmenedzsment, disszemináció és hasznosítás (M1–M48)** – Vezető: BME (76 PM)

---

## 📊 Fő KPI Mutatók és Mérföldkövek

1. **Versenyképes önköltség (KPI 1):** Ipari méretnövelés után legfeljebb **< +10% árprémium** a hagyományos alumínium kapszulákhoz képest (feltételezett PHA ár 2030-ra: 2,8–3,5 €/kg).
2. **Piacpenetráció (KPI 2):** Projekt után 2 éven belül **> 2%-os kiváltási arány** a közép-európai prémium kávépiacon (évi >500 millió bio-kapszula, ~500 t kapszulahulladék-megelőzés, ~1 g/db).
3. **Lebomlási szabvány és LCA (KPI 3):** Házi komposztban **<12 hónap** (180–360 nap), ipari komposztban **<6 hónap** alatt >90%-os biodegradáció (EN 13432, NF T51-800, ISO 14855), valamint **legalább 25% CO₂e-csökkentés** az alumínium kapszulához képest (célérték; ISO 14040/44 bölcsőtől-sírig LCA a WP4-ben). Irodalmi kiindulás: primer alumínium 15,1 kg CO₂e/kg (IAI 2022); WUR 2023: komposztálható kapszula 741 vs. alumínium 779 g CO₂e/kg kávé (kávé nélkül).
4. **Oxigén- és aromazárás (KPI 4):** **OTR < 0,05 cm³/(kapszula·nap·bar)** és WVTR < 1,0–2,0 g/(m²·nap) a 12 hónapos minőségmegőrzéshez védőgázas külső tasak nélkül.
5. **Mérföldkövek és Kulcs Deliverable-ök:**
   - **MS1 (M12):** Alapanyag-specifikáció, gépészeti toleranciák és élelmiszeripari engedélyezési terv elfogadva (`D1.1`).
   - **MS2 (M24):** Optimalizált PHA kompound granulátum (50 kg) és az első 1 000 db laboratóriumi kapszula prototípus sikeres termoformálása (`D2.1`, TRL 4).
   - **MS3 (M36):** 100 000 db demonstrációs kapszula ipari próbagyártása, 400 db/perc próbatöltése és előzetes EN 13432 auditja (`D3.1`, `D3.2`, TRL 6); a TRL 7 üzemi validáció M44–M48-ig zárul (`D4.1`).
   - **Zárás (M44–M48):** Akkreditált biodegradációs jelentés (`D4.1`), teljes bölcsőtől-sírig LCA (`D4.2`), disszeminációs kampány (`D5.1`) és zárójelentés (`D5.2`).

---

## ⏱️ Prezentációs Szabályok (`info.txt` alapján)

- **Időkeret:** Szigorúan **12 perc előadás + 3 perc vita** (15 percnél kötelezően leállítják).
- **Diaszámozás:** Kötelező formátum a diákon: `dia száma / összes dia` (pl. `1/24`).
- **Nyelv:** Egységesen egy nyelv (magyar vagy angol), a diák és az előadás nyelve azonos.
- **Tartalmi fókusz:**
  - Konkrét polimer és gyártástechnológia bemutatása.
  - TRL szintek műszaki alátámasztása.
  - Specifikus (nem általános) statisztikák a kávékapszulák és a PHA piacáról.
  - Konkrét, egyedi WP feladatok.
