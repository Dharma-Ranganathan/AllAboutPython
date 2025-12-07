# student management 
from abc import ABC, abstractmethod 

class Main(ABC):
    
    @abstractmethod
    def addStudent(self):
        pass 
    
    @abstractmethod
    def updateStatus(self):
        pass
    
    @abstractmethod
    def removeStudent(self):
        pass
    
    @abstractmethod
    def updateMarks(self):
        pass 
    
    
class Student(Main):
    
    students = []
    
    def __init__(self,name,marks,status='idle'):
        self.name = name
        self.marks = marks
        self.status = status
        
        stud_obj = {
            'name' : self.name,
            'marks' : self.marks,
            'status': self.status
        }
        
        Student.students.insert(0, stud_obj)
        
    def show_students_list(self):
        for i,s in enumerate(Student.students,1):
            print(f'{i} - {s}')
            
    def addStudent(self,name,marks,status='idle'):
        self.__init__(name,marks,status)
    
    def removeStudent(self,name):
        for student in Student.students:
            if name == student['name']:
                #print(student)
                Student.students.remove(student)
                return 

    
    def updateStatus(self,name,status):
        for student in Student.students:
            if name == student['name']:
                #print(student)
                student['status'] = status
                return 
    
    def updateMarks(self,name,mark):
        for student in Student.students:
            if name == student['name']:
                #print(student)
                student['marks'] = mark
                return 
            
            
s1 = Student('dharma',62,'idle')
s1.addStudent('vj',70)
s1.show_students_list()
s1.removeStudent('dharma')
s1.show_students_list()
s1.updateMarks('vj',99)
s1.updateStatus('vj','done')
s1.show_students_list()
        
    
    
    
    
    
    
    
