pipeline {
    agent any
    
    stages {
        stage ('SCM checkout') {
            steps {
            git branch: 'main', url: 'https://github.com/renuka22-11/jenkins.git'
            }
                
        }
        stage ('docker image build') {
            steps {
            sh '/usr/bin/docker image build -t renuka1711/myhtml .'
            }
        }
        stage ('docker login') {
            steps {
                sh 'echo dckr_pat_06GfbV79siW2nGsGAZJ2uz97a7I | docker login -u renuka1711 --password-stdin'
            }
        }
        stage ('docker image push') {
            steps {
                sh '/usr/bin/docker image push renuka1711/myhtml '
            }
        }
        stage ('get the confirmation') {
            steps {
                input 'Do you want to Deploy ?'
            }
        }
        stage ('create docker servcie') {
            steps {
                sh '/usr/bin/docker service create --name flask-serivce -p 4000:4000 --replicas 2 renuka1711/myhtml'
            }
        }
        
    }
}
