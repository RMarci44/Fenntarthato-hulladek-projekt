# Teendők és Felkészülési Ütemterv (TODO / Roadmap)

Ez a dokumentum nyomon követi a PHACK projekt és a kurzus aktuális állapotát, az előadói felkészülést és a hátralévő teendőket.

---

## 🎯 Aktuális Státusz (Áttekintés)

- [x] **Projektötlet és koncepció kidolgozása** (PHA kávékapszula, TRL 3 ➔ 6/7, Horizon Europe RIA, GY02 gyakorlat).
- [x] **Konzorcium felépítése** (6 partner: BME, MOL, Alfa Industry, RWTH Aachen, Bio-on, PackCoffee).
- [x] **Munkacsomagok és költségvetés tervezése** (WP1–WP5, 4,2M EUR, 520 PM).
- [x] **Végleges prezentáció összeállítása** (`PHACK_Prezentacio_Vegleges.pptx` – 24 dia a hivatalos BME PT kurzussablonban, `GY02` csoportkóddal, `x/24` diaszámozással, automatikus kulcsszó-kiemeléssel; egyedi mérnöki ábrák a `phack_figures.py` modulból [1–2. dia emblémalogó, 3., 4., 5., 6., 7., 8., 11. (KPI mini-ábrák), 14., 15., 16., 20., 21., 22. dia], hivatalos Horizon Europe táblázatokkal [Table 3.1a–3.1f és 3.2], beágyazott jegyzetekkel, és `slides_rendered/` mappában mind a 24 dia 1280×960 PNG renderével).
- [x] **Előadói felkészülés és szövegkönyv (Speaker Notes)** (12 perces limit szigorú betartása: `SPEAKER_NOTES.md` és beépített PPTX jegyzetek kész).
- [x] **Bírálói / Kérdezői felkészülés (Q&A)** (3 perces vitablokk lehetséges kérdései: `DEFENSE_QA.md`, Topics A–F, Top 10 csapdakérdéssel, `test_defense_qa.py` tesztkészlettel validálva).
- [x] **Önálló felkészítő dokumentum** (`FELKESZULESI_UTMUTATO.md`: nulláról tanulható összefoglaló, kulcsszámok, diánkénti lényeg, próbarend) és **forrásjegyzék** (`FORRASOK.md`).

---

## 📋 Részletes Teendők (Bontásban)

### 1. Prezentációs Szövegkönyv és Időgazdálkodás (12 perc)
A 24 diát 6 hallgatónak kell előadnia. Átlagosan **30 másodperc / dia** áll rendelkezésre, összesen pontosan 12:00 perc (720 mp) és 1515 szó!

- [x] **Hallgató 1 (Koordinátor, 1–3. dia):** 90 mp (1:30), 200 szó
  - Cím, alapadatok, Horizon Europe felhívás, a 10 milliárdos hulladékprobléma, a 6 fős konzorcium és értéklánc.
- [x] **Hallgató 2 (RD 1, 4–8. dia):** 160 mp (2:40), 363 szó
  - Stratégiai célkitűzések, TRL 3 ➔ 7 ugrás igazolása, PHA anyagi előnyei vs. PLA, technológiai folyamatlépések (fermentációtól termoformálásig).
- [x] **Hallgató 4 (Innováció & Piac, 9–11. és 20. dia):** 120 + 30 = 150 mp (2:30), 222 + 63 = 285 szó
  - Igények és célcsoportok (PPWR rendelet), környezeti/gazdasági hatások, a 4 fő KPI mutató, kockázatkezelési mátrix (R1–R3).
- [x] **Hallgató 5 (Disszemináció, 12–13. dia):** 80 mp (1:20), 163 szó
  - Tudományos disszemináció (5 Q1 cikk, Open Data, CEN szabványosítás), fogyasztói edukáció („Hová dobjam?” kampány), döntéshozói tájékoztatók.
- [x] **Hallgató 3 (RD 2, 14–17. dia):** 120 mp (2:00), 249 szó
  - Munkacsomagok (WP1–WP5), WP1-2 kompoundálás, WP3 síkfólia és termoformálás, WP4 biodegradáció (EN 13432) és LCA.
- [x] **Hallgató 6 (Pénzügy & Menedzsment, 18–19. és 21–24. dia):** 50 + 70 = 120 mp (2:00), 102 + 153 = 255 szó
  - Mérföldkövek és deliverable-ök, Gantt ütemterv (4 év), 4,2M EUR költségvetés megoszlása, hallgatói szerepkörök és zárszó.

