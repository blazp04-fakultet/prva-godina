-- Baza podataka za aplikaciju koja korisncima daje kazne ovisno o tome koji prekršaj su uradili.Ovo je reducani model koji umjesto svega što treba imati ima samo najonsovnije stvari koje postoje Ali baš naj najosnovnije do te mjere da fali podatak tko je dao kaznu opće
CREATE TABLE
    renata_zupanija (
        id INT PRIMARY KEY,
        naziv VARCHAR2 (50) NOT NULL,
        isDeleted NUMBER (1) DEFAULT 0,
        creation_date DATE NOT NULL,
        delition_date DATE
    );

CREATE TABLE
    renata_opcina (
        id INT PRIMARY KEY,
        naziv VARCHAR2 (50) NOT NULL,
        zupanija_id INT NOT NULL,
        isDeleted NUMBER (1) DEFAULT 0,
        creation_date DATE NOT NULL,
        delition_date DATE,
        CONSTRAINT fk_zupanija FOREIGN KEY (zupanija_id) REFERENCES renata_zupanija (id)
    );

CREATE TABLE
    renata_korisnici (
        id INT PRIMARY KEY,
        ime VARCHAR2 (50) NOT NULL,
        prezime VARCHAR2 (50) NOT NULL,
        adresa VARCHAR2 (50) NOT NULL,
        registration_date DATE NOT NULL,
        delition_date DATE,
        isDeleted NUMBER (1) DEFAULT 0,
        opcina_id INT NOT NULL,
        CONSTRAINT fk_opcina FOREIGN KEY (opcina_id) REFERENCES renata_opcina (id)
    );

CREATE TABLE
    renata_kazne (
        id INT PRIMARY KEY,
        amount INT NOT NULL,
        description VARCHAR2 (50) NOT NULL,
        creation_date DATE NOT NULL,
        completed_date DATE,
        korisnik_id INT NOT NULL,
        isDeleted NUMBER (1) DEFAULT 0,
        CONSTRAINT fk_korisnik FOREIGN KEY (korisnik_id) REFERENCES renata_korisnici (id),
    );