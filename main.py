import pandas as pd
from Tools import *

Welcome_Message = '''
*********************
* Python Restaurant * 
* Information about Data       : 1 
* Executive Summary Method     : 2
* Peak Time and Branch Method  : 3
* Search Order Information     : 4
* Staff Report                 : 5
* Days Report                  : 6
* Manager Alerts (Low Rating)  : 7
* Exit                         : 0
*********************
'''

print(Welcome_Message)

while True:
    userInput = input("Enter a number: ").strip()

    if userInput == "1":
        print(columns_Data())
    elif userInput == "2":
        print(Summary_Data())
    elif userInput == "3":
        print(PeakTime_Branch())
    elif userInput == "4":
        Order = input("Enter Order Number: ").strip()
        print(Order_Info(Order))
    elif userInput == "5":
        print(staff_Performance())
    elif userInput == "6":
        print(Days_Report())
    elif userInput == "7":
        print(OrderReport())
    elif userInput == "0":
        print("Bye.. ")
        break
    else:
        print("\n⚠️ Invalid selection! Please enter a valid number from 0 to 7.")
        print(Welcome_Message)