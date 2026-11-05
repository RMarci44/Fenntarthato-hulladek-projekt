# PHACK – Felkészülési útmutató nulláról (egy dokumentumból tanulható és előadható)

Ez a dokumentum önmagában elég ahhoz, hogy egy csapattag a projektet megértse, a saját részét előadja és a bizottság kérdéseire válaszoljon. A részletek külön fájlokban vannak (lásd a 10. fejezetet), de a „Mit mondjak, ha…” kérdésekre itt is van válasz.

---

## 1. A projekt egy mondatban és 30 másodpercben

**Egy mondat:** A PHACK egy 4,2 millió eurós, 48 hónapos Horizon Europe RIA-projekt, amely a kávékapszulát 100%-ban biológiailag lebomló PHA/PHBH-ból (baktériumok által termelt biopoliészter) készíti, így a használt kapszula a zaccal együtt a házi komposztba, vagy a barna kukába dobható.

**30 másodperc:** Évente több tízmilliárd egyadagos kapszula készül alumíniumból és fosszilis műanyagból, a nagy részük a lerakóba vagy az égetőbe kerül, mert a nedves zacc miatt nem érdemes szétválogatni. A PLA-alapú „bio” kapszula forró vízben (Tg ≈ 55–60 °C) meglágyul, és csak ipari komposztálóban bomlik le. A PHA hőálló (HDT > 95 °C), 15–19 bar nyomást bír, és házi komposztban is lebomlik. A konzorcium (6 partner, 4 ország) a labortól (TRL 3) az ipari pilotig (TRL 6, M36), majd az üzemi töltősori validációig (TRL 7, M44–M48) viszi el a technológiát.

**Pályázati keret:** HORIZON-CL6-2026-CIRCBIO „Circular bio-based packaging”, RIA, 100% EU-támogatási intenzitás, koordinátor: BME Polimertechnika Tanszék. Tárgy: Fenntartható hulladékgazdálkodás (BMEGEPTNX01 / BMEGEPTMSVFEHU-01), GY02 gyakorlat, P01 projekttéma.

---

## 2. Kulcsszámok puskája (ezeket mindenkinek fejből kell tudnia)

| Téma | Szám |
|---|---|
| Költségvetés | **4 200 000 €**, 100% EU-támogatás |
| Futamidő | **48 hónap** |
| Emberhónap | **520 PM**, átlag **4 000 €/PM** (sablon: 3–4000 €/PM) |
| Partnerek / országok | **6 partner, 4 ország** (HU, DE, IT, AT) |
| Hazai arány | **2,55 M€ (60,7%)**, 334 PM |
| TRL | **3 → 6 (M36) → 7 (M44–M48)** |
| Pilot | **100 000 db** kapszula (D3.2, M36), **400 db/perc** töltősor |
| Film | **5 rétegű, 380–400 µm**: PHA 180 / Tie 15 / NFC-PGA 20 / Tie 15 / PHA 150 µm |
| Barrier | **OTR < 0,05 cm³/(kapszula·nap·bar)**, WVTR < 1–2 g/(m²·nap), 12 hónap eltarthatóság |
| Hőállóság | **HDT > 95–105 °C**, 15–19 bar extrakció, temperált szerszám 60–70 °C, ciklusidő < 3,5 mp |
| Lebomlás | házi komposzt (20–25 °C) **< 12 hónap** (NF T51-800), ipari komposzt **< 6 hónap** (EN 13432), > 90% |
| KPI 1 | árprémium **< +10%** az alumíniumhoz képest |
| KPI 2 | **> 2%** kiváltás a közép-európai prémium piacon 2 éven belül |
| KPI 3 | **≥ 25% CO₂e-csökkentés** az alumínium kapszulához képest (célérték, ISO 14040/44 LCA, WP4) |
| KPI 4 | **OTR < 0,05**, védőgázas tasak nélkül |
| Piac (diák) | ~53 milliárd db/év az EU-ban (WUR 2023, nyers becslés); a használt kapszulák ~25%-át gyűjtik vissza (NL, WUR 2025); a piac ~7–8,5%/év nő |
| Munkacsomagok (PM) | WP1 **68**, WP2 **144**, WP3 **136**, WP4 **96**, WP5 **76** (összesen 520) |
| Partnerek (€ / PM) | BME 1,05 M / 144; MOL 850 k / 100; ALFA 650 k / 90; RWTH 750 k / 96; BIO 550 k / 50; PCOFF 350 k / 40 |
| Költségkategóriák | Személyi **2 080 000 € (50%)**, utazás és ellátás 130 000 € (3%), felszerelés 670 000 € (16%), egyéb áru/szolgáltatás 480 000 € (11%), indirekt (25% átalány) 840 000 € (20%) |

