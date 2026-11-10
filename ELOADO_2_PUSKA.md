# PHACK – 2. Előadó Mesterkurzus és Felkészülési Útmutató
## Anyagtudomány és Gyártástechnológia (R&D Felelős) – Felkészülés a Teljes Nulláról

> **Kinek szól ez a dokumentum?**  
> Kizárólag **Neked (a 2. Előadónak)**. Ha most úgy érzed, hogy semmit nem tudsz a projektről, a műanyagokról vagy a kávékapszulákról, **ne ess pánikba!** Ebből a dokumentumból 45 perc alatt teljesen nulláról fel tudsz készülni úgy, hogy a bemutatón magabiztos mérnökként fogsz beszélni, és a tanárok nem tudnak majd zavarba hozni.

---

# 🧠 0. FEJEZET: Gyorstalpaló a nulláról (Hogy ÉRTSD is, amit mondasz!)

Ha megérted a projekt mögötti paraszti logikát, nem kell bemagolnod a szöveget, mert természetesen fog jönni.

### 1. Mi a valódi baj a kávékapszulákkal?
* Az Európai Unióban évente **több tízmilliárd (kb. 53 milliárd)** kapszulás kávé fogy el.
* A kapszulák két anyagból készülnek:
  1. **Alumínium:** Bauxitbányászatból állítják elő, irdatlanul nagy a szén-dioxid lábnyoma (~15 kg CO₂e / kg alumínium). Egyetlen 30 másodperces kávéfőzésért kidobunk egy energiaigényes fémcsészét.
  2. **Fosszilis műanyag (PP/PE):** Kőolajból van, nem bomlik le évszázadokig.
* **A legnagyobb csapda: a KÁVÉZACC.** A használt kapszula belsejében ott marad a nedves, olajos, szerves kávézacc. A szelektív hulladékválogató gépek nem tudják gazdaságosan kimosni belőle a zaccot, ezért **a kapszulák ~75%-át nem gyűjtik vissza**, hanem a kommunális szemétbe, a lerakóba vagy a hulladékégetőbe kerülnek.

### 2. Miért nem jó a boltokban kapható „bio” PLA kapszula?
A boltokban már lehet kapni kukoricakeményítőből erjesztett **PLA (politejsav)** kapszulákat. A tanárok biztosan megkérdezik: *„Ha már van PLA, mi a fenének fejlesztenek új kapszulát?”*  
A válasz egyszerű: a PLA-nak két hatalmas hibája van:
1. **Nem bírja a forró kávéfőzést:** A PLA üvegesedési hőmérséklete ($T_g$) mindössze **55–60 °C**. A kapszulás kávéfőzőben viszont **90–95 °C-os forró víz** és brutális, **15–19 bar nyomás** tombol. Amint a forró víz eléri a PLA kapszulát, az meglágyul, mint a rágógumi, eldeformálódik, a víz melléfolyik, és a megolvadt műanyag eldugítja a méregdrága kávéfőzőt!
2. **Nem bomlik le a kertben:** A PLA csak speciális **ipari komposztáló üzemben (58 °C felett)** bomlik le. Ha kidobod a kertedbe a komposztba vagy a természetbe, évtizedekig ott marad, és mikroműanyaggá töredezik szét.

### 3. Mi a mi megoldásunk? Mi az a PHA / PHBH?
* A **PHA (polihidroxialkanoát)** és annak rugalmas kopolimere, a **PHBH** egy természetes biopoliészter, amit **baktériumok állítanak elő**, amikor cukorral, melasszal vagy használt sütőolajjal (UCO) etetik őket. Ez a baktériumok természetes „zsírraktára”.
* **Miért ez a csodaanyag kávékapszulához?**
  1. **Hőálló:** A BME által módosított és nukleált PHA kompound hőalaktartása terhelés alatt **$\text{HDT} > 95–105\text{ }^\circ\text{C}$**, és **120 °C-ig teljesen alakstabil**! Nevetve kibírja a kávéfőző 95 °C-os forró vizét és a 19 baros nyomását deformáció nélkül.
  2. **Otthoni kerti komposztban is 100%-ban lebomlik:** Mivel baktériumok készítették, a kerti talajban és a vizekben élő mikrobák imádják enni (természetes depolimeráz enzimeikkel). Normál kerti hőmérsékleten (20–25 °C) **6–12 hónap alatt maradéktalanul szén-dioxiddá, vízzé és humusszá bomlik** (az NF T51-800 szabvány szerint). Zéró mikroműanyag!
  3. **A zaccal együtt komposztálható:** A kávézacc tele van nitrogénnel, káliummal és foszforral. Így a használt kapszulát nem kell kibelezni, zaccal együtt bedobod a kerti komposztba vagy a barna bio-kukába, és prémium kerti termőföld/biotrágya lesz belőle.

