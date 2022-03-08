# This will pull the latest python image 
FROM python:latest
# This will put files at the image '/server/' folder.
ADD server.py /OTP-DOCKER-UNI/
# '/OTP-DOCKER-UNI' is the base directory
WORKDIR //OTP-DOCKER-UNI/
# Expose port 9898 in the container
EXPOSE 9898
# This will execute the command
CMD [ "python3", "/OTP-DOCKER-UNI/server.py" ]