Az indirekt a közvetlen költség 25%-a: 840 000 / 3 360 000 = 25%.

---

## 3. Fogalomtár (rövid és szóban is használható)

| Fogalom | Jelentés |
|---|---|
| **PHA / PHBH** | Polihidroxialkanoát: baktériumok által cukorból, melaszból, mezőgazdasági melléktermékből vagy használt sütőolajból (UCO) fermentált, természetes eredetű poliészter. A PHBH egy rugalmasabb kopolimer. |
| **PLA** | Politejsav: keményítőből készülő bioműanyag; alacsony hőállóságú, csak ipari komposztálóban bomlik. |
| **HDT** | Heat Deflection Temperature: az a hőmérséklet, ameddig az anyag terhelés alatt alakstabil. |
| **Tg / Tm** | Üvegesedési hőmérséklet / olvadáspont. |
| **Nukleálószer** | Adalék (orotinsav, talkum, nanocellulóz), amely gyorssá és egyenletessé teszi a lassú PHA-kristályosodást. |
| **Koextrúzió** | Több polimerréteg egyidejű extrudálása egyetlen fóliává (itt 5 réteg). |
| **Tie-réteg** | Kötőréteg, amely a polár barrier- és a PHA-rétegeket összetapasztja. |
| **NFC / PGA** | Nanocellulóz / poliglikolsav: oxigéngátló rétegek. |
| **OTR / WVTR** | Oxigén- / vízgőz-áteresztési sebesség: a kávé aromájának és eltarthatóságának mérőszáma. |
| **Termoformálás** | Fólia felmelegítése és kapszula alakúra mélyhúzása (ALFA szerszámában). |
| **TRL** | Technology Readiness Level (1–9). RIA-ban TRL 5–6 körül a cél, kereskedelmi bevezetés tilos. |
| **RIA** | Research and Innovation Action: Horizon Europe projekttípus, 100% EU-támogatás. |
| **PM** | Person-month (emberhónap): 168 munkaóra. |
| **WP / MS / D** | Work Package (munkacsomag) / Milestone (mérföldkő) / Deliverable (leszállítandó eredmény). |
| **EN 13432** | Ipari komposztálhatósági szabvány (≥ 90% lebomlás 6 hónap alatt, 58 °C). |
| **NF T51-800** | Francia szabvány a házi komposztálhatóságra (20–30 °C). |
| **ISO 14855** | CO₂-fejlődést mérő biodegradációs vizsgálati módszer (a bomlás mérésére, nem a „házi komposzt” szabványa). |
| **ISO 14040/44** | LCA (életciklus-elemzés) keretszabvány; itt bölcsőtől a sírig. |
| **PPWR** | EU csomagolási rendelet, amely a kapszulák komposztálhatóságát is szabályozza. |
| **EPR** | Extended Producer Responsibility: kiterjesztett gyártói felelősség, a díjat a forgalmazó fizeti. |
| **SUP** | Single-Use Plastics irányelv. |
| **Cpk** | Folyamatképességi index; > 1,33 = a gyártási folyamat statisztikailag képes. |
| **Stage-gate / Go–No-Go** | Mérföldkőnél döntés a folytatásról (MS1, MS2, MS3). |
| **PU / SEN** | Nyilvános (Public) / szenzitív (Sensitive) deliverable-minősítés. |
| **Indirekt költség (25% átalány)** | HE szabály: a közvetlen költségek 25%-a rezsiként átalánydíjas. |
| **Alvállalkozás** | Szolgáltatás vásárlása (pl. logisztika); nem K+F részvétel, ezért nem partner. |

---

