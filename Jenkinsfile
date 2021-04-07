def WORK_DIR
def NETBOX_TOKEN
def FAILED_STAGE
pipeline {
    agent any 
    stages {
        stage('Code Review') { 
            steps {
                script {
                    WORK_DIR="Data_Model,tools,playbooks,tasks"
                    NETBOX_TOKEN="886363985b61be00bcaaeeb10fd746dcacfda25d"
                    sh "python3.7 ./tools/validateFilesYAML.py ${WORK_DIR}"
                }
            }
        }
        stage('Create templates') { 
            steps {
                script {
                    FAILED_STAGE=env.STAGE_NAME
                    sh "ansible-playbook -i ./inventory/nepal_inv ./playbooks/play_create_config_templates.yaml --fork=10"
                }
            }
        }
        stage('Config Devices') { 
            steps {
                script {
                    FAILED_STAGE=env.STAGE_NAME
                    sh "ansible-playbook -i ./inventory/nepal_inv ./playbooks/play_config_devices.yaml --fork=10 -e='activate_v=true'"
                }
            }
        }
        stage('Rollback') { 
            steps {
                script {
                    FAILED_STAGE=env.STAGE_NAME
                    sh "ansible-playbook -i ./inventory/nepal_inv ./playbooks/play_config_devices.yaml --fork=10 -e='activate_v=false'"
                }
            }
        }
        stage('Delivery') { 
            steps {
                script {
                    FAILED_STAGE=env.STAGE_NAME
                    sh "ansible-playbook -i ./inventory/controller_inv ./tools/job_clone_rep_controller.yaml --fork=10"
                }
            }
        }
    }
    post {
        always {
            echo 'Jenkins pipeline by NEP@L'
            logstashSend failBuild: true, maxLines: 1000
        }
        success {
            script {
                echo 'Cisco CONFIG_COMPLIANCE CI pipeline finished successfully'
            }
        }
        unstable {
            echo 'I am unstable'
        }
        failure {
            echo 'Nothing failed'
        }
        changed {
            echo 'Things were different before...'
        }
    }
}