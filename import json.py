import json
employee_string='''
{ 
     "employees" : [
        {
            "userId":"rirani",
            "jobTitleName":"developer",
            "firstName":"Romin",
            "lastName":"Irani",
            "phoneNumber":"408-1234567"
        },
        {
            "userId":"nirani",
            "jobTitleName":"Developer",
            "firstName":"Neil",
            "lastName":"Irani",
            "phoneNumber":"408-1111111"
        },
        {
            "userId":"thanks",
            "jobTitleName":"program directory",
            "firstName":"tom",
            "lastName":"hanks",
            "phoneNumber":"408-2222222"
        }
    ]


}
'''
data=json.loads(employee_string)
print(type(data['employees']))
for person in data['employees']:
    print (person['firstName'])
    del person['phoneNumber']
new_string=json.dumps(data,indent=2
)
print (new_string)