## 4. Probléma, megoldás, miért PHA?

**Probléma.** A primer alumínium előállítása globális átlagban ~15 kg CO₂e / kg (IAI, 2022). A kapszulában marad a nedves, olajos zacc, ezért a válogatás gazdaságtalan, és a kapszulák többnyire a vegyes hulladékba kerülnek (NL: a használtnak ~25%-át gyűjtik vissza). A PLA-bio-kapszulák forró vízben meglágyulnak és csak ipari komposztban bomlanak. A PPWR (2026. aug. 12-től) nevesíti a kapszulákat, a komposztálhatóságot a tagállamok előírhatják; az EPR-díjak a komposztálható megoldás felé terelik a piacot.

**Megoldás.** PHA/PHBH mátrix, orotinsavval és talkummal nukleálva, 5 rétegű bio-barrier fóliából termoformálva, ultrahangosan hegesztett PHA záró fóliával.

| | PLA | PHA/PHBH |
|---|---|---|
| Hőállóság | ~55 °C | HDT > 95 °C (receptúrától 120 °C-ig) |
| Házi komposzt | nem bomlik | bomlik, 6–12 hónap |
| Víz / tenger | nem bomlik, mikroműanyag | lebomlik |
| Zacc | nehezen szeparálható | zaccal együtt komposztálható |
| Ár | olcsóbb | drágább (ezért a KPI 1 és a méretnövelés) |

**Gyártási lánc (8. dia):** (1) baktériumos fermentáció (BIO) → (2) kétcsigás kompoundálás (BME, MOL) → (3) 5 rétegű síkfólia koextrúzió (MOL) → (4) temperált termoformálás (ALFA) → (5) ultrahangos hegesztés és töltés (PCOFF) → (6) komposztálhatósági vizsgálat és LCA (RWTH).

---

## 5. Konzorcium és szerepek

| # | Partner | Típus | Ország | Szerep | WP-vezetés |
|---|---|---|---|---|---|
| 1 | BME Polimertechnika Tanszék | RTO | HU | Koordinátor, receptúra, labor | WP2, WP5 |
| 2 | MOL Nyrt. | IND | HU | Kompoundálás, koextrúzió, méretnövelés | WP3 |
| 3 | Alfa Industry Kft. | SME | HU | Szerszám, termoformálás | – |
| 4 | RWTH Aachen University | RTO | DE | EN 13432, ökotoxicitás, LCA | WP1, WP4 |
| 5 | Danimer / Bio-on EU PHA Pilot (Kaneka PHBH ref.) | IND | IT | PHA/PHBH alapanyag-fermentáció | – |
| 6 | PackCoffee Europe Barista Alliance | ASSO/IND | AT | Iparági szövetség, töltősori tesztek, barista validáció | – |

**Miért nincs logisztikai partner?** A szállítás nem K+F, ezért alvállalkozói szolgáltatás (AGA 6.2.B, 9.3). Ez az oktatói követelmény (`info.txt`) is.

**Csapat és szerepkörök (23. dia):** Hallgató 1 Koordinátor; Hallgató 2 R&D 1; Hallgató 3 R&D 2; Hallgató 4 Innováció és piac; Hallgató 5 Disszemináció; Hallgató 6 Menedzsment és pénzügy.

---

## 6. Munkacsomagok, mérföldkövek, deliverable-ök

| WP | Cím | Hónapok | Vezető | PM |
|---|---|---|---|---|
| WP1 | Igényfelmérés, specifikáció, szabályozás | M1–M12 | RWTH | 68 |
| WP2 | PHA kompoundálás, receptúrafejlesztés | M6–M24 | BME | 144 |
| WP3 | Síkfólia koextrúzió, termoformálás, töltősori pilot | M18–M36 | MOL | 136 |
| WP4 | Biodegradáció, élelmiszerbiztonság, LCA | M24–M44 | RWTH | 96 |
| WP5 | Menedzsment, disszemináció, hasznosítás | M1–M48 | BME | 76 |

