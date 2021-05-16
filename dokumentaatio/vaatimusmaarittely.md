# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on yksinkertainen graafinen laskin, jossa voi tehdä muistiinpanoja. Sovelluksen tarkoitus on voida suorittaa aritmeettisia laskutoimituksia, sekä tallentaa haluamiaan muistiinpanoja laskimen viereen.

## Sovelluksen toiminnallisuudet
* [x] Sovelluksessa on syötekenttä ja napit erinäisille laskennallisille toiminnoille.
  - [x] +, -, *, /
  - [x] Nollaus-painike
  - [x] +/- painike, joka muodostaa annetun syötteen vastaluvun. Esim syöte: 5 -> tulos -5
  - [x] %-nappi, joka muuttaa annetun syötteen prosenttimuotoon. Esim syöte: 85 -> tulos 0,85
* [x] Laskutoimituksia voi tehdä useamman peräkkäin, eli ketjussa, tuloksen pysyen ajantasaisena (ei nollaannu välissä)
* [x] Laskimen vieressä on muistilista, johon voi tallentaa haluamiaan muistiinpanoja.
* [x] Muistiinpanot voi halutessaan tyhjentää

## Jatkokehitysideoita tulevaisuuteen
- Kertomat, potenssit, neliöjuuret yms
- Yksittäisen muistiinpanon poisto


## Käyttöliittymä
Sovelluksessa on yksi näkymä. Kenttä, jossa näkyy laskutoimituksen tulos, renderöityy laskutoimituksia tehdessä. Myös muistiinpanot renderöityvät näkyviin välittömästi tallentamisen yhteydessä. 
