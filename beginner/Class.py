#little exercise for Class tyle in Python  
class Person(object):
    def __new__(cls,*args,**kw):
        print("call Person's__new__")
        print(args)
        return super(Person,cls).__new__(cls)
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'Person object : <%s>' %(self.name)
class Student(Person):
        hobby='I like Studying'
        def __new__(cls,*args,**kw):
            print("call Student's__new__")
            print(args)
            return super(Student,cls).__new__(cls)
        def __init__(self,name,gender,age,weight):
            super(Student, self).__init__(name)
            self.gender = gender
            self.age = age
            self.__weight = weight
        def __getattribute__(self,name):
            #return getattr(self,name)
            #return self.__dict__[name]
            return super(Student,self).__getattribute__(name)
        def __setattr__(self,name,value):
            #setattr(self,name,value)
            self.__dict__[name] = value
        @classmethod
        def get_hobby(cls):
            return cls.hobby
        @property
        def get_weight(self):
            return self.__weight
        def self_introduction(self):
            print ("I'm Student %s.%s"%(self.name,self.hobby))
        def __str__(self):
            return 'Student object : <%s>' %(self.name)

class Programmer(Student):
        def __new__(cls,*args,**kw):
            print("call Programmer's__new__")
            print(args)
            return super(Programmer,cls).__new__(cls)
        hobby='I love Programming'
        def __init__(self,name,gender,age,weight,language):
            super(Programmer,self).__init__(name,gender,age,weight)
            self.language = language
        def self_introduction(self):
            print ('I\'m Programmer %s.%s'%(self.name,self.hobby))
        def __str__(self):
            return 'Programmer object : <%s>:%ser' %(self.name,self.language)
        #def __dir__(self):
            #return self.__dict__.keys()
def introduce(className):
    if  isinstance(className,Programmer):
        className.self_introduction()
    elif isinstance(className,Student):
        className.self_introduction()
    else:
        print("I'm nothing")
if __name__ == '__main__':

    dili = Programmer('dili','male','22','70kg','Python')
    #jwm = Student('jiangwenmiao','female','21','40kg')
    #noone= Person('noone')
    #introduce(dili)
    #introduce(jwm)
    #introduce(noone)
    #print(dir(dili))
    #print(dili.__dict__)
    print(dili.name)