| Mérföldkő | Hónap | Tartalom | TRL |
|---|---|---|---|
| MS1 | M12 | Specifikáció, tűrések és élelmiszeripari engedélyezési terv (D1.1) | – |
| MS2 | M24 | 50 kg optimalizált PHA kompound és az első 1 000 db labor-kapszula (D2.1) | 4 |
| MS3 | M36 | 100 000 db kapszula ipari legyártása (D3.2), 400 db/perc próbatöltés, előzetes EN 13432 audit (D3.1) | **6** |
| Zárás | M44–M48 | Akkreditált biodegradációs jelentés (D4.1), LCA (D4.2), disszeminációs kampány (D5.1), zárójelentés (D5.2) | **7** |

**Miért 100 000 db egy RIA-ban?** Nem kereskedelmi eladás, hanem a statisztikai folyamatképesség (Cpk > 1,33) és az akkreditált vizsgálat (EN 13432) mintaigénye. A TRL 8–9 és a piaci bevezetés nem része a projektnek.

**TRL-időzítés (a „csapda”):** 100 000 db legyártása és próbatöltés **M36** (TRL 6). A **TRL 7** az M44–M48 közötti üzemi töltősori validáció (barista teszt, akkreditált igazolás, D4.1). Ne keverjük: a 100 000 db nem M48-ra készül el.

**Kockázatok (20. dia):** R1–R3 mátrix; a kulcs a kettős barrier tartalék (R2) és a stage-gate kapuk (Go/No-Go az MS-eknél).

---

## 7. Diánkénti egymondatos lényeg és előadó

| Dia | Cím | Egymondatos lényeg | Előadó | Idő |
|---|---|---|---|---|
| 1 | Címlap | Név, felhívás, 48 hó, 4,2M€, TRL 3→7. | H1 | 25 mp |
| 2 | Alapadatok | Akronim, felhívás, költség, PM, kulcsszavak; absztrakt: probléma → megoldás → áttörés → TRL. | H1 | 35 mp |
| 3 | Konzorcium | 6 partner, 4 ország, teljes értéklánc; miért nincs logisztikai partner. | H1 | 30 mp |
| 4 | Célok | 4 pillér (hőstabil kompound, 5 rétegű barrier, lebonthatóság, drop-in kompatibilitás); túl a PLA-n. | H2 | 30 mp |
| 5 | TRL | TRL 3 → 6 (M36) → 7 (M44–M48) stage-gate pálya. | H2 | 30 mp |
| 6 | Piaci probléma | Hulladékstatisztikák, PPWR/SUP/EPR/MOHU. | H2 | 30 mp |
| 7 | PHA vs PLA | Miért PHA: hőállóság, házi komposzt, mikroműanyag-mentesség. | H2 | 35 mp |
| 8 | Folyamatlánc | Fermentáció → kompoundálás → koextrúzió → termoformálás → töltés → vizsgálat. | H2 | 35 mp |
| 9 | Igények | Célcsoportok, EU Green Deal, PPWR illeszkedés. | H4 | 40 mp |
| 10 | Hatások | Ökológiai, gazdasági, társadalmi hasznok. | H4 | 40 mp |
| 11 | 4 KPI | Önköltség, piaci kiváltás, lebomlás/LCA, barrier. | H4 | 40 mp |
| 12 | Disszemináció | 5 Q1 cikk, nyílt tudomány, CEN szabványosítás. | H5 | 40 mp |
| 13 | Kommunikáció | „Hová dobjam?” kampány, zöldmosás elleni fellépés. | H5 | 40 mp |
| 14 | WP lista (3.1a) | 5 WP, vezetők, PM-ek + részfeladat-szintű (T1.1–T5.3) PERT-háló. | H3 | 30 mp |
| 15 | WP1–WP2 (3.1b) | Táblázat 3.1b: specifikáció/szabályozás és PHA kompoundálás. | H3 | 30 mp |
| 16 | WP3 (3.1b) | Táblázat 3.1b: koextrúzió, termoformálás, töltősori pilot. | H3 | 30 mp |
| 17 | WP4–WP5 (3.1b) | Táblázat 3.1b: biodegradáció, LCA, menedzsment. | H3 | 30 mp |
| 18 | Mérföldkövek (3.1d) | MS1–MS3 stage-gate. | H6 | 25 mp |
| 19 | Deliverable-ök (3.1c) | D1.1–D5.2, PU/SEN egyensúly. **Átadás H4-nek.** | H6 | 25 mp |
| 20 | Kockázatok (3.1e) | R1–R3, kettős barrier tartalék. **Visszaadás H6-nak.** | H4 | 30 mp |
| 21 | Gantt | 48 hónap, WP-átfedések, MS-ek. | H6 | 25 mp |
| 22 | Költségek (3.1f) | 4,2M€, 520 PM, 5 költségkategória. | H6 | 25 mp |
| 23 | Csapat | Szerepkörök és tárgyadatok. | H6 | 10 mp |
| 24 | Zárás | Zárszó, kérdések. | H6 | 10 mp |

