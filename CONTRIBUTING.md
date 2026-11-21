# Contribuyendo al Proyecto

¡Pasos para contribuir a este proyecto!
¡Esto es parte de una practica del curso de Git-GitHub, no dudes en mejorar este archivo!

## 📌 Requisitos previos

Antes de comenzar, asegúrate de tener:

- Una cuenta en GitHub
- Git instalado en tu sistema operativo
- Un editor de código como VS Code

## 🔄 Proceso de contribución

1. **Haz un fork del repositorio**

   - Ve al repositorio original en GitHub.
   - Haz clic en el botón **Fork** en la parte superior derecha.
   - Esto creará una copia del repositorio en tu cuenta de GitHub.

2. **Clona tu fork en tu máquina**

   - Esto lo puedes hacer mediante HTTPS o SSH si tienes configurada una llave

   ```bash
   git clone https://github.com/TU_USUARIO/git-github.git
   ```

   Luego, entra en el directorio del proyecto:

   ```bash
   cd git-github
   ```

3. **Añadir el repositorio original como remoto**
   Para mantener tu fork actualizado con el código mas reciente:

   ```bash
   git remote add upstream https://github.com/ORIGINAL_OWNER/git-github.git
   ```

4. **Crear una nueva rama**
   Este repositorio solo usa la rama `main`, por lo que debes crear una nueva rama para tu cambio:

   ```bash
   git switch -c nombre-de-tu-rama
   ```

5. **Realizar los cambios y confirmarlos**

   - Haz las modificaciones necesarias en el código.
   - Cuando estes conforme con tus cambios guarda los archivos y agrega un commit
     ```bash
     git add .
     ```
   - Crea un commit con un mensaje claro de lo que hiciste:
     ```bash
     git commit -m "Descripción breve de los cambios"
     ```

6. **Subir los cambios a tu fork**

   ```bash
   git push origin nombre-de-tu-rama
   ```

7. **Crear un Pull Request (PR)**
   - Ve a tu repositorio en GitHub.
   - Verás una notificación para hacer un **Pull Request**.
   - Selecciona `main` como la rama de destino en el repositorio original.
   - Añade una descripción clara sobre los cambios realizados.
   - Envía el PR y espera revisión.

## ✅ Listo

¡¡Si aprueban tu PR podras ver tus cambios en el repositorio original!!
