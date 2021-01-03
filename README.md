# [ClearBlade](https://www.clearblade.com/)-Challenge

Project Description:
  > This project uses the [ClearBlade Platform](https://platform.clearblade.com/) and ClearBlade [Python SDK](https://github.com/ClearBlade/ClearBlade-Python-SDK) to develop a IoT solution for 
  monitoring/storing real time CPU analytics.
  
Steps to Running This Project:
  > 1. Clone Repo.
  > 2. 'node macbook-api.js' to start the API which acts as the IoT Device in this project by responding to GET requests with real-time 
  CPU data (query format is specified in macbook-api.js).
  > 3. 'python mqttclient.py' to start Python Client that GETs data from Node API on regular intervals and publishes them to global topic 
  on ClearBlade broker. Make sure to fill in your system key and secret. 
  > 4. Use ClearBlade system zip to import corresponding solution into ClearBlade or use Git Rep [here](https://github.com/rohithn1/test-system).
  
 (Node App: runs on Port 8080 by default)
