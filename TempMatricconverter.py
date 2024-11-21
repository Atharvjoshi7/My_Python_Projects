print("Welcome to Temp converter Type 1 for celsius to fahrenheit and 2 for fahrenheit to celsius.")
choice = int(input("Type your choice (1 or 2): "))
temp = float(input("What is the Temperature in celsius/fahrenheit: "))

if(choice == 2):
    def Farconverter(num):
        return (num-32) / 1.8
    print(f"The temperature in Celsius is : {Farconverter(temp)}")
elif(choice == 1):
    def Celsiusconverter(num):
        return (num * 1.8) + 32
    print(f"The temperature in fahrenheit is: {Celsiusconverter(temp)}")
else:
    print("Invalid choice! Please type 1 or 2.")
