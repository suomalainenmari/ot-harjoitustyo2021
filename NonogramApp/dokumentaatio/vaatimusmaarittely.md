# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksessa on tarkoitus voida pelata Nonogram-peliä. Sovelluksessa on vaan yhdenlaisia käyttäjiä.

## Suunnitellut perusversion toiminnallisuudet
* Pelialustana toimii 10x10 ruudukko
* Pelaaja pystyy joko merkitä ruutuun täyttösymbolin  tai merkitä siihen rastin
	* Käyttöliittymässä nappi, jota painamalla pelaaja voi vaihtaa täyttösymbolin ja rastin välillä
* Jos pelaaja yrittää laittaa väärän merkin ruutuun, ei ruutua täytetä
* Kun pelaaja on täyttänyt kaikki täyttösymbolilla täytettävät ruudut, on peli läpäisty
	* Pelin läpäisystä ilmoitetaan pelaajalle

## Jatkokehitysideoita olevan ajan puitteissa
* Pelaajalla on alkutilanteessa 3 elämää
	* Mikäli pelaaja yrittää  laittaa ruutuun väärän symbolin, hän menettää elämän ja ruutuun täytetään oikea symboli
* Kun pelaajan elämät loppuvat, on peli aloitettava alusta
* Ajastin, joka mittaa peliin käytettyä aikaa
* Painike, josta pelin saa aloitettua alusta

## Käyttöliittymäluonnos
![Käyttöliittymäluonnos](/kuvat/kayttoliittymaluonnos.jpg)
Sovelluksessa on yksi näkymä. Ruudukkoon lisätään täytetyt symbolit. Symbolin vaihto tapahtuu nappia painamalla.