### 4. A legfontosabb rövidítések és szakkifejezések:
* **TRL (Technology Readiness Level):** Technológiai érettségi szint (1-től 9-ig).
  * *TRL 3:* Laboratóriumi elvigazolás (kis próbatestek, DSC mérés a BME laborban).
  * *TRL 6:* Ipari demonstráció valós környezetben (M36-nál 100 000 db kapszula legyártva a MOL és Alfa gépein).
  * *TRL 7:* Üzemi töltősori validáció (M44–M48 között a PackCoffee 400 db/perces gépsorán barista kávéfőzési tesztekkel).
* **PPWR (Packaging and Packaging Waste Regulation):** Az EU 2026. augusztusától élesedő új csomagolási rendelete, ami kifejezetten előírhatja a kávékapszulák komposztálhatóságát.
* **EPR díj (Extended Producer Responsibility):** Kiterjesztett gyártói felelősség (Magyarországon a MOHU díja). A környezetszennyező csomagolások díja az egekbe szökik, a lebomlóké kedvezőbb.
* **Termoformálás (Mélyhúzás):** A kapszulát nem fröccsöntjük (mert az vastag és lassú lenne), hanem egy vékony (0,40 mm-es) fóliát felmelegítünk, és szerszámban kapszula alakúra formálunk.
* **Koextrúzió:** Több polimerréteg egyidejű extrudálása egyetlen szalaggá. Mi egy 5 rétegű szendvicset gyártunk, aminek a közepén nanocellulóz/PGA bio-barrier gát védi a kávét az oxigéntől (hogy 12 hónapig ne avasodjon meg).
* **Nukleálószer (pl. orotinsav, talkum):** Olyan adalékanyag, ami kristályosodási magokat képez a műanyagban, így a PHA lassú kristályosodását felgyorsítja 10 másodperc alá (nem ragad bele a formába).

---

# ⏱️ 1. FEJEZET: A Te Szereped és Színpadi Koreográfiád

* **A te sorszámod:** **2. Előadó** (Anyagtudományi és Gyártástechnológiai Felelős)
* **A te diáid:** **5., 6., 7. és 8. dia** (4 dia a 24-ből)
* **A te beszédidőd:** **~1 perc 40 másodperc** (pontosan 215 szó, feszes, dinamikus, kényelmes mérnöki tempóban!)
* **Állásrend a színpadon:** A csapat félkörben áll a kivetítő mellett. Te állsz a 2. helyen (az 1. előadó mellett).

### 🟢 A belépésed (Hogyan veszed át a szót?):
1. Az **1. Előadó** befejezi a 4. diát, és ezt mondja:
   > *„...most pedig átadom a szót műszaki felelősünknek, [Te neved]-nek, aki bemutatja az anyagtudományi áttörést és a gyártási láncot.”*
2. **A te mozdulatod:**
   * Nyugodtan, magabiztosan átveszed a prezentert (lapozót).
   * Lépsz egy határozottat előre a pulpitushoz vagy a kivetítő elé.
   * Ránézel a bizottságra, megnyomod a gombot (átvált az **5. diára**), és határozottan megszólalsz:
   * **„Köszönöm a szót!”**

### 🔴 A kilépésed (Hogyan adod tovább a szót?):
1. A **8. dia legvégén** az utolsó mondatoddal rögtön felkonferálod a csapattársadat:
   > *„...A kifejlesztett technológia piaci hatásait és célcsoportjait innovációs felelősünk, [3. előadó neve] mutatja be.”*
2. **A te mozdulatod:**
   * Átnyújtod a prezentert a 3. előadónak.
   * Lépsz egyet hátra a csapat sorába, és nyugodtan, fegyelmezetten figyelsz tovább.

---

# 🎬 2. FEJEZET: Diánkénti Részletes Útmutató (5–8. dia)

Nézd meg a diák képeit vagy nyisd meg a PowerPointot, miközben ezt olvasod!

---

### 🔹 5/24. Dia: Technológiai Érettségi Szintek (TRL Ugrás: TRL 3 ➔ TRL 7)

```text
┌───────────────────────────────────────┬───────────────────────────────────────┐
│ BAL OLDAL: Kiindulási Szint (TRL 3)   │ JOBB OLDAL: Célállapot (TRL 6/7)      │
│ • BME Polimertechnika laboratórium    │ • MOL & Alfa ipari pilot: 100 000 db  │
│ • Kis próbatestek, DSC/reológia       │ • PackCoffee 400 db/perc töltősor     │
│ • Termoformálhatósági elvigazolás     │ • Barista teszt & EN 13432 audit      │
└───────────────────────────────────────┴───────────────────────────────────────┘
```

