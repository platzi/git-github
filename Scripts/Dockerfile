# Seleccionar la imagen base de Ubuntu
FROM ubuntu:latest

COPY script.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/script.sh && \
RUN    /usr/local/bin/script.sh

# Ejecutar comandos adicionales
RUN echo "Inicio de script" && \
    echo "Ejecutando tarea 1" && \
    echo "Ejecutando tarea 2" && \
    echo "script finalizado."