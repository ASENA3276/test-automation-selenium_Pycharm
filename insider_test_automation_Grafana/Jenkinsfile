pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m pip install --upgrade pip
                    python3 -m pip install -r requirements.txt
                '''
            }
        }

        stage('Create Folders') {
            steps {
                sh '''
                    mkdir -p reports
                    mkdir -p screenshots
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    python3 -m pytest tests/ \
                    --html=reports/report.html \
                    --self-contained-html
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*.html', fingerprint: true, allowEmptyArchive: true
            archiveArtifacts artifacts: 'screenshots/*.png', fingerprint: true, allowEmptyArchive: true
        }
    }
}