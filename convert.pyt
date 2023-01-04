Weight = float(input("Weight: ")) #float so the weight number will be as decimal number
Unit = input("(K)g or (L)bs: ")
if Unit.upper () == "L": #upper to capitalize whatever letter was input
    converted = Weight * 0.45
    print("Weight in Kgs: " + str(converted)) #change converted to string cuz "weight in lbs" is also string so they can combine together
elif Unit.upper () == "K":
    converted = Weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    print("wrong input")