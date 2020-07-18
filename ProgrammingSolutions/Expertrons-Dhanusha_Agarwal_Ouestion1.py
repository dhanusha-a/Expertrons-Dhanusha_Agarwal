class InvalidInput(Exception):
    pass

if __name__=='__main__':
    n=input("Enter mobile number: ")    

    try:
        if(n.isdigit()):
            if(len(n)==10):
                if(n[0]=="7" or n[0]=="8" or n[0]=="9"):
                    print("Valid")
                else:                
                    raise InvalidInput
            else:
               raise InvalidInput
        else:
            raise InvalidInput
        
    except InvalidInput:
        print("Not Invalid")
