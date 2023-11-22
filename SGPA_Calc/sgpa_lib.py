import mysql.connector as mc

class SGPA:
    
    def calculate(self, credit_list : list, marks_list : list) -> float:
        
        size = len(credit_list)
        grade_point_list = []
        credit_point_list = []

        for marks in marks_list:

            if(marks >= 91):
                grade_point_list.append(10)
            
            elif(marks >= 81):
                grade_point_list.append(9)
            
            elif(marks >= 71):
                grade_point_list.append(8)

            elif(marks >= 61):
                grade_point_list.append(7)
            
            elif(marks >= 51):
                grade_point_list.append(6)
            
            elif(marks >= 45):
                grade_point_list.append(5)
            
            else:
                grade_point_list.append(0)


        i = 0
        while(i < size):
            
            credit_point_list.append(credit_list[i] * grade_point_list[i])
            i += 1

        sgpa = sum(credit_point_list)/sum(credit_list)

        return sgpa

class Database:

    def __init__(self, host = "localhost", user = "root", password = "root", database = "login_system", autocommit = True):
        
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.autocommit = autocommit
        self.hdl = mc.connect(host = self.host, user = self.user, password = self.password, database = self.database, autocommit = self.autocommit)
        self.crs = self.hdl.cursor()

    def push(self, username : str, semester : int, course_code : str, credits : str, marks : str, sgpa : float):
         
        self.crs.execute(f'''insert into sgpa values("{username}", {semester}, "{course_code}", "{credits}", "{marks}", {sgpa});''')

    def pull(self, username):
        
        self.crs.execute(f'''select * from sgpa where username = "{username}"''')
        record_list = []
        
        for data in self.crs:
            record_list.append(list(data))

        return record_list
        
        

def main():
    # obj = SGPA()
    # out = obj.calculate([3, 4, 4, 4, 1], [81, 94, 97, 96, 100])
    # print(out)

    obj = Database()
    # obj.push("amoghthusoo", 1, "CSE101", "4", "99", 10)
    out = obj.pull("amoghthusoo")

    print(out)

if(__name__ == "__main__"):
    main()