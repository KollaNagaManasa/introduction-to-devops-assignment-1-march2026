pipeline {
    agent any

    environment {
        KUBECONFIG = '/etc/rancher/k3s/k3s.yaml'
    }

    stages {
        stage('Build Docker') {
            steps {
                sh 'docker build -t aceest-app .'
            }
        }

        stage('Deploy K8s') {
            steps {
                sh 'k3s kubectl apply -f k3s/manifests/deployment.yaml'
                sh 'k3s kubectl apply -f k3s/manifests/service.yaml'
            }
        }
    }
}
