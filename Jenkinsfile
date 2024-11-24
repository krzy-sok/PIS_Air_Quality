pipeline {
    agent {
        node {
            label 'python-agent'
            }
      }
    triggers{
        githubPush()
    }
    stages {
    stage('Build') {
        when{
            anyOf{
                branch 'master'
                branch 'development'
            }
        }
        steps {
            echo "Building.."
            sh '''
            pipx ensurepath
            '''
        }
    }
    stage('Test') {
        when{
            anyOf{
                branch 'master'
                branch 'development'
            }
        }
        steps {
            echo "Testing.."
            sh '''
            echo "doing test stuff.."
            '''
        }
    }
    stage('Deliver') {
        when{
            branch 'master'
            branch 'development'
        }
        steps {
            echo 'Deliver....'
            sh '''
            echo "doing delivery stuff.."
            '''
        }
    }
}
}