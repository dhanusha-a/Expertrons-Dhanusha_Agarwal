import ast

#give input like [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
student=input("Input: ") 
student = ast.literal_eval(student)

student.sort(key=lambda x:x[1])
#print(student)

second_lowest=0

for i in range(0,len(student)):
    if (student[0][1]==student[i][1]):
        pass
    else:
        second_lowest=student[i][1]
        #print(student[i][1])
        break

second_lowest_student=[]

for i in student:
    if i[1]==second_lowest:
         second_lowest_student.append(i[0])


second_lowest_student.sort()
print(*second_lowest_student, sep="\n")
    

