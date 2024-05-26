#!/bin/bash

# Construir la imagen Docker
docker build -t data-seed ./data-seed

# Ejecutar el contenedor Docker para poblar la base de datos
docker run --rm --network="host" -e POSTGRES_HOST=$POSTGRES_HOST -e POSTGRES_DB=$POSTGRES_DB -e POSTGRES_USER=$POSTGRES_USER -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD data-seed
