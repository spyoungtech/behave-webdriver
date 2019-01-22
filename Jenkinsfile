pipeline {
  agent {
    docker {
      image 'python:3.7'
    }

  }
  stages {
    stage('Install') {
      steps {
        sh '''python -m venv venv
source venv/bin/activate
ci/install.sh
'''
      }
    }
    stage('Test') {
      parallel {
        stage('Test') {
          steps {
            sh '''source venv/bin/activate
cd tests/demo-app
python ./runserver.py > /dev/null 2>&1 &
cd ../..
export ENV_BASE_URL=http://127.0.0.1:8000/
coverage run -m behave tests/features
coverage run -a -m pytest tests/unittests
'''
          }
        }
        stage('Security check') {
          steps {
            sh '''python -m venv security_venv
source security_venv/bin/activate
python -m pip install safety
safety check -r --full-report ./requirements.txt
'''
          }
        }
      }
    }
  }
}