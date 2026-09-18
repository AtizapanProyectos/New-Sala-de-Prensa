# Usamos una versión ligera de Python
FROM python:3.12-slim

# Evita que Python genere archivos basura (.pyc) y manda los logs directo a la consola
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Creamos la carpeta de trabajo dentro del contenedor
WORKDIR /app

# Instalamos las dependencias del sistema necesarias para compilar algunas librerías
RUN apt-get update \
    && apt-get install -y gcc libffi-dev libpq-dev \
    && apt-get clean

# Copiamos las dependencias e instalamos
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiamos todo el proyecto a la carpeta /app de Docker
COPY . /app/

# Exponemos el puerto 8000
EXPOSE 8000

# Comando para arrancar el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]