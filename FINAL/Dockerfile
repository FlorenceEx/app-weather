# DEBIAN
#FROM debian

# PYTHON
#FROM python:slim-bullseye

# ALPINE
FROM alpine
# On installe python
RUN apk add py3-pip

ADD requirements.txt ./
RUN pip3 \ 
        install \
            -r requirements.txt \
            --break-system-package ; \
    adduser \
        --home /app \
        --disabled-password app

# On copie les fichiers
COPY . .

# On ouvre le port 5000
EXPOSE 5000

# On exécute l'application
CMD ["python3", "weather.app.py"]