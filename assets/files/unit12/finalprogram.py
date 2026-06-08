## Imports
import time

## Devices in stock and their base cost
devices = [
    ["PlayStation 1", 10],
    ["Sg Mega Drive", 15],
    ["Amiga Desktop", 20]
]

## Fee multiplication values

## 1.15 is the equivalent of 15% added to the total cost
## 1.1 is the equivalent of 10% added to the total cost
nonMemberFee = 1.15
memberFee = 1.1

## Helpers for more appealing design where needed

def inputConsole(inputData, clear = False):
    ## clear if we need to, same method as in menu
    if clear == True:
        print('\n' * 80)

    print("CONSOLE > ")
    outputData = input(inputData)

    outputConsole("Processing...", True)
    time.sleep(2)

    return outputData

def outputConsole(outputData, clear = False):
    ## clear if we need to, same method as in menu
    if clear == True:
        print('\n' * 80)

    print("CONSOLE > ")
    print(outputData)

def displayMenu():
    ## Print 80 new lines to "clear" the console
    ## actually clearing the console requires OS specific methods
    print('\n' * 80)
    print("""╔══════════════════════════════════════════════════════════════════════════════╗
║      |  _ \ / ___|  \/  | | |    ___   __ _ _ __   |_   _|__   ___ | |       ║
║      | | | | |   | |\/| | | |   / _ \ / _` | '_ \    | |/ _ \ / _ \| |       ║
║      | |_| | |___| |  | | | |__| (_) | (_| | | | |   | | (_) | (_) | |       ║
║      |____/ \____|_|  |_| |_____\___/ \__,_|_| |_|   |_|\___/ \___/|_|       ║
╚══════════════════════════════════════════════════════════════════════════════╝
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║  +-+---------------+-----+                                                   ║
║  |1| """ + devices[0][0] + """ | £""" + str(devices[0][1]) + """ |                                                   ║
║  +-+---------------+-----+                                                   ║
║  +-+---------------+-----+                                                   ║
║  |2| """ + devices[1][0] + """ | £""" + str(devices[1][1]) + """ |                                                   ║
║  +-+---------------+-----+                                                   ║
║  +-+---------------+-----+                                                   ║
║  |3| """ + devices[2][0] + """ | £""" + str(devices[2][1]) + """ |                                                   ║
║  +-+---------------+-----+                                                   ║
║                                                                              ║
║                                                                              ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝""")
    
def displayReceipt(device, initialCost, feeCost, finalCost, weeks, weeklyCost):
    ## Got to print 80 new lines to hide old text
    print('\n' * 80)

    ## Also need to convert the costs and weeks to string
    ## otherwise it will error out, dropping the user through
    ## the device not in list code

    print("""       |  _ \ / ___|  \/  |        
       | | | | |   | |\/| |        
       | |_| | |___| |  | |        
       |____/ \____|_|  |_|        
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                                   
""" + device + """          £""" + str(initialCost) + """
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                                   
TOTAL: £""" + str(finalCost) + """
WEEKLY: £""" + str(weeklyCost) + """
                                   
-----------------------------------
INITIAL: £""" + str(initialCost) + """
FEES: £""" + str(feeCost) + """
WEEKS: """ + str(weeks) + """
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
             THANK YOU             
                                   """)

def loanCalc(realChosenDevice):
    ## Ask the user for the total amount of weeks, also clear all the stuff from earlier
    ## so we can keep this calculation the focus
    weeks = int(inputConsole("Please input the number of weeks the loan is going to be: ", True))
    
    ## User gave an amount we can't do, ask again with extra context.
    while weeks > 52 or weeks < 1:
        weeks = int(input("\nPlease input a valid number of weeks (1 to 52) for how long the loan will be: "))
    
    ## Calculate the cost without fees, we'll determine that later, also round to 2 decimal points because this is money.
    initialCost = round(devices[realChosenDevice][1] * weeks, 2)


    member = inputConsole("Is the customer a member? Please enter Y or N: ", True).upper()
    
    ## User gave something we don't understand, ask again.
    while member != "Y" and member != "N":
        member = input("\nIs the customer a member? Please enter only Y or N: ").upper()

    if member == "Y":
        ## User said yes, so we use that initialCost from earlier with the memberFee, then round like money
        final = round(initialCost * memberFee, 2)
    else:
        ## User said no, so use initialCost from ealier with nonMemberFee, then round it
        final = round(initialCost * nonMemberFee, 2)

    ## Get the fee cost to show on the receipt, and rounding it into regular money
    feeCost = round(final - initialCost, 2)
    deviceName = devices[realChosenDevice][0]
    
    weeklyCost = final / weeks

    displayReceipt(deviceName, initialCost, feeCost, final, weeks, weeklyCost)


## Main Program
def main():
    ## Set loop default value
    loop = "Y"
    while loop == "Y":

        ## Explains itself..
        displayMenu()
        
        ## User has given us a number, need to check if we have that device in our list
        chosenDevice = int(inputConsole("Please input the number of your console in the list: "))
        
        ## Lists start with 0, but the user doesn't know that, so we take 1 away (so 1 is actually the first device).
        realChosenDevice = chosenDevice - 1

        try:
            ## If the input was right we'll go through the if statement, if not then we go through the exception, then we loop back to the start
            if devices[realChosenDevice]:
                ## Process calculation
                loanCalc(realChosenDevice)

                ## We finished loan calc, now to determined if the user wants to continue
                loop = input("Would you like to go back to the main menu? Y or N: ").upper()
                
                ## User put something other than Y or N, so we ask again until they do.
                while loop != "Y" and loop != "N":
                    loop = input("Please enter only Y or N, would you like to go back to the main menu?: ").upper()

        except:
            print("\nDevice not in list, please try again.")
            time.sleep(2)


    ## User said no to loop, so we wait a few seconds for them to see the goodbye, then close
    print("Goodbye") 
    time.sleep(3)  

## Start
if __name__ == "__main__":
    main()