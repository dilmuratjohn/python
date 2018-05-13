# Author:Colin

Name=input("name:")
Age=int(input("age:"))
print(type(Age))
Job=input("job:")
Salary=input("salary:")

info1='''
------- info of %s -------
Name:%s
Age:%d
Job:%s
Salary:%s
'''%(Name,Name,Age,Job,Salary)
print(info1)

info2='''
------- info2 of {_name} -------
Name:{_name}
Age:{_age}
Job:{_job}
Salary:{_salary}
'''.format(_name=Name,_age=Age,_job=Job,_salary=Salary)
print(info2)

info3 = '''
------- info3 of {0} -------
Name:{0}
Age:{1}
Job:{2}
Salary:{3}
'''.format(Name,Age,Job,Salary)
print(info3)