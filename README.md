# Ohjelmistotekniikka 2021

Repositorio Helsingin yliopiston kurssin Ohjelmistotekniikka(TKT20002) laskutehtäville, sekä harjoitustyölle.

## Graafinen laskin

Sovelluksen avulla käyttäjien on mahdollista suorittaa aritmeettisia laskutoimituksia.

Sovellus on luotu Helsingin yliopiston kurssille Ohjelmistotekniikka harjoitustyöksi.

### Dokumentaatio

[Vaatimusmäärittely](/dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjanpito](/dokumentaatio/tuntikirjanpito.md)

[Arkkitehtuuri](/dokumentaatio/arkkitehtuuri.md)

[Viikon 5 release](https://github.com/suomalainenmari/ot-harjoitustyo2021/releases/tag/viikko5)

### Sovelluksen käynnistäminen

Sovelluksen toiminta on testattu Python-versiolla `3.6.9`. Mikäli käytössä ilmenee ongelmia, huomioithan, että versiolla voi olla vaikutusta asiaan.

1. Sovellus käyttää riippuvuuksien hallintaan poetrya. Voit varmistaa, että koneeltasi löytyy poetry komennolla:

```bash
poetry --version
```

Mikäli sinulla ei vielä poetrya ole, poetryn dokumentaatio tarjoaa useita [asennusvaihtoehtoja](https://python-poetry.org/docs/#installation)

2. Kun poetry on asennettu, voit kloonata projektin koneellesi.

3. Kun projekti on kloonattu, asenna riippuvuudet ja alusta virtuaaliympäristö komennolla:

```bash
poetry install
```
4. Alusta projektin tietokanta komennolla:
```bash
poetry run invoke build
```

5. Käynnistä sovelus komennolla:

```bash
poetry run invoke start
```

### Testaus

Sovelluksessa on tällä hetkellä käytössä yksikkötestejä. Sovellusta käynnistäessä ajettu **poetry install**-komento on asentanut testausta varten tarvittavat riippuvuudet.

Testit voi suorittaa komennolla:
```bash
poetry run invoke test
```


### Testikattavuusraportti

Testikattavuusraportin voi muodostaa seuraavalla komennolla:

```bash
poetry run invoke coverage-report
```

Raportti (index.html) löytyy projektiin muodostuvasta hakemistosta htmlcov.

### Pylint tyylitarkastus

Tyylillisen tarkastuksen voi muodostaa seuraavalla komennolla:

```bash
poetry run invoke lint
```
