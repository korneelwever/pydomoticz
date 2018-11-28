# pydomoticz
Python class to communicate with domoticz

Example:
from domoticz import Domoticz
pydo = Domoticz('user:pass@192.168.0.1:8080')# the IP and port of your Domoticz server
pydo.readDevice(42)
