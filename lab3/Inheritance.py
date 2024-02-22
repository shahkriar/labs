 class Student(Person):
 
 class Person:
   def __init__(self, fname):
     self.firstname = fname

   def printname(self):
     print(self.firstname)

 class Student(Person):
   pass

 x = Student("Mike")
<<<<<<< HEAD
 x.printname()
=======
 x.printname()
>>>>>>> 071fb93323d181712389aba4ba9937d5011ddcd2
