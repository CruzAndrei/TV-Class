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
    #Volume (1 to 7)
    def setVolume(self,volumelevel):
        if volumelevel>=1 and volumelevel<=7:
            self.volumeLevel=volumelevel
    #increases channel 
    def channelUp(self):
        if self.channel<120:
            self.channel+=1
        else:
            self.channel=1
#descreases channel

#increases volume
#decreases volume