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

3. Follow any specific setup instructions, such as installing dependencies or setting up environment variables.

## Usage

Provide instructions 
1. Access the application at `http://localhost:5000`.

## CI/CD Pipeline

Describe the CI/CD pipeline setup and steps involved. For example:

1. Login to AWS ECR
2. Checkout code
3. Build Docker image
4. Push to ECR
5. Update ECS Task Definition
6. Deploy to ECS

