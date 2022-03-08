# OTP-DOCKER-UNI
A OTP password creator which will send the OTP through a TCP connection. 

- Step 1 - cd into the OTP-DOCKER-UNI folder and run: `docker build -t <NAME> .`

- Step 2 - run `docker run -p 9898:9898 <NAME>` 

- Step 3 - open a new terminal within the OTP-DOCKER-UNI folder and run `python3 client.py`
