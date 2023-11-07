pipeline {

    agent any

    stages {
        stage("fuck around"){
            steps{
                echo "find out"
                sh "pwd && ls -lart"
            }
        }
        stage("Send Report"){
            steps{
                slackSend channel: '#general', message: 'Hello Work'
            }
        }
        stage ("run command"){
            steps{
                sh "ls -lart"
                sh "chmod -R 775 /py/run.sh"
                sh "./run.sh"
            }
        }
        
    }

    
}
