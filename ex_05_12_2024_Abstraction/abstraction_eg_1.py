from abc import ABC , abstractmethod

class Gear_box(ABC):

    @abstractmethod
    def set_gear(self):
        pass

class Engine(Gear_box):

    @abstractmethod
    def start(self):
        pass
        #super().set_gear()

    @abstractmethod
    def stop(self):
        pass

class Car(Engine):

    def start(self):
        print("Car is starting")


    def stop(self):
        print("car is stopping")

    def set_gear(self):
        print("gearbox is ready")


obj_car = Car()
obj_car.start()
obj_car.set_gear()
obj_car.stop()