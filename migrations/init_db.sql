CREATE TABLE passes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    height INT NOT NULL,
    location VARCHAR(100) NOT NULL,
    user_id INT NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'new'
);
