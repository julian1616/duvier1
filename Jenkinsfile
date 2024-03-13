pipeline {
    agent any
    
    stages {
        stage('Verificar Python') {
            steps {
                script {
                    def pythonPath = sh(script: 'which python3', returnStdout: true).trim()
                    if (pythonPath) {
                        echo "Python está instalado en: ${pythonPath}"
                        // Guardar la ubicación de Python en una variable global
                        env.PYTHON_PATH = pythonPath
                    } else {
                        error "Python no está instalado en el sistema"
                    }
                }
            }
        }
        
        stage('Verificar opciones de conexión') {
            steps {
                // Usar la variable de entorno PYTHON_PATH para ejecutar comandos de Python
                script {
                    if (env.PYTHON_PATH) {
                        def salidaPython = sh(script: '${env.PYTHON_PATH} duvier1/tu_script.py', returnStdout: true).trim()
                        echo "El resultado de Python es: ${salidaPython}"
                    } else {
                        error "No se encontró la ubicación de Python. La verificación de Python debe realizarse primero."
                    }
                }
            }
        }
        
        stage('Actualizar repositorio') {
            steps {
                // Actualizar el repositorio existente
                script {
                    sh "cd duvier1 && git pull"
                }
            }
        }
        
        stage('Leer archivo Python') {
            steps {
                // Ejecutar un comando de Python para leer el archivo
                script {
                    if (env.PYTHON_PATH) {
                        def salidaPython = sh(script: '${env.PYTHON_PATH} duvier1/tu_script.py', returnStdout: true).trim()
                        echo "El resultado de Python es: ${salidaPython}"
                    } else {
                        error "No se encontró la ubicación de Python. La verificación de Python debe realizarse primero."
                    }
                }
            }
        }
    }
}