* **Időtartam:** 22 másodperc (50 szó)
* **A dia lényege 1 mondatban:** Nem a nulláról álmodozunk, hanem a BME laboratóriumi kísérleteiből kiindulva az ipari partnerekkel 100 000 darabos valós üzemi szintre visszük a technológiát.
* **Mire mutass kézzel / lézerrel?**  
  Először a **bal oldali TRL 3-as kártyára** mutass, majd amikor a 100 000 darabos pilotról beszélsz, lendületesen vidd át a kezed a **jobb oldali TRL 7-es blokkra**.

> **🎙️ A szó szerinti beszéded:**  
> „Köszönöm a szót! **TRL 3-as laboratóriumi szintről indulunk**, ahol a BME és a Danimer kísérletileg már igazolta a módosított PHA termoformálhatóságát. A négyéves program végére **TRL 7-es üzemi szintre** jutunk: a MOL és az Alfa Industry gépsorain **100 000 darabos ipari pilot szériát** gyártunk, amit valós automata töltősoron és barista tesztekkel validálunk.”

---

### 🔹 6/24. Dia: A Piaci Probléma és Hulladékstatisztikák (EU PPWR & SUP)

```text
┌───────────────────────────────────────┬───────────────────────────────────────┐
│ BAL OLDAL: Hulladékprobléma           │ JOBB OLDAL: EU Szabályozási Kényszer  │
│ • 53 milliárd kapszula/év az EU-ban   │ • EU PPWR Rendelet (2026. augusztus)  │
│ • Csak ~25%-ot gyűjtenek vissza       │ • SUP Irányelv (műanyag kivezetés)    │
│ • Nedves zacc miatt lerakóba kerül    │ • MOHU növekvő EPR díjak              │
└───────────────────────────────────────┴───────────────────────────────────────┘
```

* **Időtartam:** 24 másodperc (52 szó)
* **A dia lényege 1 mondatban:** Az évi több tízmilliárd elpazarolt kapszula és az új, szigorú EU-s csomagolási törvények (PPWR) miatt a piacnak kötelező zöldre váltania, és a mi kapszulánk pontosan erre ad választ.
* **Mire mutass kézzel / lézerrel?**  
  A bal oldali nagy számokra (**53 milliárd** és **75% hulladék**), majd a jobb oldali **PPWR rendelet kék dobozára**.

> **🎙️ A szó szerinti beszéded:**  
> „Az Európai Unióban évente **53 milliárd kávékapszula** fogy, és mintegy **háromnegyedük lerakóba vagy égetőbe kerül** a benne maradó olajos zacc miatt. Ezzel párhuzamosan az új **EU PPWR rendelet** előírhatja a kapszulák kötelező komposztálhatóságát, a SUP direktíva pedig kivezeti a fosszilis műanyagokat. A PHACK pontosan erre a jogi kényszerre ad azonnali ipari megoldást.”

---

### 🔹 7/24. Dia: Miért a PHA a Jövő Anyaga? (PHA vs. PLA – A LEGFONTOSABB DIA!)

```text
┌──────────────────────────┬──────────────────────────┬──────────────────────────┐
│ Tulajdonság              │ PLA (Politejsav)         │ PHACK – Módosított PHA   │
├──────────────────────────┼──────────────────────────┼──────────────────────────┤
│ Hőállóság kávéfőzéskor   │ 55–60 °C (Megolvad!)     │ >95–105 °C (120 °C-ig!)  │
│ Lebomlás módja           │ CSAK ipari üzemben       │ Házi kerti talajban is!  │
│ Kávézacc sorsa           │ Nehezen választható szét │ Zaccal együtt komposzt   │
│ Környezeti végállapot    │ Mikroműanyagot képez     │ Víz, CO2, biomassza      │
└──────────────────────────┴──────────────────────────┴──────────────────────────┘
```

* **Időtartam:** 26 másodperc (58 szó)
* **A dia lényege 1 mondatban:** A PLA nem bírja a forró kávét és nem bomlik a kertben, a mi PHA kompoundunk viszont 120 °C-ig alakstabil és otthoni komposztban is elenyészik.
* **Mire mutass kézzel / lézerrel?**  
  Ez az egész bemutató kulcsa! Mutass rá nyomatékosan a táblázatban a **PHA 120 °C-os sorára**, húzd alá kézzel a kontrasztot a **PLA 55 °C-jával**, majd mutass az alsó sorban a **házi komposztálhatóságra**.

