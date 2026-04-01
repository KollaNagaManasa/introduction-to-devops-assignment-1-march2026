pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git ''
            }
        }

        stage('Build Docker') {
            steps {
                sh 'docker build -t aceest-app .'
            }
        }

        stage('Deploy K8s') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
            }
        }
    }
}
