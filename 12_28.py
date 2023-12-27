



class Student():
    def __init__(self , student_id , name , connection):
        self.student_id = student_id
        self.name = name
        self.course = {}
        self.connection = connection

    def student_exists(self , student_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM students WHERE student_id=?", (student_id,))
        return cursor.fetchone()[0] > 0

    def add_course(self , semester , course_code , course_name):
        if semester not in self.course:
            self.course[semester] = []

        # Check if the course already exists for the specified semester
        if any(course["code"] == course_code for course in self.course[semester]):
            return "Course already added for the specified semester."
        
        self.course[semester].append({"code":course_code , "name":course_name})

        # Save student information to the database using INSERT OR REPLACE
        cursor = self.connection.curosr()
        cursor.execute("INSERT OR REPLACE INTO students (student_id , name) VALUES (? , ?)" ,(self.student_id , self.name))

        # Save the course information to the database
        for course in self.course[semester]:
            cursor.execute("INSERT OR REPLACE INTO courses (self.student_id , semester , course_code , course_name) VALUES (? , ? ,? ,?)" , 
             (self.student_id , semester , course["code"] , course["name"]))
            
        cursor.commit()

        return "Course added successfully."
    

    


