print("1 - Plus")
print("2 - Minus")
print("3 - Multiplikation")
print("4 - Division")
option = int(input("Wähle eine der 4 Rechenoptionen: "))

if(option in [1,2,3,4]):
    num1 = int(input("Nenne die erste Nummer: "))
    num2 = int(input("Nenne die zweite Nummer: "))

    if(option == 1):
        result = num1 + num2
    elif(option == 2):
        result = num1 - num2
    elif(option == 3):
        result = num1 * num2
    elif(option == 4):
        result = num1 // num2     

else:
    print("Geht nicht")

print("Das Resultat ist ", result)