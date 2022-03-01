#StockX: https://stockx.com/
#FootLocker: https://www.footlocker.com/
#FinishLine: https://www.finishline.com/
#GOAT: https://www.goat.com/
#Nike: https://www.nike.com/
#Adidas: https://www.adidas.com/us
#Nordstrom: https://www.nordstrom.com/
#Amazon: https://www.amazon.com/
#Ebay: https://www.ebay.com/

# Import the modules needed to run the script.
#Allow file to access all functions from look_up.py
import sys, os
from look_up import *

# Main definition - constants
menu_actions  = {}  

# =======================
#     MENUS FUNCTIONS
# =======================

# Main menu
def main_menu():
    os.system('clear')
    
    print ("\n             Find-A-Shoe\n")
    print ("Please Select The Website You Want To Search On:")
    print ('[1] StockX\n[2] FootLocker\n[3] Finish Line\n[4] GOAT\n[5] Nike\n[6] Adidas\n[7] DSW\n[8] Amazon\n[9] Ebay\n[10] ALL SITES')
    print ('\n[0] Back')
    print ("\n[00] Quit\n")
    print ('Type Your Selection: ')
     
    choice = input(" >>  ")
    exec_menu(choice)

    return

# Execute menu
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print ("Invalid selection, please try again.\n")
            menu_actions['main_menu']()
    return

# Menu 1 (StockX)
def menu1():
    print ("Welcome To The StockX Search!\n")
    search = input("What Shoe Do You Want To Look For?: ")
    OpenAndSearch_StockX(search)
    print ("/n[0] Back")
    print ("[00] Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return


# Menu 2 (FootLocker)
def menu2():
    print ("Welcome To The Foot Locker Search!\n")
    search = input("What Shoe Do You Want To Look For?: ")
    OpenAndSearch_FootLocker(search)
    print ("/n[0] Back")
    print ("[00] Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return

# Menu 3 (Finish Line)
def menu3():
    print ("Welcome To The Finish Line Search!\n")
    search = input("What Shoe Do You Want To Look For?: ")
    OpenAndSearch_Nike(search)
    print ("[0] Back")
    print ("[00] Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return

# Menu 4 (GOAT)
def menu4():
    print ("Welcome To The GOAT Search!\n")
    search = input("What Shoe Do You Want To Look For?: ")
    OpenAndSearch_Goat(search)
    print ("[0] Back")
    print ("[00] Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return

# Menu 5 (Nike)
def menu5():
    print ("Welcome To The Nike Search!\n")
    search = input("What Shoe Do You Want To Look For?: ")
    OpenAndSearch_Nike(search)
    print ("[0] Back")
    print ("[00] Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return

# Menu 6 (Adidas)
def menu6(): 
    print ("Welcome To The Adidas Search!\n")
    search = input("What Shoe Do You Want To Look For?: ")
    OpenAndSearch_Adidas(search)
    print ("[0] Back")
    print ("[00] Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return

# Menu 7 (DSW)
def menu7():
    print ("Welcome To The DSW Search!\n")
    search = input("What Shoe Do You Want To Look For?: ")
    OpenAndSearch_DSW(search)
    print ("[0] Back")
    print ("[00] Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return

# Menu 8 (Amazon)
def menu8():
    print ("Welcome To The Amazon Search!\n")
    search = input("What Shoe Do You Want To Look For?: ")
    OpenAndSearch_Amazon(search)
    print ("[0] Back")
    print ("[00] Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return

# Menu 9 (Ebay)
def menu9():
    print ("Welcome To The Ebay Search!\n")
    search = input("What Shoe Do You Want To Look For?: ")
    OpenAndSearch_Ebay(search)
    print ("[0] Back")
    print ("[00] Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return

# Menu 10 (ALL SITES)
def menu10():
    print ("Welcome To The All Site Search!\n")
    search = input("What Shoe Do You Want To Look For?: ")
    OpenAndSearch_All(search)
    print ("[0] Back")
    print ("[00] Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return



# Back to main menu
def back():
    menu_actions['main_menu']()

# Exit program
def exit():
    sys.exit()

# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': menu1,
    '2': menu2,
    '3': menu3,
    '4': menu4,
    '5': menu5,
    '6': menu6,
    '7': menu7,
    '8': menu8,
    '9': menu9,
    '10': menu10,
    '0': back,
    '00': exit,
}

# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()