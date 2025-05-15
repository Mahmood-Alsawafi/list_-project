first_number = int(input("please inter the first number: "))
second_number = int(input("please inter the second number: "))
operations = input("please enter the operations (+ - * /): ")
result = 0
if operations == "+":
    result = first_number + second_number 
elif operations== "/" and second_number >0:
      ruselt=first_number / second_number
else:
    print("there is some thing wronge ")


print(result)
print("very good")
