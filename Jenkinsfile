pipeline {
    agent any
    
    stages {
        stage('Leer archivo Python') {
            steps {
                // Clonar el repositorio utilizando el token de acceso personal
                script {
                    withCredentials([string(credentialsId: 'github-token', variable: 'GITHUB_TOKEN')]) {
                        sh "git clone https://$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@github.com/julian1616/duvier1.git"
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
