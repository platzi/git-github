#!/bin/bash
# Primeramente, elimina imágenes no etiquetadas
docker image prune -a
# Luego, elimina contenedores detenidos
docker container prune
# Seguidamente, elimina volúmenes sin uso
docker volume prune
# Opcionalmente, elimina sistemas no utilizados
docker system prune
# Finalmente, limpia caché de imágenes
docker builder prune