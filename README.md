![Screenshot (184)](https://github.com/user-attachments/assets/b065fca7-8bad-4a17-b9b4-0ec8917d370d)
![Screenshot (185)](https://github.com/user-attachments/assets/c028cd23-40f3-4bab-8c4d-8f6fbd92b8f3)

# AWS Jenkins CI/CD Pipeline Integration

## Description

This project sets up a CI/CD pipeline using Jenkins, Docker, and AWS services to automate the deployment of a Dockerized application. The pipeline performs tasks such as logging into AWS ECR, checking out code, building Docker images, pushing them to ECR, updating ECS task definitions, and deploying to ECS.



## Getting Started

### Prerequisites

List any prerequisites needed to run the project, such as software or libraries. For example:

- Docker: For containerizing your application.
- Jenkins: For automating the CI/CD pipeline.
- AWS CLI: For interacting with AWS services.
- Git: For cloning the repository.
- Java: Required for running Jenkins.

  
### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repo.git
    ```

2. Navigate to the project directory:
    ```bash
    cd your-repo
    ```

3. Set Up Jenkins:
   - Install Jenkins following the official documentation.
   - Install necessary Jenkins plugins, including the AWS CLI, Docker, and Git plugins.

4. Install Docker
 -  Docker installation guide suitable for your operating system.

5. Configure AWS CLI
    ```bash
    aws configure
    ```

## Usage

Running the Application Locally
1. Build Docker Image:
  ```bash
    docker build -t your-app-name .

  ```

3. Run Docker Container
  ```bash
    aws configure
   ```
5. Access the Application
  ```bash
    docker run -p 5000:5000 your-app-name

  ```
## Running the CI/CD Pipeline

1. Access Jenkins:Open Jenkins in your browser and create a new pipeline job.
2. Configure Pipeline :Set up Jenkins credentials for AWS and Docker.Define the pipeline script (Jenkinsfile) to automate the CI/CD process.
## CI/CD Pipeline

Describe the CI/CD pipeline setup and steps involved. For example:

1. Login to AWS ECR
2. Checkout code
3. Build Docker image
4. Push to ECR
5. Update ECS Task Definition
6. Deploy to ECS

## Troubleshooting
- Pipeline Fails: Check Jenkins logs for errors and ensure all required plugins and configurations are correct.
- Docker Build Issues: Verify your Dockerfile and build context.

- AWS Permissions: Ensure your AWS credentials have the necessary permissions for ECR and ECS operations
