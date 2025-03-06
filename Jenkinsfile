pipeline {
    agent any
    
    stages {
	stage('Clone Repository') {
	    steps {
		git 'https://github.com/Zivan-R/ansible-deploy-f2-f4'
	    }
	}
	stage('Install Dependecies') {
	    steps {
		sh 'pip3 install -r app/requirements.txt'
	    }
	}
	stage('Run Tests') {
	    steps {
		sh 'pytest app/test_app.py'
	    }
	}
	stage('Build Docker Image') {
	    steps {
		sh 'docker build -t zivanr/python-app-f2-f4:latest ./app'
	    }
	}
	stage('Push Docker Image') {
	    steps {
		withCredentials([string(credentialsId: 'dockerhub_password', variable: 'bF*2JT3?gfWryaL')]) {
	    	    sh 'echo $DOCKERHUB_PASS | docker login -u zivanr --password-stdin'
		    sh 'docker push zivanr/python-app-f2-f4:latest'
	        }
	    }
	}
	stage ('Deploy Application') {
	    steps {
		sh 'docker run -d -p 8080:8080 zivanr/python-app-f2-f4:latest'
	    }
	}
    }
}
