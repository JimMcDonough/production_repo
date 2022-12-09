# production_repo
clone repository

Download the SQuAD Training Set v2.0 (40mb) from https://rajpurkar.github.io/SQuAD-explorer/
and save it in your google drive.  

Create a working driectory on your google drive and create a model folder for saving 
your final trained model. Open Collab notebook.  It is recommended to purchase  
compute units to use a premium gpu.  Upload QA_utils.py script from cloned repository 
into your notebook.  Run the notebook to train the model.  Save to your model working 
directory.  

Copy model checkpoint files into your cloned repository "/full_saved_model/" directory.

Follow instruction on the link below and use the premade docker file and flask app
for the cloned repositiory to deploy the containerized application.  Recommend using 
someting larger than a t2.micro instance on AWS.  More memory is needed for installing 
all the library in the requirements.txt file.   
https://towardsdatascience.com/simple-way-to-deploy-machine-learning-models-to-cloud-fd58b771fdcf