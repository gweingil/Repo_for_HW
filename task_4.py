class Car:
    def __init__(self, speed, colour, name, is_police=False):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Go")

    def stop(self):
        print('Stop')

    def turn(self, direction):
        print(f'Car turn to {direction}')

    def show_speed(self):
        print(f'Current speed is {self.speed}')

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Speed limit violated!')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Speed limit violated!')

class PoliceCar(Car):
    def __init__(self, speed, colour, name):
        super().__init__(speed, colour, name, True)

town = TownCar(70, "black", "Town")
sport = SportCar(130, "yellow", "Sport")
work = WorkCar(40, "red", "Work")
police = PoliceCar(90, "blue", "Police")

town.show_speed()
work.show_speed()

work.speed = 35
work.show_speed()

police.turn('Right')