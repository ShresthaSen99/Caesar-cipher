from art import logo
print (logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', " ", "!","#","$","%","^","&","*","(",")",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'," ","!","#","$","%","^","&","*","(",")",]

should_continue = True
while should_continue :
     
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift= shift % 26 

    def encrpt (text,shift):
            new_en= ""
            for i in (text):
                finding_alpha = alphabet.index (i) 
                if direction == "encode":
                    finding_alpha += shift
                else:
                    finding_alpha -= shift
                new_alpha= alphabet[finding_alpha]
                # print (new_alpha)
                new_en += new_alpha
            print (f"Your {direction}d message is {new_en}")


    encrpt(text,shift)

    ask_user = input("Do you want to run this program again? yes/no \n")
    if ask_user == "no":
         should_continue = False
         print ("Thanks for choosing us!")
         
