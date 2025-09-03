# You are builidng a thermostat alert system. If device status is active & temp > 35 -> print "Alert! High temperature detected!".
# else, print "Temperature is normal."
# if device status is inactive, print "Device is inactive."

device_status = "active"
temperature = 36

if device_status == "active":
    if temperature > 35:
        print("Alert! High temperature detected!")
    else:
        print("Temperature is normal.")
else:
    print("Device is inactive.")
