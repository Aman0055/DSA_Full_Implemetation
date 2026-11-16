# suare of the no :
squares = []
for i in range(1,6):
    squares.append(i ** 2)
print(f"The square of the number from the range 1 to 6 : {squares}")

# take a different exaple of locker : 
attempts , correct_pin, entered_pin = 0 , "4312", ["1111", "1265", "4312"]
while attempts < 3:
    pin = entered_pin[attempts]
    attempts += 1
    if pin == correct_pin:
        print(f"Attempts :{attempts}, pin entered ;{pin}, correct pin")
        break
    else:
        print(f"Kindly entered a correct pin, mentioned pin : {pin}, has incorrect with no of attempts :{attempts}")
else :
    print("Maximum attempt failed ! device locked !")
        
