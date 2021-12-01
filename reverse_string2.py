input_string="I hope you enjoy this task"
output_string=""
num1=0
length=len(input_string)
for i in input_string:
    num2=input_string.index(" ")
    output_string=input_string[num1:((num2)+1)]+output_string
    input_string=input_string[(num2+1):]
    print(output_string)




