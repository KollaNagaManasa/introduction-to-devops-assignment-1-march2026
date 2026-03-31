pipeline {
    agent any

    environment {
        IMAGE_NAME = "gym-app"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/KollaNagaManasa/introduction-to-devops-assignment-1-march2026.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker run $IMAGE_NAME pytest'
            }
        }

        stage('Run Application (Optional)') {
            steps {
                sh 'docker run -d -p 8080:8080 $IMAGE_NAME || true'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline executed successfully!'
        }
        failure {
            echo '❌ Pipeline failed! Check logs.'
        }
    }
}
