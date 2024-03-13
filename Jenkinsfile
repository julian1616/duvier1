pipeline {
    agent any
    
    environment {
        PYTHON_PATH = '/usr/bin/python3'
        REPO_PATH = '/ruta/a/duvier'
    }
    
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
        
        stage('Actualizar repositorio') {
            steps {
                // Actualizar el repositorio existente
                script {
                    sh "cd ${env.REPO_PATH} && git pull"
                }
            }
        }
        
        stage('Leer archivo Python') {
            steps {
                // Ejecutar un comando de Python para leer el archivo
                script {
                    def salidaPython = sh(script: "${env.PYTHON_PATH} ${env.REPO_PATH}/tu_script.py", returnStdout: true).trim()
                    echo "El resultado de Python es: ${salidaPython}"
                }
            }
        }
    }
}

