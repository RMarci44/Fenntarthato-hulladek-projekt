# Döntési Napló (Project Decision Records - ADR)

Ez a dokumentum rögzíti a PHACK projekt során meghozott legfontosabb anyagtudományi, technológiai és konzorciumi döntéseket, valamint az elvetett alternatívákat és azok szakmai indoklását.

---

## ADR-01: Alapanyag kiválasztása – Miért PHA és miért nem PLA vagy Alumínium?

- **Döntés:** A kapszula teste és zárófóliája baktériumok által szintetizált **Polihidroxialkanoátból (PHA)** készül.
- **Elvetett alternatívák:**
  - *Fosszilis polimerek (PP, PS):* Nem fenntarthatóak, az olajos kávézacc szennyeződése miatt gazdaságosan és mechanikailag nem újrahasznosíthatóak szelektív gyűjtésből.
  - *Primer Alumínium:* Bár jól zár, előállítása rendkívül energiaigényes (Bauxit bányászat, Bayer-eljárás, Hall–Héroult elektrolízis). A zaccot a fogyasztók 90%-a nem kaparja ki a kapszulából, így lerakóba vagy égetőbe kerül.
  - *Politejsav (PLA):* Bár elterjedt bio-alapú műanyag, **két kritikus hibája van kávékapszulánál:**
    1. **Hőállóság:** Üvegesedési átmenete ($T_g$) alacsony (~55–60°C). A forró kávéfőző víz (90–95°C) és a nyomás (15–19 bar) alatt a kapszula deformálódik, megolvad, és elrontja a gépet.
    2. **Biológiai lebomlás:** A PLA **csak ipari komposztáló üzemben** (58°C felett, magas páratartalom mellett) bomlik le. Házi kerti komposztban vagy a természetbe jutva évtizedekig megmarad.
- **A PHA igazolása:**
  - Hőállósága módosítással akár 120°C-ig stabil.
  - **Valódi otthoni komposztálhatóság:** Szobahőmérsékleten (20–25°C), kerti talajban és természetes vizekben is lebomlik 6–12 hónap alatt.
  - Zárt szerves körforgás: a kávézaccal együtt komposztálható, a bomlás végterméke tápanyag a talajnak.

---

## ADR-02: Gyártási technológia – Miért Termoformálás és miért nem Fröccsöntés?

- **Döntés:** Kétcsigás kompoundálás után **síkfólia extrúzió (0,35–0,45 mm)**, majd **nagysebességű vákuumos/túlnyomásos termoformálás**.
- **Elvetett alternatíva (Fröccsöntés):**
  - A fröccsöntött kapszulák falvastagsága jóval nagyobb (>0,8–1,2 mm), ami feleslegesen növeli a drága bio-alapanyag felhasználását és lassítja a biodegradációt.
  - A PHA kristályosodási kinetikája viszonylag lassú, a fröccsöntési ciklusidő túl hosszú lenne a gazdaságos ipari tömeggyártáshoz.
- **A Termoformálás indoklása:**
  - Vékony falvastagság (0,38–0,40 mm) érhető el kiváló méretstabilitással (±0,1 mm kamratűrés) **temperált (60–70°C) szerszámban**, amelyben az orotinsavval/talkummal nukleált PHA gyorsan (<3,5 mp ciklusidő) átkristályosodik utózsugorodás nélkül.
  - Az 5-rétegű síkfólia koextrúziójával könnyen integrálható a bio-barrier záróréteg (aroma- és gázzárás: OTR < 0,05 cm³/(kapszula·nap·bar), WVTR < 1,0–2,0 g/(m²·nap)).
  - Meglévő ipari csomagológépeken (pl. ALFA Industry gépparkja és PackCoffee 400 db/perc töltősora) azonnal adaptálható.

---

## ADR-03: Konzorciumi Partnerek és a Logisztikai Cég Kizárása

- **Döntés:** 6 fős, 4 európai országot felölelő konzorcium kialakítása, lefedve a teljes K+F+I értékláncot:
  1. Nyersanyag-előállítás: Danimer Scientific / Bio-on European Facility (IT, Ipari partner)
  2. Receptúra & Kutatás: BME (HU, Koordinátor, Kutatóhely)
  3. Extrúziós méretnövelés: MOL Csoport (HU, Ipari partner)
  4. Formázás & Szerszámozás: Alfa Industry (HU, KKV)
  5. Vizsgálat, Szabványosítás & LCA: RWTH Aachen (DE, Kutatóhely)
  6. Töltés, Minőségbiztosítás: PackCoffee Europe Barista Alliance (AT, Ipari partner)
