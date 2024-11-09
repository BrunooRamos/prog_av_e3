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
                
                sh 'sudo mv src/fluent_api.html /var/www/html/documentins/usql-parser.html'
            }
        }
    }
}
