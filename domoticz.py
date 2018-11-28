''' Domoticz <3 Python
    V0.1
    This works via the JSON Api of Domoticz
    This hasn't been made to work with basic authentication or https
    https://www.domoticz.com/wiki/Domoticz_API/JSON_URL%27s
    Author: Korneel Wever / dippety.com
'''
import urllib, json, math

class Domoticz:
    def __init__(self, newhost):
        print 'Proper included'
        self.host = newhost
        self.url = 'http://' + self.host + '/json.htm?'


    # simple call handler
    def doJson(self, data):
        response = urllib.urlopen(self.url+data)
        return json.loads(response.read())

    # shortcut to update devices
    def updateDevice(self, id, nval=0, sval=0):
        update = 'type=command&param=udevice&idx='+str(id)+'&nvalue='+str(nval)+'&svalue='+str(sval)  # 24
        data = self.doJson(update)
        return data['status']

    # get latest device information
    def readDevice(self, id):
        read = 'type=devices&rid='+str(id)
        return self.doJson(read)

    def getSunRiseSet(self):
        return self.doJson('type=command&param=getSunRiseSet')

    # used for devices that are RGBWW / Mi-Light
    def setRGBdevice(self, id, color):
        return self.doJson('type=command&param=setcolbrightnessvalue&idx=' + str(id) + '&hex='+color)

    # off switch for lights
    def switchOff(self,idx):
        return self.doJson('type=command&param=switchlight&switchcmd=Off&idx='+str(idx))

    # on switch for lights
    def switchOn(self,idx):
        return self.doJson('type=command&param=switchlight&switchcmd=On&idx=' + str(idx))

    # set a light to a percentage
    def lightPercent(self,idx, percent):
        step = 0
        percent = int(percent);
        device = self.readDevice(idx)
        deviceType = device['result'][0]['Type'];
        # do logic for the level
        if deviceType == 'Lighting 2': # kaku device 0-32 steps
            print float(percent)/100
            step = math.ceil(32*(float(percent)/100))
        elif deviceType == 'Lighting Limitless/Applamp':
            step = percent+1 #milight etc has 100 steps. but it runs from 1 - 101
        else:
            print 'Don\t know this device type yet:'+deviceType
            return False

        # can not use updateDevice as the param is different.
        data = "type=command&param=switchlight&idx="+str(idx)+"&switchcmd=Set Level&level="+str(step)
        return self.doJson(data)