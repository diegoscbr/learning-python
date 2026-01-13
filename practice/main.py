
###calculator app 
print("Running Calulator App...")
operators = ['+', '-', '/', '*']
print("OPERATORS:")
print(operators)


#get rid of whitespace
#sort
while(True):
    data = input()
    #remove whitespaces
    data = data.replace(" ", "")
    #check against key
    if "+" in data:
        operatorList =data.split("+")
        num1 = int(operatorList[0])
        num2 = int(operatorList[1])
        result = num1 + num2
    if "-" in data: 
        operatorList =data.split("-")
        num1 = int(operatorList[0])
        num2 = int(operatorList[1])
        result = num1 - num2
    if "/" in data:
        operatorList =data.split("/")
        num1 = int(operatorList[0])
        num2 = int(operatorList[1])
        result = num1 / num2
    if "*" in data: 
        operatorList =data.split("*")
        num1 = int(operatorList[0])
        num2 = int(operatorList[1])
        result = num1 * num2
    print(result)

    if data == "exit" or data == "quit":
        break


print("SEE YA LATER")