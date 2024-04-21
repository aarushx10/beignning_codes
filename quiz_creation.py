print('                                      QUIZ ON PYTHON                  ')
score = 0 
guess=[]
questions=("1. Which of the following is the error raised when a wrong data value is given to the opertaor or a method: ")
options=("a) DataTypeError" , "b) Value Error" , "c) TypeError" , "d) None of the above ")
print(questions)
print(options)
guess = input("Enter option: ").lower()
if guess == "c":
    score += 1
    print("correct")
else:
    print("incorrect")
    print("correct answer is c")

print("----------------------------------------------------------------------")
questions =("2. What is the output of the code \n      raise: ")
options = ("a) SynatxError" , "b)'raise' ","c) NameError", "d) RuntimeError")
print(questions)
print(options)
guess = input("Enter option: ").lower()
if guess == "d":
    score += 1
    print("correct")
else:
    print("incorrect")
    print("correct answer is d")

print("----------------------------------------------------------------------")
questions =("3. An immutuable object is an object that can be changed after it is created: ")
options = ( "a) True" , "b) False")
print(questions)
print(options)
guess = input("Enter option: ").lower()
if guess == "b":
    score += 1
    print("correct")
else:
    print("incorrect")
    print("correct answer is b")

print("----------------------------------------------------------------------")
questions =("4. Python automatically stores byte code in files with a.pyc extension: ")
options =( "a) True" , "b) False ")
print(questions)
print(options)
guess = input("Enter option: ").lower()
if guess == "a":
    score += 1
    print("correct")
else:
    print("incorrect")
    print("correct answer is a")

print("----------------------------------------------------------------------")
percentage= (score*100)/4
print(f"{percentage}% questions are correct")