---

### 2. Lehetséges Tanári Kérdések és Védési Érvek (Q&A)

- [x] **Kérdés 1 (Alapanyag ár és gazdaságosság - Topic A):** *„Nem túl drága a PHA az alumíniumhoz és a PP-hez képest?”*
  - **Válasz:** A méretnöveléssel (WP3) és a Danimer nagyüzemi fermentációjával (UCO / melasz szénforrások) a költségprémium 10% alá szorul (2,8–3,5 €/kg 2030-ra). Emellett az új EU PPWR rendelet és az EPR eko-modulációs díjak a nem lebomló/nem újrahasznosítható kapszulákat drasztikusan megdrágítják.
- [x] **Kérdés 2 (Oxigén- és aromazárás - Topic B):** *„Hogyan biztosítható, hogy a kávé ne avasodjon meg 12 hónap alatt?”*
  - **Válasz:** Koextrudált 5-rétegű bio-barrier fóliát alkalmazunk (PHA külső 180 µm / Tie 15 µm / Nanocellulóz vagy PGA mag 20 µm / Tie 15 µm / PHA belső 150 µm; WP3), amely garantálja az OTR < 0,05 cm³/(kapszula·nap·bar) értéket (12 hónap aroma- és lipoprotekció).
- [x] **Kérdés 3 (Konzorcium és alvállalkozás - Topic C):** *„Miért nincs logisztikai partner a konzorciumban?”*
  - **Válasz:** A felhívás kutatás-fejlesztési fókuszú (RIA). A Horizon Europe AGA Art. 6.2.B és 9.3 alapján a szállítás nem innovatív commodity szolgáltatás, így alvállalkozási költségként számolható el. Partnerként 25% indokolatlan overheadet vonna el és pontlevonást okozna (Criterion 3).
- [x] **Kérdés 4 (TRL 3 -> 6/7 ugrás és kockázatkezelés - Topic D):** *„Hogyan igazolható a TRL ugrás és a 100 000 darabos pilot gyártás egy RIA projektben?”*
  - **Válasz:** A 48 hónap alatt BME laboratóriumi PoC-ból kiindulva a MOL és Alfa meglévő gépparkján történik a méretnövelés. A 100 000 db nem kereskedelmi értékesítés, hanem nagysebességű (400 db/perc) töltősori folyamatképesség-ellenőrzés és akkreditált EN 13432 biodegradációs mintaszükséglet.
- [x] **Kérdés 5 (LCA, biogáz és PPWR jogszabályok - Topic E):** *„Mennyivel zöldebb a PHA, és hogyan illeszkedik a hazai hulladékgazdálkodáshoz?”*
  - **Válasz:** ISO 14040/44 szerinti bölcsőtől-sírig LCA (WP4): célérték legalább 25% CO2e-csökkentés az alumíniumhoz képest (WUR 2023: komposztálható 741 vs. alumínium 779 g CO2e/kg kávé). A MOHU barna kuka közvetlenül biogázüzembe viszi, ahol a PHA 30–45 nap alatt biometánná alakul, míg a PLA nem degradálódik. A PPWR 9. cikk (2) a) szerint a tagállamok előírhatják a merev kapszulák komposztálhatóságát.

---

### 3. Előadás előtti ellenőrzőlista (próbarend)
 
- Legalább 2 teljes, stopperrel mért főpróba az éles sorrendben (H1, H2, H4, H5, H3, H6, H4, H6); cél: 12:00 ±15 mp.
- Mindenki fejből tudja a saját diáinak kulcsszámait (`FELKESZULESI_UTMUTATO.md` – „Kulcsszámok puskája”).
- A 19 ➔ 20. és 20 ➔ 21. dia kézátadás (prezenter) begyakorolva.
- Q&A: a Top 10 csapdakérdés és a Topic F (költségvetés, források) 15 másodperces válaszai mindenkinek megvannak.
- Kinyomtatott/offline tartalék: PPTX + PDF export + jegyzetek; a projektor 4:3 felbontása kipróbálva.
- A hallgatói nevek és Neptun-kódok a 23. dián a végleges csoportadatokra cserélve (jelenleg: Hallgató 1–6 / NEPTUN1–6; a szkriptben a 23. dia táblázata). Az előadás dátuma: 2026.11.12. (címlap és 23. dia).
