pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Package') {
            steps {
                sh "/opt/homebrew/bin/minikube image build -f Dockerfile -t app-demo:latest ."
            }
        }
        stage('DeployToK8S') {
            steps {
                sh "/usr/local/bin/helm upgrade --install app-demo ./app-demo-chart"
            }
        }
    }
}