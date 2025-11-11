FROM nginx:1.27.2

RUN apt-get update && apt-get -y upgrade

RUN groupadd -r benja && useradd -r -g benja benja
RUN chown -R benja:benja /usr/share/nginx/html
USER benja



CMD [ "bash", "-c", "echo hello from appuser!!" ]
