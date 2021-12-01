input_string="i hope you enjoy this task"
length=(len(input_string))
count=0
l=[]
for i in range(0,length):
    for j in range(0,length):

        if input_string[i]==input_string[j]:
           count+=1
           freq= (input_string[i],count)
    count=0

    l.append(freq)
print(l)