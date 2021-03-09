#!/usr/bin/python3

import secrets 
import string 

def password_generator(password_length):
    
    characters = string.ascii_letters + string.digits
    secure_password = ''.join(secrets.choice(characters) for i in range(password_length)) 

    return secure_password

#idade = input("Preencha sua Idade")
#nome = input("What's your name?")

#print ("%s tem %s", nome, idade)
if __name__ == '__main__':
    
   # a = input("DIGITE ALGO")
    user_pass_length = int(input("Digits number for pass: "))  
    print("Passoword Generated: ", password_generator(user_pass_length))

