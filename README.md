# clone production_repo
clone repository: https://github.com/JimMcDonough/production_repo.git

#Getting Data
Download the SQuAD Training Set v2.0 (40mb) from https://rajpurkar.github.io/SQuAD-explorer/
and save it in your google drive.  

#Training model
Create a working driectory on your google drive and create a model folder for saving 
your final trained model. Open Collab notebook.  It is recommended to purchase  
compute units to use a premium gpu.  Upload QA_utils.py script from cloned repository 
into your notebook.  Run the notebook to train the model.  Save to your model working 
directory.  

Copy model checkpoint files into your cloned repository "/full_saved_model/" directory.

#Building and Launching Containerized Flask application on AWS
Follow instruction on the link below and use the premade docker file and flask app
from the cloned repositiory to deploy the containerized application.  Recommend using 
something larger than a t2.micro instance on AWS.  More memory is needed for installing 
all the libraries in the requirements.txt file.   
https://towardsdatascience.com/simple-way-to-deploy-machine-learning-models-to-cloud-fd58b771fdcf

You will upload to AWS app.py, Dockerfile, requirements.txt, and 
full_saved_model directory using the terminal command:

scp -i /path/my-key-pair.pem file-to-copy ec2-user@public-dns-name:/home/ec2-user

use -r command to recursively copy the full_saved_model directory

Follow the above article for more details.  

#Using Application
You must run the docker application using aws console or remote in from terminal.  
From the above article use these commands:

command remote in on terminal: ssh -i /path/my-key-pair.pem ec2-user@public-dns-name

start docker command: sudo service docker start
user mode command: sudo usermod -a -G docker ec2-user

command to run: docker run -p 80:80 <app_name> .

Send an HTTP request to the aws_public_DNS provide on aws (looks like this 
ec2–x–x–x–x.compute-1.amazonaws.com).  

You should pass in two variables in the request: context and question.
context: The passage or document with the answer or you would like to search
question: The question text you would like to answer.  

You should receive a json response with the answer text, character locations, and 
score.
