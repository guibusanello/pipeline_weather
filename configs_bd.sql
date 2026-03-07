-- Criação do usuário "guilherme"
CREATE USER guilherme WITH PASSWORD 'postgres';

-- Atribuição de privilégios ao usuário "guilherme"
GRANT ALL PRIVILEGES ON DATABASE postgres TO guilherme;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO guilherme;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO guilherme;
GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public TO guilherme;

-- Concessão de privilégios de superusuário ao usuário "guilherme"
ALTER USER guilherme WITH SUPERUSER;

-- Criação do banco de dados "weather_data"
CREATE DATABASE weather_data OWNER guilherme;

-- Verificação dos bancos de dados e usuários criados
SELECT datname FROM pg_database;
SELECT * FROM pg_roles;