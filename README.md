# Video Recommendation System

Este proyecto es un sistema de recomendación de videos que sugiere el siguiente video a visualizar a partir del tercer video visto por el usuario, basado en el tiempo de visualización y las etiquetas de los videos.

## Instalación

1. Clona el repositorio:
   ```sh
   git clone https://github.com/dennys3mf/videos-recomendation.git
   cd videos-recomendation
Configura las variables de entorno. Copia .env.example a .env y completa los valores necesarios.
# Ejecutar aplicacion
docker-compose up --build

### 2. Pruebas Unitarias y de Integración

Agrega un directorio `tests` y configura un framework de pruebas como `Jest` para Node.js. 

Instala `Jest` y `Supertest`:

```sh
npm install --save-dev jest supertest
