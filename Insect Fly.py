import FlyClass as F

wings = int(input("how many wings does the insect have?"))
legs = int(input("how many legs does the insect have?"))

#this is creating an instance of the insect class
mosquito = F.Insect(2,4)
housefly = F.Insect(3,6)

mosquito.flight_length()
housefly.flight_length()

print("The mosquito can fly up to", mosquito.get_miles(), "miles")
print("The housefly can fly up to", housefly.get_miles(), "miles")