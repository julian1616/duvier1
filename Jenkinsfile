pipeline {
    agent any
    
    stages {
        stage('Verificar opciones de conexión') {
            steps {
                script {
                    // Intento 1: Conexión directa al servidor
                    try {
                        sh "ping -c 1 github.com"
                        echo "Opción 1: Conexión directa al servidor: Correcta"
                    } catch (Exception e) {
                        echo "Opción 1: Conexión directa al servidor: Fallida"
                    }

                    // Intento 2: Conexión utilizando HTTPS
                    try {
                        sh "git ls-remote https://github.com/julian1616/duvier1.git"
                        echo "Opción 2: Conexión utilizando HTTPS: Correcta"
                    } catch (Exception e) {
                        echo "Opción 2: Conexión utilizando HTTPS: Fallida"
                    }

                    // Intento 3: Conexión utilizando SSH
                    try {
                        sh "git ls-remote git@github.com:julian1616/duvier1.git"
                        echo "Opción 3: Conexión utilizando SSH: Correcta"
                    } catch (Exception e) {
                        echo "Opción 3: Conexión utilizando SSH: Fallida"
                    }
                }
            }
        }
        
        stage('Leer archivo Python') {
            steps {
                // Clonar el repositorio utilizando el token de acceso personal
                script {
                    sh "git clone https://$GITHUB_TOKEN@github.com/julian1616/duvier1.git"
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