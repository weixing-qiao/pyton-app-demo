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
                minikube build -f Dockerfile -t app-demo:latest .
            }
        }
        stage('DeployToK8S') {
            steps {
                helm upgrade --install app-demo ./app-demo-chart
            }
        }
    }
}