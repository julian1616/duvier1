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
        
        stage('Clonar o confirmar existencia del repositorio') {
            steps {
                script {
                    def repositoryName = "duvier10"
                    def repositoryURL = "https://github.com/tu-usuario/${repositoryName}.git"

                    // Verificar si el repositorio ya está clonado
                    if (fileExists(repositoryName)) {
                        echo "El repositorio ${repositoryName} ya está clonado"
                    } else {
                        // Si el repositorio no está clonado, clonarlo
                        echo "Clonando el repositorio ${repositoryName}..."
                        sh "git clone ${repositoryURL}"
                        echo "El repositorio ${repositoryName} se ha clonado exitosamente"
                    }
                }
            }
        }
        
        stage('Confirmación de ejecución al azar') {
            steps {
                // Ejecutar una ejecución al azar, por ejemplo, imprimir "ok"
                echo "ok"
            }
        }
    }
}

def fileExists(fileName) {
    return fileExists("${fileName}/.git")
}
