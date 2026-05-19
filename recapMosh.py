name = input("What is you name? ")
print("Hello "+name)  #concatenation
birth_year=input("Enter your birth year: ")
#age = 2026 - birth_year (wrong as cannot subract string from integer)
age = 2026 - int(birth_year)
#print("Your age is "+age) wrong as cannot concatenate int with str, possible when both str
print("My age is "+str(age)) 
#python cannot concatenate float and string,convert float to string by str(float) 
course="Python for Beginners"
print(course.upper()) #over course is the object and upper is the method(mathods are like finctions)
print(course) #when run we see this dont change meaning method make another str didnt change original
print(course.find('n')) #find method returns index of the character
print(course.find('N')) #n is present but as python is case-sensitive so returns -1(false)
print(course.replace('for','4'))
#strings are immutable so methods create new str not changing original
print('Python' in course) #in is the keyword known as in operator returns boolean result like True 
# ARITHEMETIC: (10/3=3.33)gives float,(10//3=3)gives int, (10%3=1)gives remainder,(5**2=25)power
# COMPARISON OPERATORS: ==,<,>=,!= all give boolean results
# LOGICAL OPERATORS: and , or , not : all gives boolean results
price = 5
print(price>1 and price<10) # True
print(price>5 or price<10)  # True
print(not 5)                # False 
temp=int(input("Enter temperature: "))
if (temp>30):
    print("It's a hot day.")
    print("Have plenty of water.")
elif (temp>20):
    print("Perfect day to travel.")
else :
    print("It's cold be careful.") 
# WHILE LOOPS:
i=5              # initialisation
while (i>=1):    # condition
    print(i*"*") #this is not concatenating number*str means str will be number times
    i-=1         # updatation  
# LIST is a built-in Python data type used to store multiple items in a single variable.
# Key Features: It is ORDERED (keeps track of position), CHANGEABLE (items can be added/removed)
names= ["John","Bob","Mosh","Sam","Hary"]
print(names[-2]) #starts with index 0 but -ve works from backward, -2 means Sam
print(names[0:2]) #prints from index 0 till (2-1) index
names[2]="Sohel"
print(names) #since lists are mutable so Mosh is changed to Sohel
names.append("Zeya") #adds after the last index
names.insert(2, "Mosh") #adds at the given index
names.remove("Bob") #delete that item from list, to delete all use clear function
print(names)
print("Zeya" in names) #this give boolean results 
print(len(names)) #gives exact length no worry of index
for item in names: #for loops to iterate all the names without qutation and square bracket
    print(item)
numbers = range(1 ,10 , 2) #range has number from 1 to (10-1) which is 9
for item in numbers:
    print(item)