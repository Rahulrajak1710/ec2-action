pipeline {
    agent any
    environment {
        AWS_ACCOUNT_ID = "730335487526"
        AWS_DEFAULT_REGION = "us-east-2"
        IMAGE_REPO_NAME = "oriserve"
        IMAGE_TAG = "latest"
        REPOSITORY_URI = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}"
        CLUSTER_NAME = "oriserve"  // Replace with your ECS cluster name
        SERVICE_NAME = "oriserveService1"  // Replace with your ECS service name
        TASK_DEFINITION_NAME = "oriserveTaskDefinition" // Replace with your ECS task definition name
    }

    stages {
        stage('Login to AWS ECR') {
            steps {
                script {
                    sh """
                    aws ecr get-login-password --region ${AWS_DEFAULT_REGION} | \
                    docker login --username AWS --password-stdin ${REPOSITORY_URI}
                    """
                }
            }
        }

        stage('Checkout Code') {
            steps {
                git url: "https://github.com/Rahulrajak1710/python-application.git", branch: "master"
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_REPO_NAME}:${IMAGE_TAG}")
                }
            }
        }

        stage('Push to ECR') {
            steps {
                script {
                    sh """
                    docker tag ${IMAGE_REPO_NAME}:${IMAGE_TAG} ${REPOSITORY_URI}:${IMAGE_TAG}
                    docker push ${REPOSITORY_URI}:${IMAGE_TAG}
                    """
                }
            }
        }

    stage('Updating ECS Task Definition') {
    steps {
        script {
            
            def taskDef = sh(
                script: """aws ecs describe-task-definition --task-definition ${TASK_DEFINITION_NAME} --query 'taskDefinition' --output json""",
                returnStdout: true
            ).trim()

            
            def updatedTaskDef = sh(
                script: """
                echo '${taskDef}' | jq 'del(.taskDefinitionArn, .revision, .status, .requiresAttributes, .compatibilities, .registeredAt, .registeredBy, .tags) | .containerDefinitions[0].image = \"${REPOSITORY_URI}:${IMAGE_TAG}\"'
                """,
                returnStdout: true
            ).trim()

            
            def newTaskDef = sh(
                script: """aws ecs register-task-definition --cli-input-json '${updatedTaskDef}'""",
                returnStdout: true
            ).trim()

            env.NEW_TASK_DEFINITION_ARN = sh(
                script: """echo '${newTaskDef}' | jq -r '.taskDefinition.taskDefinitionArn'""",
                returnStdout: true
            ).trim()
        }
    }
}


        stage('Deploy to ECS') {
            steps {
                script {
                    sh """
                    aws ecs update-service \
                    --cluster ${CLUSTER_NAME} \
                    --service ${SERVICE_NAME} \
                    --task-definition ${env.NEW_TASK_DEFINITION_ARN} \
                    --force-new-deployment \
                    --region ${AWS_DEFAULT_REGION}
                    """
                }
            }
        }
    }
}

