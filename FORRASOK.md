# PHACK – Forrásjegyzék és az állítások ellenőrzöttsége

A kurzus sablonja, a mintaprezentáció és az `info.txt` nem kér forráslistát, a diákon ezért nincs hivatkozás (a diák száma 24 marad). Ez a dokumentum a vitához és a felkészüléshez készült: melyik állítás honnan ered, és mennyire biztos.

**Jelmagyarázat:** ✅ ellenőrzött forrással · ⚠️ részben igazolt, vagy a forrás eltér a diától · ❓ nem ellenőriztük, konzorciumi becslés / célérték.
Az ellenőrzés internetes keresésen alapult (2026), a másodlagos forrásokat (Wikipedia, aggregátorok) jelöljük.

---

## 1. Állítások és források

| # | Állítás a deckben | Státusz | Mit találtunk | Forrás |
|---|---|---|---|---|
| 1 | ~53 milliárd kapszula/év az EU-ban (6. dia) | ⚠️ becslés | A WUR „nyers becslése”: ~53 milliárd Nespresso-típusú kapszula/év az EU-ban (kb. 12 g nedves tömeg/db); a pontos piacméret ismeretlen. Független második forrás nincs. Hollandia: ~1,5–1,9 milliárd/év | Thoden van Velzen et al., WFBR Report 2450, 2023, https://edepot.wur.nl/641509; WUR longread 2025, https://www.wur.nl/en/longread/route-circular-coffee-capsules; DutchNews 2023, https://www.dutchnews.nl/2023/12/coffee-companies-aim-to-boost-aluminium-capsule-recycling-rate/ |
| 2 | Piacnövekedés ~7–8,5%/év | ✅ (másodlagos) | Straits Research: 7,07% CAGR (2026–2034); Sci. Rep. 2020: 8,5% CAGR (2017–2025, kapszula + pod együtt). A korábbi „60 milliárd db globálisan” nem igazolható (egy másodlagos adat: 8,2 milliárd db 2020-ban), ezért kikerült | https://straitsresearch.com/report/coffee-capsules-market; Sci. Rep., doi 10.1038/s41598-020-74138-1 |
| 3 | PPWR és a kapszulák (6. dia) | ✅ javítva | A PPWR 2026. aug. 12-től alkalmazandó. A merev, nem fém kapszulánál a komposztálhatóság **tagállami lehetőség** (9. cikk (2) a)), ahol van biohulladék-gyűjtés; a puha/áteresztő egységekre kötelező. A diák ezt már így mondják | Regulation (EU) 2025/40 (PPWR), Arts. 3(1)(f),(g), 9, 71, https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202500040 |
| 4 | EN 13432: 90% lebomlás 6 hónap alatt | ✅ | Megerősítve (másodlagos forrás) | Wikipedia, *Biodegradable plastic*, https://en.wikipedia.org/wiki/Biodegradable_plastic |
| 5 | EN 13432: 58 °C, 12 hét dezintegráció, 6 hó / 90%; NF T51-800: 20–30 °C, 12 hó / 90% | ⚠️ másodlagos | Biomera (gyártói oldal) és European Bioplastics ismertetője egyezik a diákkal; a szabványszöveget nem nyitottuk meg. A 20–25 °C helyett a forrás 20–30 °C-ot ad | https://biomera.eu/home-compostable-vs-industrial-compostable/; European Bioplastics; szabványok: CEN, AFNOR |
| 6 | Összes migrációs határérték 10 mg/dm² (Reg. 10/2011) | ✅ | 12. cikk (1) | Commission Regulation (EU) No 10/2011, https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02011R0010-20200923 |
| 7 | PLA Tg ≈ 55–60 °C | ⚠️ | A Wikipedia 60–65 °C-ot ad; biztonságosabb: „kb. 55–65 °C” | Wikipedia, *Polylactic acid*, https://en.wikipedia.org/wiki/Polylactic_acid |
| 8 | PHBH Tm, HDT > 95–105 °C | ⚠️ részben | Kaneka PHBH merev típus: Tg 2 °C, Tm 142 °C, **HDT 100 °C** (0,46 MPa); félmerev: Tm 136 °C, HDT 87 °C. A „HDT > 95–105 °C” a merev típusra igaz, a nukleált kompound célérték (WP2) | https://www.lookpolymers.com/polymer_Kaneka-PHBH-Rigid-Bio-based-Polymer.php (Kaneka-adat, viszonteladó oldala) |
| 9 | A nukleálószerek (orotinsav) gyorsítják a PHA-kristályosodást | ⚠️ | Összefoglalók alapján: PHBV orotinsavval nukleálva (*Polymers* 18(3):340, 2026); PHBHHx kristályosodás optimalizálása (*Sci Rep* 2023) – teljes szöveget nem olvastunk | DOI 10.3390/polym18030340; DOI 10.1038/s41598-023-27595-3 |
| 10 | LCA / CO₂e (6. és 7. dia, KPI 3) | ✅ javítva | A korábbi 120–150 / 50–60 / 35–45 / 15–25 kg CO₂e / 1000 db és „>70%” **nem igazolható, törölve**. Ellenőrzött: primer Al globálisan **15,1 kg CO₂e/kg** (IAI, 2022), Európa 6,6 (2023); ~1 g kapszula → ~16 kg/1000 db (saját számítás). WUR Table 15: komposztálható (komposztálva) **741**, alumínium (40% újrahasznosított, külön gyűjtve) **779 g CO₂e / kg kávé**, kávé nélkül; a kávé ~6× nagyobb hatású. A KPI 3 ezért **célérték: ≥ 25%** csökkentés (WP4). A WUR-t komposztálható alapanyag-gyártók finanszírozták | IAI, https://international-aluminium.org/ (2024); European Aluminium, https://european-aluminium.eu/projets/a-low-carbon-footprint/ (2025); WUR 2023, https://edepot.wur.nl/641509 |
| 11 | HE indirekt költség: 25% átalány | ✅ | A közvetlen költség 25%-a, az alvállalkozói költség nélkül | HE Work Programme 2023–2024, General Annexes, https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/wp-call/2023-2024/wp-13-general-annexes_horizon-2023-2024_en.pdf |
| 12 | TRL 3 / 6 / 7 definíciók | ✅ | TRL 3: kísérleti elvigazolás; TRL 6: releváns (ipari) környezetben demonstrált; TRL 7: rendszerprototípus üzemi környezetben | Ugyanaz a General Annexes dokumentum |
| 13 | Danimer és Bio-on partnerek | ⚠️ **kockázat** | Bio-on S.p.A.: csődbe nyilvánítva 2019. dec. 20. (Bolognai Bíróság, 137/19). Danimer Scientific: Chapter 11 2025 márciusában, a Teknor Apex vásárolta meg 2025 júniusában (másodlagos forrás) | Bioplastics News, „Bio-on Declared Bankrupt”, 2020, https://bioplasticsnews.com/bio-on-bankruptcy/; Wikipedia, *Danimer Scientific* (Plastics News, 2025) |
| 14 | PHA ára 5–6 €/kg (9. csapdakérdés) | ⚠️ | IMARC: ~3,2 USD/kg (Franciaország, 2026 Q2: 3 166 USD/t); EUR/kg forrás nincs. Az 5–6 €/kg a konzorcium becslése (speciális PHBH-típusok drágábbak) | https://www.imarcgroup.com/polyhydroxyalkanoates-pricing-report |
| 15 | UCO (használt sütőolaj) mint PHA-alapanyag | ✅ | Szakirodalmi áttekintés („waste cooking oil”) | Int. J. Biol. Macromol., DOI 10.1016/j.ijbiomac.2025.146592; *3 Biotech*, DOI 10.1007/s13205-025-04594-x |
| 16 | CEN/TC 249 (műanyagok), TC 261 (csomagolás), TC 411 (bioalapú) | ⚠️ | A bizottságok léteznek (katalóguscímekből); a TC 249 WG 9 a lebomlás jellemzésével foglalkozik; TC 261 szerepe az EN 13432-ben nincs igazolva | https://standards.cencenelec.eu |
| 17 | Cikkek: *Polym. Degrad. Stab.*, *Packag. Technol. Sci.*, *ACS Sustain. Chem. Eng.* | ✅ | A folyóiratok léteznek (Crossref) | https://api.crossref.org/journals |
| 18 | Nespresso: 15–19 bar, 90–95 °C | ⚠️ | Nespresso-forrás nincs; Nespresso-kompatibilis gép adata: 19 bar, 93 ± 2 °C (szakirodalmi cikk). A „15” alsó határ nem igazolt, ezért szóban „max. ~19 bar, ~93 °C” | Quantification of Caffeoylquinic Acids in Coffee Brews by HPLC-DAD, https://europepmc.org/article/PMC/PMC4283437 (2014) |
| 19 | 1 PM = 3–4000 EUR; 168 óra | ✅ (sablon) | A kurzus sablonja, 8. dia | `etc\FHG HE sablon 2026.pptx` |
| 20 | A RIA-ban 100% a támogatási intenzitás; TRL 5–6 körüli cél | ✅ (kurzus) | A kurzus követelményei és a HE szabályok | `info.txt`, HE General Annexes |

