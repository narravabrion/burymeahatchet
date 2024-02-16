pipeline {
    agent any

    stages {
        stage('clean workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Clone Repository') {
            steps {
                script {
                    scmVars = checkout(scm)
                    env.BRANCH_NAME = scmVars.GIT_BRANCH
                    env.GIT_COMMIT = "${scmVars.GIT_COMMIT[0..7]}"
                    env.GIT_REPO_NAME = scmVars.GIT_URL.replaceFirst(/^.*\/([^\/]+?).git$/, '$1')
                    GIT_REPO_NAME = env.GIT_REPO_NAME
                }
            }
        }

        stage('Create Virtual Environment') {
            steps {
                script {
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate'
                    sh 'venv/bin/pip3 install -r requirements.txt'
                }
            }
        }

        stage('Run Test') {
            parallel {
                stage('Lint Test') {
                    steps {
                        script {
                            try {
                                // sh 'python3 -m venv venv && . venv/bin/activate && pip install -r requirements.txt'
                                sh 'pwd'
                                sh 'venv/bin/python3 pre-commit install'
                                sh 'venv/bin/python3 pre-commit run --all-files --output-format=json:lint.json,colorized'
                            }
                        catch (Error|Exception err) {
                                echo err
                        }
                        }
                    }
                }
                stage('Unit Test') {
                    steps {
                        script {
                            try {
                                // sh 'python3 -m venv venv && . venv/bin/activate && pip install -r requirements.txt'
                                sh 'pwd'
                                sh 'venv/bin/python3 pytest -v --junitxml=test-results.xml'
                            }
                            catch (Error|Exception err) {
                                echo err
                            }
                        }
                    }
                }
                stage('coverage') {
                    steps {
                        script {
                            try {
                                // sh 'python3 -m venv venv && . venv/bin/activate && pip install -r requirements.txt'
                                sh 'pwd'
                                sh 'venv/bin/python3 coverage run -m pytest'
                                sh 'venv/bin/python3 coverage xml'
                            }
                            catch (Error|Exception err) {
                                echo err
                            }
                        }
                    }
                }
            }
        }
    }

    post {
        always {
            // junit 'test-results.xml'
            // publishHTML([allowMissing: false, alwaysLinkToLastBuild: true, keepAll: true, reportDir: 'htmlcov', reportFiles: 'index.html', reportName: 'Code Coverage Report'])
            // publishHTML([allowMissing: false, alwaysLinkToLastBuild: true, keepAll: true, reportDir: '.', reportFiles: 'lint.json', reportName: 'Lint Report'])
            // archiveArtifacts artifacts: 'lint.json', fingerprint: true
            // archiveArtifacts artifacts: 'test-results.xml', fingerprint: true
            // archiveArtifacts artifacts: 'htmlcov', fingerprint: true
            // archiveArtifacts artifacts: 'coverage.xml', fingerprint: true
            script {
                try {
                    sh 'deactivate'
                    sh 'rm -rf venv'
                }
                catch (Error|Exception err) {
                    echo err
                }
            }
        }
    }
}
