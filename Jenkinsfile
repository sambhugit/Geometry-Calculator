pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'pip3 install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'python3 test.py'
      }
      post {
        always {
          junit 'test-reports/*.xml'
          sh 'python3 tobin.py'
        }
      }    
    }
    node {
  stage('SCM') {
    checkout scm
  }
  stage('SonarQube Analysis') {
    def scannerHome = tool 'sonarjen';
    withSonarQubeEnv() {
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }
}
  }
}