Teljes szöveg: `SPEAKER_NOTES.md` (összesen 1515 szó, pontosan 720 mp, ~126 szó/perc).

---

## 8. Előadói beosztás és színpadi rend

| Előadó | Diák | Idő |
|---|---|---|
| Hallgató 1 | 1–3 | 1:30 |
| Hallgató 2 | 4–8 | 2:40 |
| Hallgató 4 | 9–11 | 2:00 |
| Hallgató 5 | 12–13 | 1:20 |
| Hallgató 3 | 14–17 | 2:00 |
| Hallgató 6 | 18–19 | 0:50 |
| Hallgató 4 | 20 | 0:30 |
| Hallgató 6 | 21–24 | 1:10 |
| **Összesen** | 24 dia | **12:00** + 3:00 vita |

Szabály: 15 percnél leállítanak. A diaszám formátuma `x/24`. A nyelv a diákon és a beszédben azonos (magyar).

---

## 9. A 3 perces vita: hogyan válaszoljunk?

1. Azonnal reagálunk: „Köszönöm a kérdést, a konzorcium nevében…”.
2. 20–30 mp-es válasz, benne **szám + WP/deliverable hivatkozás**.
3. Zárás: egy mondatos konklúzió.
4. Legfeljebb egy kiegészítés, 5 mp.
5. Sosem mondjuk, hogy „nem tudjuk”: a TRL 3 szórás → a WP3 D3.1 zárja le.

**Top 10 csapdakérdés (15 mp-es válaszok: `DEFENSE_QA.md` 2. fejezet):**

1. PLA feleannyi → miért PHA? (a PLA Tg-je 55–60 °C, a PHA HDT-ja > 95–105 °C, WP2)
2. Miért nincs logisztikai partner? (AGA 6.2.B/9.3: nem K+F, alvállalkozás WP1/WP3/WP5)
3. 12 hónapig nem avasodik? (5 rétegű koextrudált fólia, nanocellulóz/PGA mag, OTR < 0,05, WP3)
4. A nanocellulóz hidrofil? (szendvicsszerkezet: a 20 µm-es magot mindkét oldalról hidrofób PHA-réteg és tie védi)
5. TRL 7 egy 100%-os RIA-ban nem piaci bevezetés? (nem sorozatgyártás; a folyamatképesség statisztikai validálásához kell a 100 000 db, kutatási demonstráció)
6. Utólagos zsugorodás/beszorulás? (nukleálószer + bio-lágyító, 60–70 °C-os temperált szerszám, ±0,1 mm)
7. Nincs ipari komposztáló? (MOHU barna kuka → anaerob biogázüzem; a vékony PHA 30–45 nap alatt elbomlik)
8. PHA vs végtelenszer újrahasznosítható alumínium? (WUR 2023: komposztálható 741 vs. alumínium 779 g CO₂e/kg kávé; célunk ≥ 25%; a fő érv a végállapot: a használt kapszula ~25%-át gyűjtik vissza)
9. Ki fizeti meg az árat? (a kapszula ~2,5 g, így a felár ~1 eurócent/db; PPWR és EPR-díjak)
10. ISO 14855 csak mérési módszer? (igen; a megfelelőségi szabvány az NF T51-800 / OK Compost HOME, az ISO 14855 a kinetikai validálás WP4-ben)

**Költségvetési kérdések (`DEFENSE_QA.md` Topic F):** miért 520 PM, miért 4 000 €/PM, miért 20% indirekt, honnan vannak a számok.