> **🎙️ A szó szerinti beszéded:**  
> „Miért a PHA a megoldás? A mikrobiális PHA nemcsak ipari üzemben, hanem **házi komposztban és természetes vizekben is maradéktalanul elbomlik**, zéró mikroműanyaggal. Míg a piacon lévő **PLA 55 °C-on meglágyul** a forró kávéfőzéstől, addig a mi kompoundunk **120 °C-ig alakstabil**, a használt kapszula pedig zaccal együtt a kerti komposztban **6–12 hónap alatt humusszá válik**.”

---

### 🔹 8/24. Dia: Műszaki és Technológiai Módszertan (6 Lépéses Értéklánc)

```text
┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ 1. Bio-on    │➔ │ 2. BME/MOL   │➔ │ 3. MOL       │➔ │ 4. Alfa      │➔ │ 5. PackCoffee│➔ │ 6. RWTH      │
│ Fermentáció  │   │ Kompoundálás │   │ 5-r. Fólia   │   │ Termoformálás│   │ UH Hegesztés │   │ Lebomlás/LCA │
└──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘
```

* **Időtartam:** 25 másodperc (55 szó)
* **A dia lényege 1 mondatban:** A 6 európai partner egymásra épülő lépésekben viszi végig az anyagot: a baktériumos fermentációtól a fóliagyártáson és a kapszulaformázáson át a töltésig és az akkreditált lebomlási tesztekig.
* **Mire mutass kézzel / lézerrel?**  
  A mutatóddal vagy kezeddel balról jobbra folyamatosan pásztázd végig a 6 mérnöki dobozt és nyilat: 1. fermentáció $\rightarrow$ 2. kompoundálás $\rightarrow$ 3. fóliagyártás $\rightarrow$ 4. termoformálás $\rightarrow$ 5. hegesztés $\rightarrow$ 6. vizsgálatok.

> **🎙️ A szó szerinti beszéded:**  
> „A megvalósítás a teljes értékláncot lefedi: a használt étolajból történő baktériumos fermentációt **kétcsigás kompoundálás** követi a gyors kristályosodásért. Ebből **0,40 mm-es, 5-rétegű bio-barrier fóliát** koextrudálunk, amit temperált szerszámban mélyhúzunk. A töltés után **kíméletes ultrahangos zárást** alkalmazunk, végül akkreditált EN 13432-es lebomlási audit zárja a láncot. A piaci hatásokat és célcsoportokat **[3. előadó neve]** mutatja be.”

---

# 🔢 3. FEJEZET: Kulcsszámok puskája (Ezeket éjszaka felkeltve is tudd!)

A bizottság imádja a konkrét számokat. Ha belekérdeznek, ne általánosságokat mondj, hanem ezeket a számokat:

| Mit kérdezhetnek? | A pontos szám | Miért fontos? |
|---|---|---|
| Milyen meleg a kávéfőző víz? | **90–95 °C** | Ezt kell kibírnia az anyagnak. |
| Mekkora a nyomás a gépben? | **15–19 bar** | Hatalmas extrakciós mechanikai nyomás. |
| Mi a PLA gyenge pontja? | **$T_g \approx 55–60\text{ }^\circ\text{C}$** | Az üvegesedési hőmérsékletnél meglágyul, szétfolyik. |
| Mit bír a mi PHA-nk? | **$\text{HDT} > 95–105\text{ }^\circ\text{C}$ (120 °C-ig stabil)** | Hőalaktartás terhelés alatt; nem deformálódik! |
| Milyen vastag a kapszula fala? | **0,40 mm (380–400 µm)** | 5 rétegű koextrudált síkfólia nanocellulóz maggal. |
| Milyen meleg a formázószerszám? | **60–70 °C-ra temperált** | A gyors kristályosodásért (<3,5 mp ciklusidő). |
| Mennyi idő alatt bomlik le a kertben? | **6–12 hónap (NF T51-800)** | Házi komposztban (20–25 °C), humusszá válik. |
| Hány darabot gyártunk le pilotban? | **100 000 db (M36-ra)** | TRL 6 ipari pilot, 400 db/perc automata töltősoron. |

---

# 🛡️ 4. FEJEZET: A 3 Perces Vitablokk (Q&A) – A te csapdakérdéseid

Az előadás után 3 perc kérdezz-felelek lesz. Ha a tanárok a műanyagokról vagy a technológiáról kérdeznek, **nem nézel körbe bizonytalanul: azonnal teszel egy határozott lépést előre, és te válaszolsz!**

