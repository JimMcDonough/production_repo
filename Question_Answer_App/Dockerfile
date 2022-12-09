FROM python:3.8.15-slim-buster
WORKDIR /Question_Answer_App
COPY requirements.txt  /Question_Answer_App/requirements.txt
RUN pip3 install -r requirements.txt
COPY . /Question_Answer_App
EXPOSE 80
ENTRYPOINT ["python", "app.py"]