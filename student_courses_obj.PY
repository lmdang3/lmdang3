# object oriented programming in py
# lams notes seems like a object acts as a schema similar to mongo db 

class Student:
    # this class holds the objects of the student who are created 
    def __init__ (self, name, age, grade):
        self.name = name 
        self.age = age 
        self.grade = grade # 0-100


    def get_grade(self):
        return self.grade

class Course:
    # this obj holds the data of the courses in which a student can be enrolled in along with the num of students and the name of the course 
    def __init__ (self,name ,max_students):
        self.name = name 
        self.max_students = max_students
        self.students = [] #  this array hold the number of student
        # self.is_active = False

    def add_student(self, student):
        if len(self.students) <= self.max_students: # basicaly checks the array to see if the number of student in the array does not go pass the max num of students 
            self.students.append(student) 
            return True
        return False

    def get_average_grade(self):
        value = 0 
        for student in self.students:
            value += student.get_grade()
        return value/len(self.students)



if __name__ == "__main__":

    s1 = Student("Lam",22,95)
    s2 = Student("Jane",20,100)
    s3 = Student("Goku",3,99)

    course1 = Course("Com Sci",2)
    course1.add_student(s1)
    course1.add_student(s2)
    course1.add_student(s3)
    print(course1.get_average_grade())
