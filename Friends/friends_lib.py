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

    def if_table_friends_exists(self, username):
        
        self.crs.execute('''show tables;''')
        
        table_list = []
        for table_name in self.crs:
            table_list.append(table_name[0])

        if(("friends_" + username) in table_list):
            return True
        else:
            return False
        
    def if_table_requests_exists(self, username):
        
        self.crs.execute('''show tables;''')
        
        table_list = []
        for table_name in self.crs:
            table_list.append(table_name[0])

        if(("requests_" + username) in table_list):
            return True
        else:
            return False
        
    def create_table_friends(self, username):
        self.crs.execute(f'''create table friends_{username}(friends varchar(150));''')
        
    def create_table_requests(self, username):
        self.crs.execute(f'''create table requests_{username}(requests varchar(150));''')

    def delete_table_friends(self, username):
        self.crs.execute(f'''drop table friends_{username}''')

    def delete_table_requests(self, username):
        self.crs.execute(f'''drop table requests_{username}''')

    def pull_friends(self, username):
        
        self.crs.execute(f'''select friends from friends_{username};''')
        
        friend_list = []
        for friend in self.crs:
            friend_list.append(friend[0])

        return friend_list
    
    def pull_requests(self, username):
        
        self.crs.execute(f'''select requests from requests_{username};''')
        
        request_list = []
        for request in self.crs:
            request_list.append(request[0])

        return request_list
    
    def if_user_exists(self, username):
        
        self.crs.execute(f'''select username from auth_user where username="{username}"''')

        for username in self.crs:
            return True
        else:
            return False
        
    def if_request_already_send(self, source_user, destination_user):
        
        self.crs.execute(f'''select * from requests_{destination_user} where requests = "{source_user}";''')

        for request in self.crs:
            return True
        else:
            return False
        
    def if_incoming_request_exists(self, source_user, destination_user):
        
        self.crs.execute(f'''select * from requests_{source_user} where requests = "{destination_user}";''')

        for request in self.crs:
            return True
        else:
            return False
        
    def if_already_friends(self, source_user, destination_user):
        
        self.crs.execute(f'''select * from friends_{destination_user} where friends = "{source_user}"''')

        for friend in self.crs:
            return True
        else:
            return False
    
    def send_friend_request(self, source_user, destination_user):
        self.crs.execute(f'''insert into requests_{destination_user} values("{source_user}")''')

    def make_friends(self, source_user, destination_user):

        self.crs.execute(f'''delete from requests_{destination_user} where requests = "{source_user}";''')
        self.crs.execute(f'''insert into friends_{destination_user} values("{source_user}");''')
        self.crs.execute(f'''insert into friends_{source_user} values("{destination_user}");''')

    def reject_friend_request(self, source_user, destination_user):
        self.crs.execute(f'''delete from requests_{destination_user} where requests = "{source_user}";''')

    def remove_friend(self, user, target):
        self.crs.execute(f'''delete from friends_{user} where friends = "{target}";''')
        self.crs.execute(f'''delete from friends_{target} where friends = "{user}";''')

    def pull_dms(self, source_user, dest_user):
        
        if(source_user < dest_user):
            id = source_user + "_"  + dest_user
        else:
            id = dest_user + "_" + source_user 

        self.crs.execute(f'''select messages from dms where id = "{id}";''')

        record_list = []
        
        for data in self.crs:
            record_list.append(list(data)[0])

        return record_list
    
    def push_dm(self, source_user, dest_user, message):
        
        if(source_user < dest_user):
            id = source_user + "_"  + dest_user
        else:
            id = dest_user + "_" + source_user

        message = source_user + " : " + message

        self.crs.execute(f'''insert into dms values("{id}", "{message}");''')

    def clear_chat(self, source_user, dest_user):

        if(source_user < dest_user):
            id = source_user + "_"  + dest_user
        else:
            id = dest_user + "_" + source_user

        self.crs.execute(f'''delete from dms where id = "{id}";''')

    def close_connection(self):
        self.hdl.close()


def main():

    database = Database()

    # if(not database.if_table_friends_exists("amoghthusoo")):    
    #     database.create_table_friends("amoghthusoo")
    
    # if(not database.if_table_requests_exists("amoghthusoo")):
    #     database.create_table_requests("amoghthusoo")


    # database.delete_table_friends("test")
    # database.delete_table_requests("test")

    # out = database.pull_requests("amoghthusoo"); 
    # print(out)

    # out = database.if_user_exists("amoghthusoo")
    # print(out)

    # out = database.if_request_already_send("user9", "amoghthusoo")
    # print(out)

    # out = database.if_already_friends("user", "amoghthusoo")
    # print(out)

    # database.send_friend_request("user9", "amoghthusoo")
    
    # out = database.pull_dms("test", "amoghthusoo")
    # print(out)

    # database.push_dm("test", "amoghthusoo", "this is a message")

if(__name__ == "__main__"):
    main()