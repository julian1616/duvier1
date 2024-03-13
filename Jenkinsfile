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
        
        stage('Ejecutar aplicación Flask') {
            steps {
                script {
                    sh "python importrandom.py &"
                }
            }
        }
        
        stage('Enviar mensaje de texto') {
            steps {
                script {
                    def accountSid = 'tu_account_sid'
                    def authToken = 'tu_auth_token'
                    def toNumber = '+573192246527'  // Reemplaza con tu número de teléfono
                    def fromNumber = '+1234567890'  // Reemplaza con tu número de teléfono Twilio

                    def twilio = new com.twilio.Twilio(accountSid, authToken)
                    def message = twilio.message(toNumber, fromNumber, 'La aplicación Flask se ejecutó correctamente en Jenkins.')
                    echo "Mensaje de texto enviado con éxito a ${toNumber}"
                }
            }
        }
    }
}
