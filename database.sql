    CREATE TABLE urls (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) UNIQUE,
        created_at TIMESTAMP DEFAULT CURRENT_DATE
    );