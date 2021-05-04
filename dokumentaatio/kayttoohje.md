# Käyttöohje

Projektin viimeisimmän releasin voi ladata [täältä](https://github.com/suomalainenmari/ot-harjoitustyo2021/releases). Lähdekoodi löytyy Assets-osion alta Source code nimisenä zip-pakettina.

## Ohjelman käynnistäminen

Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla:
```
poetry install
```

Tämän jälkeen ohjelman alustustoimet tulee suorittaa komennolla:
```
poetry run invoke build
```

Ohjelman voi nyt käynnistää komennolla:
```poetry run invoke start
```

## Aloitusnäkymä

Sovellus käynnistyy näkymässä, jossa vasemmalla puolella löytyy perinteinen laskin, ja oikealla puolella muistiinpanot.

![Aloitusnäkymä](kuvat/aloitusnakyma.png)

Laskutoimituksien tekeminen onnistuu syöttämälle Syöte:-kenttään haluttu luku ja valitsemalla painikkeista mitä luvulla halutaan laskea. Tulos näkyy alareunassa. Laskutoimitukset tehdään suhteessa tulokseen.

Oikealla puolella olevaan Muistiinpanot:-kenttään voi kirjoittaa haluamansa muistiinpanon, jonka voi tallentaa Tallenna-painikkeella. Tämän jälkeen muistiinpano tulee näkyviin Tallenna-painikkeen alapuolelle.



