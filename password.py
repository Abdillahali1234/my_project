import random
import string 


def create_password(lenght=8,complex1=False):
    list_passwd=[]
    if not complex1:
        while len(list_passwd)<lenght:
            uper_case_latter=random.choice(string.ascii_uppercase)
            lower_case_latter=random.choice(string.ascii_lowercase)
            digit=str(random.randint(0,10))
            spechiel_char=random.choice(string.punctuation)
            list_passwd.extend([uper_case_latter,lower_case_latter,digit,spechiel_char])
    else:
        while len(list_passwd)<lenght:
            uper_case_latter=random.choice(string.ascii_uppercase)
            lower_case_latter=random.choice(string.ascii_lowercase)
            digit=str(random.randint(0,10))
            list_passwd.extend([uper_case_latter,lower_case_latter,digit])
       
        if lenght%2==0:
            x=int(lenght/2)
        else:
            x=int(lenght/2)+1   
        list_passwd=list_passwd[0:x]
        while len(list_passwd)<lenght:
            spechiel_char=random.choice(string.punctuation)
            list_passwd.append(spechiel_char)    
    
    return "".join(list_passwd)      
print(create_password(9,complex1=True))