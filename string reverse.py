input_string="I hope you enjoy this task"
output_string=""
length=len(input_string)
for i in range(0,(length)):
    output_string=(input_string[i]+output_string)
print(output_string) 
