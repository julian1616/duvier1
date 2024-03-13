pipeline {
    agent any
    
    stages {
        stage('Leer archivo Python') {
            steps {
                // Clonar el repositorio utilizando el token de acceso personal
                script {
                    withCredentials([string(credentialsId: 'github-token', variable: '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')]) {
                        sh "git clone https://$GITHUB_TOKEN@github.com/julian1616/duvier1.git"
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
