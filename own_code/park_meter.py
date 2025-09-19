'''
task is to create a park meter simulation in class
'''

# displaying text for user for input
print("Welcome to the Parking Meter Simulation")
print("You can enter these coins :")
print("$1.00 = 30 minutes")
print("$0.50 = 15 minutes")
print("$0.20 = 6 minutes")
print("$0.10 = 3 minutes")
print("Type stop to finish.")
minutes = 0
coin = ""
# decision for amount of coin show eqaul amount of time
while minutes < 60 and coin != "stop":
    coin = input("Enter coin or type stop : ")
    if coin == "$1.00":
        minutes = minutes + 30
    elif coin == "$0.50":
        minutes = minutes + 15
    elif coin == "$0.20":
        minutes = minutes + 6
    elif coin == "$0.10":
        minutes = minutes + 3
    elif coin != "stop":
        print("That is not a valid coin.")
print("You have", minutes, "time remaining.")
# in task a countdown needs to be applied in the code
print("Simulating parking countdown :")
time_left = minutes
while time_left > 0:
    print("Parking time remaining :", time_left, "minutes")
    time_left = time_left - 10
print("Time expired!")