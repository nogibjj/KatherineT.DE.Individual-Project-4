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
![Screenshot 2023-12-03 at 20 38 32](https://github.com/nogibjj/KatherineT.DE.Individual-Project-4/assets/143833511/0acf19dc-2829-4af0-88c3-70871f83a568)


## References

![1 1-function-essence-of-programming](https://github.com/nogibjj/python-ruff-template/assets/58792/f7f33cd3-cff5-4014-98ea-09b6a29c7557)



