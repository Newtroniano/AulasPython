-- Criar o banco de dados (se não existir)
CREATE DATABASE IF NOT EXISTS game_db;
USE game_db;

-- Tabela 'level': Armazena os níveis
CREATE TABLE level (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT
);

-- Tabela 'user': Armazena as informações dos usuários
CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela 'user_level': Relacionamento muitos-para-muitos entre usuários e níveis
CREATE TABLE user_level (
    user_id INT NOT NULL,
    level_id INT NOT NULL,
    level_progress INT DEFAULT 0,  -- Por exemplo, progresso no nível
    PRIMARY KEY (user_id, level_id),
    FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE,
    FOREIGN KEY (level_id) REFERENCES level(id) ON DELETE CASCADE
);

SELECT * FROM  user where user.id=1;

USE game_db;