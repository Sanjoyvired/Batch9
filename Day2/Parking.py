# Start of the program

#### getting the car details######
noOfCars = int(input("Please enter the no of Cars:"))
noOfHoursCars = int(input("Please enter the nof of hours for cars"))

#### getting the bike details######
noOfBikes = int(input("Please enter the no of bikes:"))
noOfHoursBikes = int(input("Please enter the nof of hours for bikes"))

# cash received by the parking lot owner
cashReceived = int(input("Please enter the cash received by end of the day"))
#####end of input section##############################################
####Hardcoding cars and bikes payment rates#####
rateOfPaymentCars = 50
rateOfPaymentBikes = 10
# calculating the payment received
carsPaymentTotal = noOfCars*noOfHoursCars*rateOfPaymentCars
bikesPaymentTotal = noOfBikes*noOfHoursBikes*rateOfPaymentBikes
####calculating Total Payment#######
totalPayment = carsPaymentTotal+bikesPaymentTotal

# validating with the cashin hand
###Calculating the difference####
difference = totalPayment-cashReceived
# Setting up the statements on difference value
if(difference == 0):
    print("all is well")
elif(difference > 0):
    print("auditing not succesful the payment differ by Rs."+str(difference))
else:
    print("auditing not succeful where the cashreceived is more than the total payment by Rs." + str(int(difference)))

print(type(difference))
