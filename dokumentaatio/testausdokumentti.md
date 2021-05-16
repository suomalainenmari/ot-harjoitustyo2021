# Testausdokumentti

Ohjelmaa on testattu automatisoidusti yksikkö- ja integraatiotasolla käyttäen unittestiä. Tämän lisäksi testausta on tehty järjestelmätasolla manuaalisesti.

## Yksikkö- ja integraatiotestaus

### Testauskattavuus

Käyttöliittymäkerrosta ei testata automatisoiduilla testeillä. Muiden ohjelmakerrosten osalta haaraumakattavuus on 97%.

![Haaraumakattavuus](kuvat/haaraumakattavuus.png)

Tiedostosta initialize_database.py on jätetty testaamatta tiedoston suoritus komentoriviĺtä. 