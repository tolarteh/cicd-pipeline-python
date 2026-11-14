# Dockerfile
# Usa una imagen base oficial de Python. Elige una versión específica para consistencia.
FROM python:3.13-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia solo el archivo de requerimientos primero para aprovechar el cache de Docker
COPY requirements-lock.txt .

# Instala solo las dependencias de ejecución (Flask y Gunicorn)
# Usa --no-cache-dir para reducir el tamaño de la imagen
# --require-hashes obliga a usar versiones fijadas (==) con hashes verificados
# --only-binary :all: evita compilar paquetes desde código fuente (no ejecuta setup.py)
RUN python -m pip install --no-cache-dir --require-hashes --only-binary :all: -r requirements-lock.txt

# Crea un usuario sin privilegios para ejecutar la aplicación
RUN groupadd --system nonroot \
    && useradd --system --gid nonroot --no-create-home --shell /usr/sbin/nologin nonroot

# Copia el código de la aplicación (solo la carpeta app)
COPY --chown=root:root app/ ./app/

# Ejecuta el contenedor como usuario no root
USER nonroot

# Expón el puerto en el que Gunicorn servirá la aplicación
# Gunicorn por defecto usa 8000, así que usaremos ese.
EXPOSE 8000

# Comando para ejecutar la aplicación usando Gunicorn cuando el contenedor inicie
# 'app.app:app' significa: del archivo app.py dentro del paquete app, usa la instancia 'app' de Flask.
# 'workers=4' es un ejemplo, ajusta según sea necesario.
# 'bind 0.0.0.0:8000' hace que Gunicorn escuche en todas las interfaces de red en el puerto 8000.
CMD ["gunicorn", "--workers=4", "--bind=0.0.0.0:8000", "app.app:app"]