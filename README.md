Challenge Técnico: Cloud & Platform - Banco Galicia

Este repositorio contiene la resolución del desafío técnico para la posición de Cloud Architect. Consiste en una REST API desarrollada en Python, contenerizada y con un proceso de CI/CD automatizado.

📋 Descripción del Proyecto La aplicación es una API robusta que permite la gestión de ítems, diseñada bajo estándares modernos de desarrollo y escalabilidad.

Lenguaje: Python (FastAPI).

Documentación: Swagger (OpenAPI) integrada.

Contenerización: Docker / Buildah.

CI/CD: Jenkins.

🚀 Instalación y Ejecución Local Requisitos previos Docker instalado.

Python 3.9 o superior (opcional para ejecución sin contenedor).

Pasos para ejecución (Docker) Clonar el repositorio:

Bash git clone cd Construir la imagen:

Bash docker build -t api-galicia:latest . Correr el contenedor:

Bash docker run -d -p 8000:8000 --name api-galicia api-galicia:latest Acceder a la API:

API: http://localhost:8000

Swagger UI: http://localhost:8000/docs

🔄 Pipeline de CI/CD El despliegue está automatizado mediante un Jenkinsfile que cumple con los siguientes stages obligatorios:

Descarga de código: Integración con repositorio Git.

Compilación: Validación de dependencias y entorno.

Despliegue en contenedor: Generación de imagen y ejecución mediante Docker/Buildah.

