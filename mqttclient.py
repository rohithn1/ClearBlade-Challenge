from clearblade.ClearBladeCore import System, Query, Developer, registerDev
import urllib.request, json, time

## New system with ClearBlade key and secret
systemKey = "SYSTEMKEY_HERE"
systemSecret = "SYSTEMSECRET_HERE"

mySystem = System(systemKey, systemSecret)

## New device with Clearblade active key and name
deviceName = "DEVICENAME_HERE"
deviceActiveKey = "ACTIVEKEY_HERE"
macDevice = mySystem.Device(deviceName, deviceActiveKey)
token = macDevice.token

## Using device to access messaging client
mqtt = mySystem.Messaging(macDevice, port=1883)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# subscribeTopic = "rohith-mac/1/requests"
# def on_connect(client, userdata, flags, rc):
# 	global subscribeTopic
# 	client.subscribe(subscribeTopic)

# incomingRequest = None

# def on_message(client, userdata, msg):
# 	global incomingRequest
# 	incomingRequest = (msg.payload).decode('utf-8')

# mqtt.on_connect = on_connect
# mqtt.on_message = on_message
# mqtt.connect()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Defining publish topic
publishTopic = "rohith-mac/1/cpu-raw"

## Fetching CPU data from local API via HTTP GET request in loop
## Data to be published as percentage
while True:
	try:
		with urllib.request.urlopen("http://localhost:8080/api/system-analysis?cpus=false&totalmem=true&freemem=true") as url:
		    data = json.loads(url.read().decode())
		    freeMemory = data["free_memory"][0]["freemem"]
		    totalMemory = data["total_memory"][0]["totalmem"]
		    print("~~~~~~"+str(freeMemory))
		    print("~~~~~~"+str(totalMemory))

		    ## Calculating percent of CPU memory usage
		    cpu_data_raw = str((freeMemory/totalMemory)*100)
		    print(cpu_data_raw)

		## Publishing memory usage % to 'cpu-raw' topic
		## To be subscribed by ClearBlade platform and stored in Collection
		mqtt.publish(publishTopic, cpu_data_raw)

		## Thread sleep for 1 second
		time.sleep(1)

	## Exit command via CTR C
	except KeyboardInterrupt: 
		mqtt.unsubscribe("requests")
		mqtt.disconnect()
		time.sleep(5)
		break
	
















