# pydomoticz
Python class to communicate with domoticz using the API. Can work with and without the basic authentication. Currently has support to read and set lights (dimmable) on KaKu, MyLight and ZWave.

Example:
```python
from domoticz import Domoticz
pydo = Domoticz('user:pass@192.168.0.1:8080')# the IP and port of your Domoticz server
pydo.readDevice(42)
```
