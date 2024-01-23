pipeline {
    agent any
    stages{
        stage('clean workspace'){
            steps{
                cleanWs()
            }
        }
        stage('Clone Repository'){
            final scmVars = checkout(scm)
            env.BRANCH_NAME = scmVars.GIT_BRANCH
            env.GIT_COMMIT = "${scmVars.GIT_COMMIT[0..7]}"
            env.GIT_REPO_NAME = scmVars.GIT_URL.replaceFirst(/^.*\/([^\/]+?).git$/, '$1')
            GIT_REPO_NAME = env.GIT_REPO_NAME
        }
        // create virtual environment
        stage('Create Virtual Environment'){
            steps{
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }
        // stage to run lint tets for django project using pre-commit
        stage('Run Test'){
            parallel{
                stage('Lint Test'){
                    steps{
                        try{
                            sh 'pre-commit run --all-files --output-format=json:lint.json,colorized'
                        }
                        catch(Error|Exception err){
                            echo err
                        }
                    }
                }
                stage('Unit Test'){
                    steps{

                        try{
                            sh 'pytest -v --junitxml=test-results.xml'
                        }
                        catch(Error|Exception err){
                            echo err
                        }
                    }
                }
                stage('coverage'){
                    steps{
                        try{
                            sh 'coverage run -m pytest'
                            sh 'coverage xml'
                        }
                        catch(Error|Exception err){
                            echo err
                        }
                    }
                }
            }
        }

    }
    post{
        always{
            // junit 'test-results.xml'
            // publishHTML([allowMissing: false, alwaysLinkToLastBuild: true, keepAll: true, reportDir: 'htmlcov', reportFiles: 'index.html', reportName: 'Code Coverage Report'])
            // publishHTML([allowMissing: false, alwaysLinkToLastBuild: true, keepAll: true, reportDir: '.', reportFiles: 'lint.json', reportName: 'Lint Report'])
            // archiveArtifacts artifacts: 'lint.json', fingerprint: true
            // archiveArtifacts artifacts: 'test-results.xml', fingerprint: true
            // archiveArtifacts artifacts: 'htmlcov', fingerprint: true
            // archiveArtifacts artifacts: 'coverage.xml', fingerprint: true
            steps{
                try{
                    sh 'deactivate'
                    sh 'rm -rf venv'
                }
                catch(Error|Exception err){
                    echo err
                }
            }
        }
    }
}