---

## 10. Fájltérkép, build és ellenőrzés

| Fájl / Mappa | Mire való |
|---|---|
| `PHACK_Prezentacio_Vegleges.pptx` | **Főmappa:** A 24 dia a hivatalos BME PT sablonban, beágyazott előadói jegyzetekkel |
| `FELKESZULESI_UTMUTATO.md` | **Főmappa:** Ez a központi felkészülési dokumentum (nulláról tanulható összefoglaló) |
| `docs/SPEAKER_NOTES.md` | Diánkénti szó szerinti beszédszöveg (12:00 perc, 1515 szó), időzítés, színpadi átadás |
| `docs/DEFENSE_QA.md` | Vita: Top 10 csapdakérdés (15 mp-es válaszokkal), Topic A–F mélyebb érvek, WP-mátrix |
| `docs/FORRASOK.md` | Források és az állítások státusza (ellenőrzött irodalmi tény vs. konzorciumi célérték) |
| `docs/PROJECT_CONTEXT.md` | Pályázati adatlap: alapadatok, konzorcium, WP-k, KPI-k |
| `docs/DECISIONS.md` | Tervezési és mérnöki döntések naplója (ADR-01…06) |
| `docs/TODO.md` | Státusz és előadás előtti főpróba-ellenőrzőlista |
| `slides_rendered/slide_01..24.png` | A 24 dia 1280×960 PNG képe (gyors képi előnézet) |
| `scripts/generate_final_presentation.py`, `scripts/phack_figures.py`, `scripts/build_and_verify_notes.py` | A PPTX prezentáció, a mérnöki ábrák és az előadói jegyzetek generátora |
| `scripts/test_*.py` | Automatizált regressziós és konzisztencia-tesztek (4 tesztkészlet) |
| `etc/FHG HE sablon 2026.pptx`, `etc/FHG mintaprezentáció 2026.pdf`, `etc/info.txt`, `etc/lap1..4.jpg` | Kurzus-alapanyagok: hivatalos sablon, mintaprezentáció, oktatói követelmények, kéziratos GY02 lapok |

**Újragenerálás és ellenőrzés** (a `Projekt` főmappából):

```powershell
python scripts/generate_final_presentation.py
python scripts/test_challenger_stress.py
python scripts/test_speaker_notes.py
python scripts/test_defense_qa.py
python scripts/test_adversarial_critic.py
```

Szabály: ha szám változik, a diákon, a `build_and_verify_notes.py`/`SPEAKER_NOTES.md`-ben, a `DEFENSE_QA.md`-ben és a teszteken is át kell vezetni, majd a 4 tesztnek zöldnek kell lennie.

---

## 11. Felkészülési terv (nulláról a bemutatóig)

| Lépés | Mit | Mennyi |
|---|---|---|
| 1 | Elolvasni ezt a dokumentumot (1–6. fejezet) | 30 perc |
| 2 | Saját diák végigolvasása a `SPEAKER_NOTES.md`-ben, kulcsszámok bemagolása (2. fejezet) | 30 perc |
| 3 | Saját szakasz hangos elmondása stopperrel | 3× |
| 4 | Teljes főpróba az éles sorrendben és átadásokkal (8. fejezet) | 2× |
| 5 | A Top 10 csapdakérdés és a költségvetési kérdések begyakorlása párban | 30 perc |
| 6 | Technikai ellenőrzés: PPTX + PDF tartalék, 4:3 kép | 10 perc |

Cél: 12:00 ±15 mp; az utolsó főpróbán senki nem olvas a jegyzetből.

---

## 12. Amit előre jó tudni (őszinte határok)

- A 3–4000 €/PM a kurzus sablonjának irányadó értéke; a költségvetés ehhez van igazítva.
- A partnerszervezetek szerepei és a számok **tervezési, konzorciumi becslések**, nem kötelező érvényű ajánlatok. A diákon szereplő hozzávetőleges piaci számok forrásait és státuszát a `FORRASOK.md` tartalmazza.
- Ha a bizottság a partnerek (pl. Danimer / Bio-on) jelenlegi cégállapotáról kérdez, a válasz a `DEFENSE_QA.md` Topic F-ben van.
