pipeline {
    agent any
    
    stages {
        stage('Leer archivo Python') {
            steps {
                // Clonar el repositorio utilizando HTTPS (solo para repositorios públicos)
                script {
                    sh "git clone https://github.com/julian1616/duvier1.git"
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
