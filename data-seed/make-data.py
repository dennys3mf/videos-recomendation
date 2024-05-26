import psycopg2
from psycopg2 import sql
import os

# Conexión a la base de datos PostgreSQL
conn = psycopg2.connect(
    host=os.environ.get('POSTGRES_HOST', 'localhost'),
    database=os.environ.get('POSTGRES_DB', 'videos'),
    user=os.environ.get('POSTGRES_USER', 'postgres'),
    password=os.environ.get('POSTGRES_PASSWORD', 'example')
)

cur = conn.cursor()

# Crear tablas si no existen
cur.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    correo VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS videos (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    url TEXT NOT NULL,
    etiquetas TEXT[] NOT NULL,
    usuario_id INT NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
);
""")

# Insertar datos de ejemplo
cur.execute("""
INSERT INTO usuarios (nombre, correo) VALUES
('Usuario 1', 'dennys@example.com'),
('Usuario 2', 'gabriela@example.com')
ON CONFLICT DO NOTHING;
""")

cur.execute("""
INSERT INTO videos (titulo, url, etiquetas, usuario_id) VALUES
('Video 1', 'https://youtu.be/Gjxm1s26dXY?si=7LL9oPayAU1VMC8N', ARRAY['música', 'entretenimiento'], 1),
('Video 2', 'https://youtu.be/6AZvs-HIkfk?si=MlFHmj3Twet_bJnP', ARRAY['deportes', 'noticias'], 1),
('Video 3', 'https://youtu.be/IydiZUwmCUw?si=-yKKMdhhvB-9M9lJ', ARRAY['comedia', 'divertido'], 2)
ON CONFLICT DO NOTHING;
""")

# Confirmar los cambios y cerrar la conexión
conn.commit()
cur.close()
conn.close()

