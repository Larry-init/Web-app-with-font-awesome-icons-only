pipeline {

    agent { dockerfile true }
    // agent {
    //     dockerfile {
    //         dir'jenkins/'
    //     }
    // }

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
                sh "chmod +x ./py/run.sh"
                sh "./py/run.sh"
            }
        }
        
    }

    
}
