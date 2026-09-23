pipeline {
    agent any

    environment {
        IMAGE_NAME = "student-feedback"
        CONTAINER_NAME = "student-feedback-app"
        APP_PORT = "5000"
    }

    stages {
        // Stage 1: Pull the latest source code from Git / GitHub
        stage('Checkout') {
            steps {
                echo '=== Stage 1: Checking out code from GitHub repository ==='
                checkout scm
            }
        }

        // Stage 2: Validate application code and run unit tests
        stage('Build') {
            steps {
                echo '=== Stage 2: Validating Python Code and Running Tests ==='
                sh 'python3 -m py_compile app.py || python -m py_compile app.py'
                sh 'python3 test_app.py || python test_app.py'
                echo 'Application code verification and unit tests passed successfully!'
            }
        }

        // Stage 3: Build Docker image packaging the application
        stage('Docker Build') {
            steps {
                echo "=== Stage 3: Building Docker Image: ${IMAGE_NAME}:${BUILD_NUMBER} ==="
                sh "docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} -t ${IMAGE_NAME}:latest ."
                echo 'Docker container image built successfully!'
            }
        }

        // Stage 4: Deploy the containerized application
        stage('Deploy') {
            steps {
                echo '=== Stage 4: Deploying Application via Docker Container ==='
                // Stop and remove previous container if running
                sh "docker stop ${CONTAINER_NAME} || true"
                sh "docker rm ${CONTAINER_NAME} || true"
                // Run new container instance
                sh "docker run -d -p ${APP_PORT}:5000 --name ${CONTAINER_NAME} ${IMAGE_NAME}:latest"
                echo "Application successfully deployed! Accessible at http://localhost:${APP_PORT}"
            }
        }
    }

    // Post-execution notifications
    post {
        success {
            echo '==================================================='
            echo ' DevOps CI/CD Pipeline Completed Successfully!    '
            echo ' Student Feedback App is live at port 5000.        '
            echo '==================================================='
        }
        failure {
            echo '==================================================='
            echo ' Pipeline execution failed. Please check build log.'
            echo '==================================================='
        }
    }
}