- **Megfontolás & Elvetett ötlet:**
  - Felmerült logisztikai / disztribúciós partner bevonása a konzorciumba.
  - **Oktatói szabályzat alapján elvetve:** A logisztikai cég nem végez érdemi technológiai fejlesztést, a Horizon Europe bírálók a pontszámot csökkentik felesleges partnerek miatt. A logisztikai feladatok kizárólag alvállalkozói díjként számolhatók el.

---

## ADR-04: TRL Ugrás – Miért TRL 3-ról TRL 6/7-re (és miért nem TRL 8–9)?

- **Döntés:** A projekt a laboratóriumi működési elv igazolásától (**TRL 3**) az ipari pilot demonstráción (**TRL 6**, M36) át a valós üzemi töltősori környezetben történő rendszerprototípus-demonstrációig (**TRL 7**, M48) tart.
- **Indoklás:**
  - Ez egy Horizon Europe **Research and Innovation Action (RIA)** típusú pályázat, amely az ipari kutatásra és kísérleti fejlesztésre fókuszál.
  - A 100 000 db-os demonstrációs tétel (WP3, T3.3) nem kereskedelmi értékesítés, hanem a 400 db/perc sebességű ipari töltő- és ultrahangos hegesztősor folyamatképesség-ellenőrzése ($C_{pk} > 1,33$) és az akkreditált EN 13432 / NF T51-800 biodegradációs tesztek mintaszükséglete.
  - Nem TRL 8–9 (teljes piaci kereskedelmi bevezetés és tömeggyártási tanúsítás), mert a 48 hónap alatt az új bio-kompound élelmiszeripari validációja és a 100 000 db-os üzemi demonstráció a reális és szakmailag megalapozott RIA cél.
  - **Időzítés (a diákkal egyező):** a 100 000 db legyártása és a 400 db/perc próbatöltés M36-ra készül el (WP3, MS3, D3.2 = TRL 6); a TRL 7 az M44–M48 közötti üzemi validáció (barista teszt, Cpk, akkreditált EN 13432 / NF T51-800 igazolás, D4.1).

---

## ADR-05: Költségvetés és emberhónap – miért 520 PM és 4 000 €/PM

- **Kiinduló probléma:** A kurzus sablonja (FHG HE sablon, 3.1a dia) szerint 1 személyhónap (PM) átlagosan 168 óra, összköltsége 3–4000 EUR, és a személyi költségnek összhangban kell lennie a PM-ekkel. Az első változatban 2,15 M€ / 260 PM ≈ 8 270 €/PM volt, ami a bírálók szerint túlárazott.
- **Döntés:** Az összköltség marad 4,2 M€ (100% EU támogatás), a PM-ek megduplázódtak (260 → 520), a személyi költség 520 PM × 4 000 € = 2 080 000 €. A költségkategóriák a sablon (Personnel / Travel and subsistence / Equipment / Other goods, works and services) szerintiek, külön indirekt sorral:
  - Személyi 2 080 000 € (50%) | Utazás és ellátás 130 000 € (3%) | Felszerelés 670 000 € (16%) | Egyéb áru, munka, szolgáltatás 480 000 € (11%) | Indirekt 25% átalány 840 000 € (20%) = 4 200 000 €.
  - Az indirekt költség a közvetlen költség 25%-a: 840 000 / 3 360 000 = 25%.
- **Partnerek:** BME 144 PM / 1,05 M€; MOL 100 / 850 k€; ALFA 90 / 650 k€; RWTH 96 / 750 k€; BIO 50 / 550 k€; PCOFF 40 / 350 k€. WP-összegek: WP1 68, WP2 144, WP3 136, WP4 96, WP5 76 = 520 PM. Hazai (HU) részarány: 2,55 M€ (60,7%), 334 PM.
- **Következmény:** minden PM-szám a diákon, a jegyzetekben, a Q&A-ban és a teszteken ennek megfelelően frissült; a beszédszöveg szószáma változatlan (1515 szó).

---

## ADR-06: Vizuális megoldások – saját ábramodul, logó és a minta szerinti címlap

- **Döntés:** Az összes ábra a `phack_figures.py` modulban készül (matplotlib, pontos pt-méretben, a dia helyére illesztve, nincs utólagos átméretezés). A címlap a mintaprezentáció szerint központosított (tag-sor, PHACK, alcím, felhívás, középen emblémalogó, alul tárgy és csoport); a logó (`make_fig_logo`) a 2. dián világos hátterű változatban is megjelenik.
- **Indoklás:** a minta címlapja csak cím + logó + tárgy; az egyedi, pontos méretű ábrák elkerülik a torzulást és a szövegtúlcsordulást, és a `test_challenger_stress.py` ellenőrzi, hogy a kulcsdiákon kép van.
