FROM node:21

WORKDIR /app

COPY package*.json ./
RUN npm install
COPY src/ src/
EXPOSE 3000

# Comando para ejecutar la aplicación
CMD ["node", "src/index.js"]