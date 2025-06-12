from day17_rental_cars import CarRental,CarDetails
from data import car_list

carrentallist=[]
for cars in car_list:
    carname=cars["name"]
    cartype=cars["type"]
    caravailable=cars["available"]
    car1=CarDetails(carname,cartype,caravailable)
    carrentallist.append(car1)

car1=CarRental(carrentallist)
while True:
    userinput=input("Enter to access cars (a-availablecars,b-rent,c=return): ")
    if userinput=='a':
        car1.availablecars()

    elif userinput=='b':
        rentin=input("Enter car name to rent? ")
        car1.rentcar(rentin)

    elif userinput=='c':
        retin=input("Enter car name to return? ")
        car1.carreturn(retin)

    elif userinput=="off":
        break