---

## 2. Mi változott a diákon ezen források alapján

1. **PPWR (6. dia, 9. dia, jegyzet, Q&A):** már nem „kötelező”, hanem „a tagállamok előírhatják (9. cikk (2) a))”.
2. **LCA (6., 7., 10., 11., 17. dia, jegyzet, Q&A):** a 120–150 / 15–25 kg CO₂e/1000 db és a „>70%” törölve; helyette ellenőrzött IAI- és WUR-adat, a KPI 3 pedig **célérték: ≥ 25%** (WP4 igazolja). A 6. dia jobb ábrája a WUR Table 15 adatait mutatja.
3. **Kapszulák száma (6. dia):** „60 milliárd globálisan / 12 milliárd EU” helyett „~53 milliárd db/év az EU-ban (WUR-becslés)”; a visszagyűjtés ~25% (NL, WUR 2025). A „>10 milliárd db/év lerakóban/égetőben” alsó becslésként érvényes marad (2. és 3. dia).
4. **Növekedés (6. dia):** ~7–8,5%/év (Straits Research; Sci. Rep. 2020).
5. **Danimer / Bio-on:** a diákon a névvel szereplő partnerek változatlanok (csapatdöntés); a cégállapot-kockázatra a Q&A F.3 ad választ. Beadás előtt érdemes a partnert cserélni vagy általánosítani (pl. „európai PHA-gyártó”).

A beszédszöveg szószáma 1515 maradt.

## 2/b. Még nyitott

- PLA Tg: az irodalom 60–65 °C; a diákon „55–60 °C” szerepel (alsó tartomány), pontosítható „60–65 °C”-ra.
- Nespresso: a diákon „15–19 bar, 90–95 °C”; az egyetlen forrás 19 bar / 93 ± 2 °C.
- PHA ára: EUR/kg forrás nincs.

---

## 3. Hogyan hivatkozzunk szóban

- Ellenőrzött számra: „…a Horizon Europe általános mellékletei szerint…”, „…az (EU) 2025/40 rendelet 9. cikke szerint…”.
- Becslésre: „a konzorcium becslése”, „célérték”, „a WP4-ben igazoljuk”.
- Soha ne állítsunk mért tényként olyan számot, amely a ❓ vagy ⚠️ csoportban van.
