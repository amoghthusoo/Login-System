import mysql.connector as mc

class Database:

    def __init__(self, host = "localhost", user = "root", password = "root", database = "login_system", autocommit = True):
        
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.autocommit = autocommit
        self.hdl = mc.connect(host = self.host, user = self.user, password = self.password, database = self.database, autocommit = self.autocommit)
        self.crs = self.hdl.cursor()

    def push(self, message):
         
        self.crs.execute(f'''insert into messages values("{message}");''')

    def pull(self):
        
        self.crs.execute(f'''select * from messages''')
        record_list = []
        
        for data in self.crs:
            record_list.append(list(data))

        return record_list
    
def main():
    
    database = Database()
    # database.push("Hello, my name is amogh")

    record_list = database.pull()
    print(record_list)

if(__name__ == "__main__"):
    main()