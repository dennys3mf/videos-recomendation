# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios
COPY make-data.py .

# Instalar psycopg2 para la conexión con PostgreSQL
RUN pip install psycopg2-binary

# Ejecutar el script Python al iniciar el contenedor
CMD ["python", "make-data.py"]
