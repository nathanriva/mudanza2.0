CREATE TABLE tablearticulos (
    id int NOT NULL PRIMARY KEY,
    nombre TEXT NOT NULL
);

CREATE TABLE tablecompras (
    id_compra int NOT NULL PRIMARY KEY,  
    id_art int,
    cant int NOT NULL,
    in_stock BOOLEAN NOT NULL,
    FOREIGN KEY (id_art)
        REFERENCES tablearticulos (id)
);