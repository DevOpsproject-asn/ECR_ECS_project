# ECR_ECS_project
Project for : create the ECR repo and integrate with github repo  & make the automation  

Step –1 :  Create the aws ECR repo  


 Step-2 :  Create the Github repository 

 Step-3: Github repo add the project files   

Step-4: Go the github repo > setting > Secrets and variables > Actions  

     Add the secret values and make it variables. 

Step-5 : Also added the .github/workflows/build.yaml  configuration file  

build.yaml file : 

name: Build and push image to ECR 

on: push 

jobs: 

  build:  

    name: Build Image 

    runs-on: ubuntu-latest 

    steps: 

  

    - name: Check out code 

      uses: actions/checkout@v2 

     

    - name: Configure AWS credentials 

      uses: aws-actions/configure-aws-credentials@v1 

      with: 

        aws-access-key-id: ${{ secrets.ACCESS_KEY }} 

        aws-secret-access-key: ${{ secrets.SECRET_KEY }} 

        aws-region: ap-south-1 

  

    - name: Login to Amazon ECR 

      id: login-ecr 

      uses: aws-actions/amazon-ecr-login@v1 

  

    - name: Build, tag, and push image to Amazon ECR 

      env: 

        ECR_REGISTRY: ${{ steps.login-ecr.outputs.registry }} 

        ECR_REPOSITORY: demoecrrepo 

        IMAGE_TAG: image2 

      run: | 

        docker build -t $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG . 

        docker push $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG 

 


Step: To see the AWS ECR repo image came or not.