#### 🎯 1. Kérdés: *„A PLA feleannyiba kerül, mint a PHA. Miért nem abból csinálják a kapszulát?”*
* **Miért kérdezi a tanár?** Mert a piacon a PLA a legismertebb bioműanyag, és látni akarja, tisztában vagy-e az anyagtudományi korlátaival.
* **A te 15 másodperces válaszod:**
  > *„Köszönöm a kérdést! A PLA üvegesedési hőmérséklete mindössze 55–60 °C. A kávéfőző 90–95 °C-os forró vizében és 19 baros nyomásán a PLA azonnal meglágyul, a pereme kifordul, a kapszula deformálódik és szivárog. Emellett a PLA kerti talajban egyáltalán nem bomlik le, kizárólag 58 °C feletti ipari komposztálóban. A mi nukleált PHA kompoundunk hőalaktartása meghaladja a 95–105 °C-ot, így a forrázás alatt tökéletesen alakstabil marad, utána pedig a házi kerti komposztban is maradéktalanul elbomlik a WP2 fejlesztése szerint.”*

#### 🎯 2. Kérdés: *„A PHA köztudottan lassan kristályosodik és utólag zsugorodik. Nem fog beszorulni a Nespresso gépbe a kapszula?”*
* **Miért kérdezi a tanár?** Mert a polimertechnika oktatók tudják, hogy a nyers PHA lassan hűl le és deformálódhat.
* **A te 15 másodperces válaszod:**
  > *„Pontosan ez volt a WP2 legfőbb mérnöki kihívása. A BME receptúrájában bio-nukleálószereket – például orotinsavat és mikronizált talkumot – alkalmazunk, amivel a kristályosodási félidőt 10 másodperc alá szorítjuk le. Ráadásul az Alfa Industry 60–70 °C-ra temperált szerszámban végzi a termoformálást, így a kapszula már a formában eléri a 90%-os kristályossági fokot, garantálva a szigorú ±0,1 mm-es mérettűrést.”*

#### 🎯 3. Kérdés: *„Miért termoformálják a kapszulát, miért nem egyszerűen fröccsöntik?”*
* **Miért kérdezi a tanár?** Mert a műanyagiparban a legtöbb poharat és kupakot fröccsöntik.
* **A te 15 másodperces válaszod:**
  > *„Fröccsöntéssel a minimális falvastagság 0,8–1,2 mm lenne, ami legalább 60%-kal megnövelné az alapanyagköltséget, ráadásul a lassabb kristályosodás miatt gazdaságtalanul hosszú lenne a ciklusidő. A termoformálás lehetővé teszi a mindössze 0,40 mm vékony falvastagságot, a kis kapszulatömeget (kb. 2,5 g) és a gyors, nagysebességű ipari szériagyártást a MOL és Alfa sorain.”*

---

# 🚀 5. FEJEZET: 45 Perces Edzésterv Ma Estére (Hogyan készülj fel?)

Nem kell órákat tanulnod! Csináld pontosan ezt a 45 perces blokkot:

1. **0–15. perc: Olvasd át még egyszer a 0. fejezetet (Gyorstalpaló).**  
   Értsd meg a sztorit: *Alumínium rossz (CO2), PLA rossz (megolvad a forró vízben), PHA a király (bírja a 95 fokot és lebomlik a kertben a zaccal együtt).*
2. **15–30. perc: Nyisd meg a PowerPointot az 5., 6., 7., 8. diánál.**  
   Olvasd fel a 2. fejezetben lévő szöveget hangosan, miközben a megfelelő ábrákra mutatsz a képernyőn. Csináld meg egymás után **háromszor**.
3. **30–40. perc: Stopperes éles próba.**  
   Indíts el egy stoppert a telefonodon! Mondd el a 4 diát a belépéstől (*„Köszönöm a szót!”*) az átadásig (*„...[3. előadó neve] mutatja be.”*).  
   *Cél:* **1 perc 35 mp és 1 perc 45 mp között** kell lenned. Ha túl gyors vagy, tarts hatásszünetet a számok után. Ha túl lassú, ne állj meg gondolkodni.
4. **40–45. perc: Kérdés-felelet próba.**  
   Olvasd el a 4. fejezet 2 legfőbb kérdését és válaszát hangosan. Ha van szobatársad vagy csapattársad, kérd meg, hogy tegye fel neked a kérdést!

Ha ezt végigcsinálod, **készen állsz az 5-ösre**, magabiztos leszel, és te leszel a csapat legfelkészültebb műszaki előadója!
