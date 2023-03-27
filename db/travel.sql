DROP TABLE IF EXISTS visits;
DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    country_id INT NOT NULL REFERENCES countries(id)
);

CREATE TABLE visits (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users(id),
    city_id INT NOT NULL REFERENCES cities(id),
    visited BOOLEAN
)