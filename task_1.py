from time import sleep

class Trafficlight:
    colours = ('red', 'yellow', 'green')
    delay = (7, 2, 6)

    def __init__(self):
        self.__colour = 'green'

    def running(self):
        while True:
            for i in self.colours:
                self.__colour = i
                print(self.__colour)
                sleep(self.delay[self.colours.index(self.__colour)])


traffic_light = Trafficlight()
traffic_light.running()
