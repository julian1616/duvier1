pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Verificar opciones de conexión') {
            steps {
                script {
                    try {
                        sh "ping -c 1 github.com"
                        echo "Opción 1: Conexión directa al servidor: Correcta"
                    } catch (Exception e) {
                        echo "Opción 1: Conexión directa al servidor: Fallida"
                    }

                    try {
                        sh "git ls-remote https://github.com/julian1616/duvier1.git"
                        echo "Opción 2: Conexión utilizando HTTPS: Correcta"
                    } catch (Exception e) {
                        echo "Opción 2: Conexión utilizando HTTPS: Fallida"
                    }

                    try {
                        sh "git ls-remote git@github.com:julian1616/duvier1.git"
                        echo "Opción 3: Conexión utilizando SSH: Correcta"
                    } catch (Exception e) {
                        echo "Opción 3: Conexión utilizando SSH: Fallida"
                    }
                }
            }
        }
        
        stage('Ejecutar script Python en Visual Studio Code') {
            steps {
                // Ejecutar el script Python desde Visual Studio Code
                sh "code /ruta/a/tu/script.py" // Reemplaza /ruta/a/tu/script.py con la ruta de tu script
            }
        }
    }
}
