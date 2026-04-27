"""
This is a game that will decypt ecrypt your code, and so people will have fun playing it.
"""

# We welcome user to the prgram and make a variable called name for the user to use.(start function)

# This function we will use a dictionary to make all the letters of the alphabet translate into numbers.
# We will also use keyword and value to make this work(ecrypt function )

# In this function we will take the dictionary that we made in the ecyrpt function and use .replace to decrypt the message.(decrypt function)

# main function 
# Its the main function that is looped and used in the game and calls all the other functions when needed.
# This function has four function options the first one is start that will help start the game. next is eycrpt that will give the unknown message.
# Then its decrypt that will take the unknown message and reviel it to the user. And last is exsit thats when the user can choose to leave the game.
# We add a break at the end where the loop stops to end the game.

def start():
    name = input("Heloo user welcome to the enigam machine game! What is your name user???: ").strip().title()
    
    print(f"Heloo {name}!")


def encrypt_yea():
    """This is where we are going to code down our big and boring dictionary!"""

    message = input("WHAT MESSAGE ENCRYOPT?: ").strip().lower()

    encrypt = {
    'a':'z',
    'b':'y',
    'c':'x',
    'd':'w',
    'e':'v',
    'f':'u',
    'g':'t',
    'h':'s',
    'i':'r',
    'j':'q',
    'k':'p',
    'l':'o',
    'm':'n',
    'n':'m',
    'o':'l',
    'p':'k',
    'q':'j',
    'r':'i',
    's':'h',
    't':'g',
    'u':'f',
    'v':'e',
    'w':'d',
    'x':'c',
    'y':'b',
    'z':'a',            

}
    
    for key in encrypt:
        message = message.replace(key, encrypt[key])
        print(f"Here is the encrypt message {message}")
        break



    
def decrypt_no():
    "This is where we are going to use the same dictionary from the start to decrypt the code"
    
    message = input("WHAT MESSAGE DECRYPT?: ").strip().lower()

   
    decrypt = {
    'a':'z',
    'b':'y',
    'c':'x',
    'd':'w',
    'e':'v',
    'f':'u',
    'g':'t',
    'h':'s',
    'i':'r',
    'j':'q',
    'k':'p',
    'l':'o',
    'm':'n',
    'n':'m',
    'o':'l',
    'p':'k',
    'q':'j',
    'r':'i',
    's':'h',
    't':'g',
    'u':'f',
    'v':'e',
    'w':'d',
    'x':'c',
    'y':'b',
    'z':'a',

}

    for key in decrypt:
        message = message.replace(key, decrypt[key])
        print(f"Here is the decrypt message {message}")

        break




def main():
    """main function that calls all his friends!"""
    start()
    
    while True:
        print("1- Encrypt")
        print("2- Decrypt")
        print("3- Exsit")

        choice = input("Choose one of the options above.")

        if choice == "1":
            encrypt_yea()

        elif choice == "2":
            decrypt_no()

        elif choice == "3":
            print("Thanks for playing HAHAHAHAHAHAHAHAHAHA!")
            break 
        
        else:
            print("INVALID INPUT SUCKERRRRRRRRR!")


# Run main function
if __name__== "__main__":
    main()

