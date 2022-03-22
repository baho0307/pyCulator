import re

#Simple Calculating Functions(for make this project easier):
def SimpleCalc(Float,float2,operator):

    #if the operator is equals to "*" ,do multiply(the others are similar):
    if operator == "*":
        return Float*float2
    elif operator == "/":
        return Float/float2
    elif operator == "+":
        return Float+float2
    elif operator == "-":
        return Float-float2

def ListEditor(operator,list):
    #Add to List by Index (index is equals to operator's index -1,value that to be added is equals to be calculated values)
    list.insert(list.index(operator) - 1, SimpleCalc(float(list[list.index(operator) - 1]),float(list[list.index(operator) + 1]), operator))

    #deleting the calculated values(there is two so we should delete them.Because we want one left.
    list.pop(list.index(operator) + 1)
    list.pop(list.index(operator) - 1)

    #deleting the operator from list to do the other calculations. If we don't the program'll be stuck in this operator.
    list.pop(list.index(operator))

def Calculate(value):
    #Commands That Seperates Numbers and Operators and Add These to a List:
    calcValues = re.findall('(\d+|[^ 0-9])', value)


    #The Loop Continues Until One Element Remains
    while len(calcValues) > 1:

        if "*" in calcValues:
            ListEditor("*",calcValues)

        elif "/" in calcValues:
            ListEditor("/",calcValues)

        elif "-" in calcValues :
            ListEditor("-",calcValues)

        elif "+" in calcValues:
            ListEditor("+",calcValues)

    #Result:
    result = calcValues[0]

    #The Condition That Deleting The ".0" of The Result:
    if int(result) == result:
        result= int(result)

    return result

#Getting Input:
calcInput = input("What Do You Want Me to Calculate?:\n")

#Printing Result:
print(calcInput,"=",Calculate(calcInput))