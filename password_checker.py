import re
import random
import string

def check_password_strength(password):
    score=0

    if len(password) >=8:
        score+=1

    if re.search("[A-Z]",password):
        score+=1
    if re.search("[a-z]",password):
        score+=1
    if re.search("[0-9]",password):
        score+=1
    
    if score <=2:
        return "weak password ❌"
    if score <=4:
        return "medium password ⚠️"
    else:
        return"strong password ✅"
    
def suggest_password(length=12):
    characters=string.ascii_letters+string.digits+"@#$%^&*!"
    password=""

    for i in range(length):
        password+=random.choice(characters)

    return password 

def estimate_crack_time(password):
    charset_size=0

    if re.search("[a-z]",password):
        charset_size+=26
    if re.search("[A-Z]",password):
        charset_size+=26
    if re.search("[0-9]",password):
        charset_size+=10
    if re.search("[@#$%^&*!]",password):
        charset_size+=8

    combinations=charset_size**len(password)

    guess_per_second=1_000_000_000

    seconds=combinations/guess_per_second

    if seconds<60:
        return f"{int(seconds)}seconds"
    if seconds<3600:
        return f"{int(seconds/60)}seconds"
    if seconds<86400:
        return f"{int(seconds)/3600}seconds"
    elif seconds<31536000:
        return f"{int(seconds/86400)}days"
    else:
        return f"{int(seconds/31536000)}years"
