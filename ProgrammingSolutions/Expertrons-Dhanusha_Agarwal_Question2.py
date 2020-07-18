def unique_list():
    size = input('Enter list size less than 10: ')
    if (size.isdigit() and int(size)<10):

        A=[]
        B=[]
        size=int(size)
        
        print("Enter values for list A")
        for i in range(0,size):
            A.append(input())


        print("Enter values for list B")
        for i in range(0,size):
            B.append(input())

        C=list(set().union(A,B))
            
        print(C)

    else:
        print("Try again")
        unique_list()


if __name__ == '__main__':
    unique_list()
    
