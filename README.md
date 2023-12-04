# Individual Project 4
This project builds a publicly accessible auto-scaling container using Azure App Services and Flask. I designed a web app that returns welcoming messages and the current UTC time as a clock converter. DockerHub is used to build a container. This app runs at the public URL provided by Azure.

## Steps
1. Set up environment. Modify the `requirement.txt` file to install `flask` package in GitHub CodeSpace.
2. Create a HTML template `index.html` in templates folder. My template returns two welcome messages and currect UTC time.
3. Build a flask app `app.py` that utlizes the template file.
4. Use the following command to build docker file. Be sure to expose the port 9000 Commands
```
docker build myapp
docker run -p 9000:9000 myapp
```
Your terminal should look like this. 
<img width="1070" alt="Screenshot 2023-12-03 at 20 09 24" src="https://github.com/nogibjj/KatherineT.DE.Individual-Project-4/assets/143833511/a0b82f7b-5186-4d65-85d3-a403d7ed937f">
<img width="885" alt="Screenshot 2023-12-03 at 20 09 40" src="https://github.com/nogibjj/KatherineT.DE.Individual-Project-4/assets/143833511/acc6adb5-8296-4298-ac52-9c330187c212">


5. Use the following command to log into DockerHub, build container and push
```
docker login --username
docker build -t username/reponame .
docker push username/reponame
```
Your terminal should look like this. 

<img width="695" alt="Screenshot 2023-12-03 at 20 09 45" src="https://github.com/nogibjj/KatherineT.DE.Individual-Project-4/assets/143833511/c3375af2-8a03-4168-82bc-6bc11867d89c">
<img width="849" alt="Screenshot 2023-12-03 at 20 09 52" src="https://github.com/nogibjj/KatherineT.DE.Individual-Project-4/assets/143833511/5747804b-734c-4c2d-ad34-72a906818eee">
<img width="830" alt="Screenshot 2023-12-03 at 20 10 06" src="https://github.com/nogibjj/KatherineT.DE.Individual-Project-4/assets/143833511/bed20af9-893f-49c8-96a5-bac4879bcab5">

6. Check the repo on DockerHub. You would see a tag created like this.
7. 
![Screenshot 2023-12-03 at 20 38 32](https://github.com/nogibjj/KatherineT.DE.Individual-Project-4/assets/143833511/0acf19dc-2829-4af0-88c3-70871f83a568)

8. Set up a web app on Azure. Select Docker Container and insert your DockerHub image and tag when creating the web app.
9. After deployment, go to configuration to add "WEBSITES_PORT" with a value of 9000.
    
![Screenshot 2023-12-03 at 20 52 31](https://github.com/nogibjj/KatherineT.DE.Individual-Project-4/assets/143833511/8d26a470-34eb-439c-9e20-e49b2a86fcc0)
11. Browse your web app from the domain! This is my web app.

![Screenshot 2023-12-03 at 20 53 58](https://github.com/nogibjj/KatherineT.DE.Individual-Project-4/assets/143833511/53fb0286-b810-4973-a165-535700555e9a)

## Public URL
utcwebapp.azurewebsites.net

## References
1. https://learn.microsoft.com/en-us/azure/app-service/tutorial-custom-container?tabs=azure-portal&pivots=container-linux
2. https://learn.microsoft.com/en-us/azure/devops/pipelines/apps/cd/deploy-docker-webapp?view=azure-devops&tabs=java%2Cyaml



