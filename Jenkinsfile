pipeline {
    agent any
    
    environment {
        GIT_REPO_URL = 'https://github.com/julian1616/duvier1.git'
    }
    
    stages {
        stage('Leer archivo Python') {
            steps {
                // Clonar el repositorio utilizando las credenciales
                script {
                    withCredentials([usernamePassword(credentialsId: 'duvier0', usernameVariable: 'julian1616', passwordVariable: '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')]) {
                        sh "git clone ${env.GIT_REPO_URL}"
                    }
                }

                // Ejecutar un comando de Python para leer el archivo
                script {
                    def salidaPython = sh(script: 'python tu_script.py', returnStdout: true).trim()
                    echo "El resultado de Python es: ${salidaPython}"
                }
            }
        }
    }
}
