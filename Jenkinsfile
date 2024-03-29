pipeline {
    agent any

    environment {
        SECRET_KEY = 'django-insecure-ad3il=wq^p2(&8+7534g6rfeiuc#5nh7gy&k$48#zzasi--+tj'
    }

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
                    // env.GIT_COMMIT = '${scmVars.GIT_COMMIT[0..7]}'
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

                                // sh 'venv/bin/python3 git config --unset-all core.hooksPath'
                                // sh 'venv/bin/python3 $env.WORKSPACE/venv/bin/pre-commit install'
                                // sh '. venv/bin/activate && which pre-commit'
                                // sh 'venv/bin/python3 $env.WORKSPACE/venv/bin/pre-commit run --all-files --output-format=json:lint.json,colorized'
                                sh 'cat /var/lib/jenkins/workspace/burymeahatchet_develop@tmp/durable-948baced/script.sh'
                                sh ". venv/bin/activate && venv/bin/python3 $env.WORKSPACE/venv/bin/pre-commit run --all-files --env-var=$SECRET_KEY"
                                sh 'cat /var/lib/jenkins/workspace/burymeahatchet_develop@tmp/durable-948baced/script.sh'
                            }
                        catch (Error|Exception err) {
                                echo err
                        }
                        }
                    }
                }
                // stage('Unit Test') {
                //     steps {
                //         script {
                //             try {
                //                 // sh 'python3 -m venv venv && . venv/bin/activate && pip install -r requirements.txt'
                //                 // sh 'venv/bin/python3 $env.WORKSPACE/venv/bin/pytest -v --junitxml=test-results.xml'
                //                 sh 'venv/bin/python3 $env.WORKSPACE/venv/bin/pytest'
                //             }
                //             catch (Error|Exception err) {
                //                 echo err
                //             }
                //         }
                //     }
                // }
                // stage('coverage') {
                //     steps {
                //         script {
                //             try {
                //                 // sh 'python3 -m venv venv && . venv/bin/activate && pip install -r requirements.txt'
                //                 sh 'venv/bin/python3 coverage run -m pytest'
                //                 sh 'venv/bin/python3 coverage xml'
                //             }
                //             catch (Error|Exception err) {
                //                 echo err
                //             }
                //         }
                //     }
                // }
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
