from Aircraft import *
from Plane import *
from People import *
from Passenger import *
from Flight_trip import *

# do the simplest while loops -
# switch board
while True:
    print("-----------------------WELCOME TO THE AIRPORT-----------------------")
    print("Enter a number from the menu below.                                |")
    print("1) For create a passenger.                                         |")
    print("2) For create a plane.                                             |")
    print("3) For create a flight trip.                                       |")
    print("4) For help.                                                       |")
    print("If you wish to leave the airport input a non-listed number.        |")
    user_input = str(input("Enter a number:                                                    | \n ->").strip())
    # create if statement for input 1
    if user_input == '1':
        name = input("Enter your name: \n -> ")
        p_number = input("Enter your passport number: \n -> ")

    # # create if statement for input 2
    elif user_input == '2':
        pl_number = input("Enter your plane number: \n -> ")

    # # create if statement for input 3
    elif user_input == '3':
        origin = input("Enter your name: \n -> ")
        destination = input("Enter your passport number: \n -> ")
        passenger_input = input("Please enter name of whom will be on this flight: \n -> ")

    # # create if statement for input 4
    elif user_input == '4':
        print("----------Still Under Maintenance--------")
        exit = input('type back to exit: \n ->')
    # #write code to help guide user
    # elif user_input == 'Help':
    # #write code to allow user to quit
    elif user_input > '4':
        print("Goodbye, thanks for visiting the terminal!")
        break


