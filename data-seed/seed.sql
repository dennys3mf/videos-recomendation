-- Crear tabla de usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    correo VARCHAR(255) NOT NULL UNIQUE
);

-- Crear tabla de videos
CREATE TABLE IF NOT EXISTS videos (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    url TEXT NOT NULL,
    etiquetas TEXT[] NOT NULL,
    usuario_id INT NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
);

-- Insertar datos en la tabla de usuarios
INSERT INTO usuarios (nombre, correo) VALUES
('Usuario 1', 'usuario1@example.com'),
('Usuario 2', 'usuario2@example.com');

-- Insertar datos en la tabla de videos
INSERT INTO videos (titulo, url, etiquetas, usuario_id) VALUES
('Video 1', 'https://youtu.be/Gjxm1s26dXY?si=7LL9oPayAU1VMC8N', ARRAY['música', 'entretenimiento'], 1),
('Video 2', 'https://youtu.be/6AZvs-HIkfk?si=MlFHmj3Twet_bJnP', ARRAY['deportes', 'noticias'], 1),
('Video 3', 'https://youtu.be/IydiZUwmCUw?si=-yKKMdhhvB-9M9lJ', ARRAY['comedia', 'divertido'], 2);
