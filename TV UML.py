class TV:
    def __init__(self):
        self.channel = 1
        self.volumelevel = 1
        self.on = False
    #Indicate the TV is on/off
        #Turns on Tv
    def turnOn(self):
        self.on=True
    #Turns off Tv
    def turnOff(self):
        self.on=False
    #return channel
    def getChannel(self):
        return self.channel
    #Channel (1 to 120)
    def setChannel(self,num):
        if num>=1 and num<=120:
            self.channel=num
    #return volume          
    def getVolume(self):
        return self.volumeLevel
        
#new channel
#gets volume

#sets a new volume

#increases channel 
#descreases channel

#increases volume
#decreases volume