# fruit=['Apple','BANNA','Mango','Guava','Orange']
# print(fruit[0])
# print(fruit[-1])
# print(fruit[1:4])

# dict={}
# num=int(input("Enter the number of students: "))
# for i in range(0,num):
#     name=str(input("Enter the name student: "))
#     age=int(input("Enter the age student: "))
#     dict[name]=age
# for keys in dict.keys():
#     print(keys,':',dict[keys])

# name=str(input("Enter the name of new student: "))
# age=int(input("Enter the age student: "))
# dict[name]=age


# for keys in dict.keys():
#     print(keys,':',dict[keys])



def Duplicate(lst:list):
    dict={
    }
    for i in lst:
        dict[i]=0
    
    for i in lst:
        dict[i]+=1
    ret=[x for x in dict.keys() if dict[x]>1]
    return ret
lst=[1,1,2,3,4,4]
print(Duplicate(lst))