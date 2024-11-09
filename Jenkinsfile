pipeline {
    agent any
    stages {
        stage('Clonar Repositorio') {
            steps {
                git url: 'https://github.com/BrunooRamos/prog_av_e3.git', branch: 'main'
            }
        }
        stage('Instalar Dependencias') {
            steps {
                sh '/usr/bin/python3 -m pip install ply'
            }
        }
        stage('Ejecutas Pruebas') {
            steps {
                sh '/usr/bin/python3 -m unittest discover -s test'
            }
        }
        stage('Generar Documentación') {
            steps {
                sh 'sudo mkdir -p /opt/docs && sudo chmod 777 /opt/docs'
                
                sh 'cd src && python3 -m pydoc -w fluent_api'
                
                sh 'sudo mv src/fluent_api.html /var/www/html/documentins/usql-traductor.html'
            }
        }
    }
    post {
        success {
            // Envía un correo con el archivo trivia.html adjunto y un mensaje de éxito
            emailext(
                to: 'martinsena2804@gmail.com',
                subject: 'Generación de Documentación Completada con Éxito',
                body: '''Hola Bruno,

La documentación ha sido generada exitosamente y el archivo trivia.html ha sido generado y movido a la ubicación correspondiente.

Puede ver la documentación correspondiente en este enlace: http://34.227.68.157/usql-traductor

Saludos,
Jenkins
                ''',
            )
        }
        
        failure {
            // Envía un correo en caso de que ocurra un fallo
            emailext(
                to: 'martinsena2804@gmail.com',
                subject: 'Error en la Generación de Documentación',
                body: '''Hola Martín,

Hubo un problema durante la generación de la documentación. Revisa el log de Jenkins para más detalles.

Puede ver la documentación anterior en este enlace: http://34.227.68.157/usql-traductor

Saludos,
Jenkins
                '''
            )
        }
    }
}
