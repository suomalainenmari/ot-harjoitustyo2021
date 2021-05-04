## Arkkitehtuurikuvaus

### Rakenne

Ohjelmassa on sovellettu kerrosarkkitehtuuria, jossa ohjelma on jaettu kolmeen tasoon: UI, services ja calculator, sekä repositories. Kokonaisuuksien välisiä suhteita on havainnoillistettu pakkauskaaviolla:

![Pakkauskaavio](kuvat/pakkauskaavio.png)

Luokka UI sisältää käyttöliittymästä vastaavan koodin, ja luokka Calculator laskintoiminnallisuuden sovelluslogiikasta vastaavan koodin. UI:lla on riippuvuus luokkaan Calculator.

Muistiinpanojen käsittelystä vastaavat luokat NoteService ja NoteRepository. NoteService tarjoaa käyttöliittymälle muistiinpanojen tallentamiseen ja esittämiseen metodit. Tietojen tallennuksesta ja hakemisesta tietokannassa vastaa NoteRepository, joka tarjoaa NoteServicelle metodit.

### Käyttöliittymä

Käyttöliittymässä on vain yksi näkymä. Näkymästä vastaa luokka UI. 

### Sovelluslogiikka

Sovellus sisältää toiminnallisuuksia niin laskimen kun muistiinpanojen osalta, ja näistä toiminnallisuuksista vastaavat erilliset luokat, Calculator ja NotesService. Luokat tarjoavat kaikille käyttöliittymän toiminnoilla metodit.

### Tietojen pysyväistallennus

Pakkauksessa repositories oleva luokka NoteRepository vastaa muistiinpanojen pysyväistallennuksesta. Muistiinpanot tallennetaan SQLite tietokantaan. Repository- suunnittelumallin myötä NoteService luokan testauksessa on voitu käyttää stub-tyyppistä ratkaisua oikean tietokannan sijasta.

Pysyväistallennuksen tämänhetkisestä tilanteesta lisätietoa kohdassa "Ohjelman rakenteessa tällä hetkellä olevat heikkoudet
"

### Muistiinpanon lisääminen

Aloitusnäkymässä käyttäjä syöttää muistiinpanon sille varattuun kenttään ja painaa "Tallenna".

![Sekvenssikaavio](kuvat/muistiinpanon_lisaaminen.png)

Painikkeen painamiseen reagoi tapahtumankäsittelijä, joka kutsuu sovelluslogiikan NoteService metodia create_note jolla on parametrina syötekenttään syötetty sisältö. NoteService välittää tallennuspyynnön NoteRepositoryyn, jossa uusi muistiinpano lisätään tietokantaan. Tämän jälkeen UI:ssa olevalle muuttujalle, joka näyttää muistiinpanot listassa, asetetaan uusi arvo. Tämä tapahtuu kutsumalla NoteServicen metodia _show_notes(). NoteService puolestaan kutsuu NoteRepositoryn metodia get_all_notes, joka palauttaa kaikki tietokantaan haetut vinkit. Kun tämä UI:ssa olevan muuttujan arvo päivittyy renderöityy se ruudulle, ja käyttäjä näkee tallennetun muistiinpanon näytöllä heti.

## Ohjelman rakenteessa tällä hetkellä olevat heikkoudet

Tällä hetkellä muistiinpanoja ei voi käsitellä yksitellen, eikä poistaa, vaan tulevat merkkijonomuuttujana näkyviin. Myöskin tietokanta tyhjenee jokaisen käynnistyksen välissä. Nämä heikkoudet on tarkoitus saada korjattua tulevissa versioissa.