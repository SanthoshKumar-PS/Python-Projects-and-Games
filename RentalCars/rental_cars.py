class CarDetails:
    def __init__(self,name,type,availability):
        self.name=name
        self.type=type
        self.availability=availability

class CarRental:
    def __init__(self,list):
        self.car_list=list

    def availablecars(self):
        print("Available cars are listed below-->")
        for car in self.car_list:
            if car.availability==True:
                print(car.name)
        print("\n")

    def rentcar(self,name):
        for car in self.car_list:
            if name==car.name:
                if car.availability:
                    car.availability=False
                    print(f"You rented this '{car.name}'")
                    car.availability=False
                else:
                    print(f"'{car.name}' is not available. Please choose any available car")
        print("\n")


    def carreturn(self,name):
        if name not in self.car_list:
            print(f"{name} does not exist in our garage")
        for car in self.car_list:
            if car.name==name:
                car.availability=True
                print(f"You successfully returned {name} car")
        print("\n")
