# Continuation of the What IF exercise

people = 30
cars = 45
buses = 15

if cars > people:
    print("We should take the cars.")
elif cars < people:                               # this will only be picked up if cars < people in this case 45 < 30
    print("We should not take the cars.")
else:                                             # this will only worked if both IF and ELIF doesnt satisfy the case
    print("We can't decide.")

if buses > cars:
    print("That's too many buses.")
elif buses < cars:
    print("Maybe we could take the buses.")
else:
    print("We still can't decide")

if people > buses:
    print("Alright, let's just take the buses.")
else:
    print("Fine, let's stay home then.")


# OUTPUT
# We should take the cars.
# Maybe we could take the buses.
# Alright, let's just take the buses.
