# spelling-bee
Beat the NYTimes Spelling Bee puzzle https://www.nytimes.com/puzzles/spelling-bee

Finds all solutions and (optionally) submits them to NYTimes on your behalf.

## Setup
Install Python 3.x and the `requests` library. If usinig `pipenv`:
```
pipenv install requests
pipenv shell
```
You will also need a dictionary of possible words to search. If submitting automatically, use the largest word list
* 480k word list: https://github.com/dwyl/english-words/blob/master/words.txt
* 58k word list: http://www.mieliestronk.com/corncob_lowercase.txt

## Usage
### Solve without Submitting
To show matching words without submitting. This example would solve a puzzle with the center letter `I` and `COILRTV` as the complete set of allowed letters.
```
python spelling-bee.py --word_file ~/Downloads/words.txt --center_letter i --letters coilrtv 
```
Output:
  ```
  Found: adamantinoma, adamantoid, adamantoma, adamo, adao, adatom, addio, addition, addoom, adiation, adion, aditio, admonition, adnation, adnomination, adod, adon, adona, adonai, adonia, adoniad, adonian, adonidin, adonin, aimo, ainoi, aiod, aion, aition, amado, amando, amatito, amato, amidation, amido, amidon, amination, amino, aminoid, ammino, ammo, ammon, ammonation, ammonia, ammoniation, ammonion, ammonitoid, ammono, ammonoid, amnion, amnionata, amnionia, amniota, amniotin, amon, amotion, anammonid, anamnionata, anamniota, anatto, andantino, ando, animando, animation, animato, animo, anion, annatto, anno, annomination, annona, annot, annotation, annotto, anoa, anodon, anodonta, anodontia, anoia, anoint, anomia, anomodont, anomodontia, anon, anonad, anotia, anotta, anotto, antdom, antiatom, antido, antimonid, antinion, antinomian, antiodont, antntonioni, anton, antoni, antonia, antonin, antonina, antoniniani, antonino, antonio, antonito, aonian, atimon, ation, atmo, atom, aton, atonia, dado, daimio, daimon, daimonion, damiano, damnation, damnonii, damon, danio, dannon, dantomania, danton, datamation, dation, dato, datto, diamantoid, diamido, diamond, dianoia, diao, diatom, diatoma, diatomin, dido, didonia, diiodid, diiodo, dimidiation, dimond, dindon, dinmont, dino, dino, diodia, diodon, diodont, dion, dioon, diota, dioti, ditation, dition, ditto, ditton, dmod, doand, doanna, doat, dodd, dodi, dodman, dodo, dodoma, dodona, dodonian, doina, doit, domain, domina, dominant, domination, domini, dominion, domino, domitian, domn, domoid, dona, donaana, donat, donata, donati, donatio, donation, donato, dondi, dondia, doni, donia, donn, donna, donni, donnot, dont, doodad, doodia, doom, doon, dotant, dotation, doti, doto, dott, dotti, iddio, iddo, idiom, idion, idiot, idmon, idona, idonna, imido, imino, imitation, immanation, inanimation, inanition, indio, indoin, iniomi, inion, initiation, initio, inition, innominata, inoma, intimado, intimation, intimidation, into, intonation, ioannina, iodama, iodation, iodid, iodin, iodination, iodo, iona, ioni, ionia, ionian, iota, ition, itmo, itonama, itonaman, itonia, itonidid, mado, madonia, madonna, madtom, maimon, maioid, mammodi, mammon, mammondom, mammoni, mamo, mamona, manado, manation, manatoid, mandation, mandom, manito, manno, mano, manomin, manon, manto, mantoid, manton, maomao, mattoid, mattoon, miao, midnoon, mimmation, mimmood, minamoto, mindanao, minination, minion, mino, minoa, minoan, minot, minto, minton, mnioid, moan, moat, modi, modiation, modo, moia, moid, moina, moio, moit, momi, momma, mommi, momo, mona, monad, monadina, mond, monda, mondain, mondamin, mondo, monia, monimia, monition, monnion, mono, monoamid, monoamin, monoamino, monodon, monodont, monodonta, monoid, monomania, monon, monona, mononomian, monont, monotint, mont, montana, montanan, montanin, montano, montant, montanto, monti, montia, monto, monton, mood, moon, moonman, moot, mootman, mota, motion, motitation, motmot, moton, mott, motto, naio, namatio, nammo, nanaimo, nanoid, nanon, naoi, naoma, naomi, naoto, natation, nation, nato, natoma, nidation, nidiot, nino, ninon, nintoo, niota, nito, niton, noaa, noam, noami, noao, noddi, nodi, noint, noma, nomad, nomadian, noman, nomi, nomina, nomination, nomoi, nona, nonaid, nonamino, nonamotion, nonanimation, nonda, nondamnation, nondo, nondominant, nondomination, nondonation, noni, nonimitation, nonintimidation, nonion, nonman, nonmotion, nonna, nonnant, nonnat, nonnomad, nonnomination, nono, nonomad, nontan, nontannin, noon, noonan, nota, notan, notation, noti, notidani, notidanian, notidanid, notidanidan, notidanoid, notion, notitia, notition, notodontian, notodontid, notodontoid, notommatid, oatman, oddd, oddman, odin, odinian, odom, odon, odonata, odont, odontia, odontoid, odontoma, odoom, oidia, oidioid, oina, oinomania, oint, oita, oman, omani, omao, omina, omit, ommatidia, ommatitidia, ommiad, omni, omniana, omoo, onamia, onan, ondo, onia, onida, oniomania, onion, onomantia, onomatomania, ontina, onto, ooid, oomantia, oona, oont, oooo, ootid, otiant, otidia, otina, otionia, otomi, otomian, ototoi, otti, otto, ottoman, ottonian, tadio, taino, tannoid, tano, tanoa, tanoan, tanto, taotai, tatoo, tattoo, tiao, timo, timon, timonian, tino, tion, tiona, tionontati, titano, tito, toad, toano, toat, toatoa, toda, todd, todt, toit, toitoi, toma, toman, tomand, tomato, tomi, tomia, tomin, tommi, tomomania, tomtit, tonada, tonant, tonation, tondi, tondino, tondo, toni, tonia, tonina, tonn, tonna, tonto, toom, toomin, toon, toona, toot, tootmoot, toto
  ```
### Auto-submit Solution
To automatically submit your answers, include the `--puzzle_id` and `--nyt_s` options. You can find the values for these by submitting a word on the NYTimes site and inspecting the request: `--puzzle_id` is `puzzleID` in the request body, and `--nyt_s` is the value from the `--nyt_s` header.
```
python spelling-bee.py --word_file ~/Downloads/words.txt --center_letter i --letters coilrtv --puzzle_id 12065 --nyt_s <value>
```
