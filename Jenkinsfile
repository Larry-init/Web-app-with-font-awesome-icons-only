pipeline {

    agent any

    stages {
        stage("fuck around"){
            steps{
                echo "find out"
                sh "pwd && ls -lart"
            }
        }

        stage("build"){
            steps{
                sh "docker build -t webapp ."
            }
        }
        
    }    
    
    }
