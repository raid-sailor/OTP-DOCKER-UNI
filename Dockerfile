# This will pull the latest python image 
FROM python:latest
# This will put files at the image '/otp_python/' folder.

RUN apt-get update 

RUN apt-get install -y git

RUN git clone https://github.com/raid-sailor/OTP-DOCKER-UNI.git
# '/otp_python/' is the base directory
WORKDIR /OTP-DOCKER-UNI/
# Expose port 9898 in the container
EXPOSE 9898
# This will execute the command
CMD [ "python3", "server.py"]
