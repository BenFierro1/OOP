import InsectClass as i

fly = i.Insect(4, 8, 0)

print(fly.get_wings())
print(fly.get_legs())

print("The insect can fly up to", str(fly.flight_length()), "miles.")
