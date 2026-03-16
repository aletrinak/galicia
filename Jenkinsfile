pipeline {
    agent any

    stages {
        stage('Descarga de Código') { // Stage de Git 
            steps {
                checkout scm
                echo 'Código descargado correctamente del repositorio.'
            }
        }

        stage('Compilación y Test') { // Stage de Compilación 
            steps {
                echo 'Instalando dependencias para validar el código...'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Build Contenedor') { // Uso de Docker/Buildah [cite: 16, 18, 21]
            steps {
                script {
                    // Se recomienda Buildah por seguridad, pero Docker es aceptado 
                    sh 'docker build -t api-galicia:latest .'
                }
            }
        }

        stage('Despliegue') { // Stage de Despliegue 
            steps {
                sh 'docker stop api-container || true && docker rm api-container || true'
                sh 'docker run -d --name api-container -p 8000:8000 api-galicia:latest'
                echo 'Aplicación desplegada. Acceda a http://localhost:8000/docs para el Swagger.'
            }
        }
    }
}