def greet(first_name, last_name):
   print(f"Hello {first_name} {last_name}! You just developed into python")
a = input("Enter your first name: ")
b = input("Enter your last name: ")
if(len(a) and len(b) <=10):
   greet(a,b)
else:
   print("Your input is not within the specified constraintsI(first and last names each ≤ 10 characters)")