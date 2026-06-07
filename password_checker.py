import string

with open("10k-most-common.txt", "r") as f:
        common_password= [line.strip() for line in f]

def check_password(password):
    print("checking password:", password)
    score=0

    #checking length
    if len(password)<6:
        print("password is too short")
        return False
    
    if password.lower() in common_password:
        print("too common!")
        return False
    

    if len(password)<=11:
        score+=1
        print("password is okay but not great")
    else:
        score+=2
        print("password is of good length")

    #checking char. present 
    has_upper= any(c in string.ascii_uppercase for c in password)
    has_lower= any(c in string.ascii_lowercase for c in password)
    has_digit= any(c in string.digits for c in password)
    has_special= any(c in string.punctuation for c in password)

    checks=[(has_upper, "use an uppercase!"),
            (has_lower, "use a lowercase"),
            (has_digit, "use a digit"),
            (has_special, "use a special char")
            ]
    for condition, message in checks:
        if not condition:
            print(message)
             
        else:
          score+=1

    #scoring
    if score<=2:
        print("strength: weak")
        return False
    elif score<=5:
        print("strength: medium")
        return False
        
    else:
        print("strength: strong") 
        return True 


while True:
    password=input("enter the password: ")

    if check_password(password):
        break


