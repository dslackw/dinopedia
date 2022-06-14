SELECT 'CREATE DATABASE dinopedia'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'dinopedia');