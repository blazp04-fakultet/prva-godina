CREATE TABLE
    korisnici (
        id INT PRIMARY KEY,
        ime VARCHAR(50) NOT NULL,
        prezime VARCHAR(50) NOT NULL,
        email VARCHAR(50) NOT NULL,
        telefon VARCHAR(50)
    );

CREATE TABLE
    vozila (
        id INT NOT NULL PRIMARY KEY,
        registracija VARCHAR(50) NOT NULL,
        tip_vozila VARCHAR(50) NOT NULL,
        boja VARCHAR(50) NOT NULL,
        vlasnik INT NOT NULL,
        CONSTRAINT fk_vlasnik FOREIGN KEY (vlasnik) REFERENCES korisnici (id)
    );

CREATE TABLE
    parking_mjesta (
        id INT NOT NULL PRIMARY KEY,
        lokacija VARCHAR(50) NOT NULL,
        status SMALLINT NOT NULL,
        vozilo INT NOT NULL,
        cijena DECIMAL(10, 2) NOT NULL,
        CONSTRAINT fk_vozilo FOREIGN KEY (vozilo) REFERENCES vozila (id)
    );

CREATE TABLE
    rezervacija (
        id NUMBER NOT NULL PRIMARY KEY,
        datum_od DATE NOT NULL,
        datum_do DATE NOT NULL,
        broj_redova NUMBER NOT NULL,
        cijena NUMBER (10, 2) NOT NULL,
        korisnik NUMBER NOT NULL,
        mjesto NUMBER NOT NULL,
        CONSTRAINT fk_korisnik_r FOREIGN KEY (korisnik) REFERENCES korisnici (id),
        CONSTRAINT fk_mjesto_r FOREIGN KEY (mjesto) REFERENCES parking_mjesta (id)
    );

CREATE TABLE
    naplata (
        id NUMBER NOT NULL PRIMARY KEY,
        datum DATE NOT NULL,
        iznos NUMBER (10, 2) NOT NULL,
        rezervacija NUMBER NOT NULL,
        CONSTRAINT fk_rezervacija FOREIGN KEY (rezervacija) REFERENCES rezervacija (id)
    );