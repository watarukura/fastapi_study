#!/bin/bash

cat <<EOF |
USE test;

CREATE TABLE user (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL,
    age INT,
    PRIMARY KEY (id)
);

INSERT INTO
    user (name, age)
VALUES
    ("太郎", 15),
    ("次郎", 18),
    ("花子", 20);
EOF
mysql -h localhost \
    -u "${MYSQL_USER}" \
    -p"${MYSQL_PASSWORD}" \
    -P 3306 \
    "${MYSQL_DATABASE}" \
    --default-character-set=utf8 