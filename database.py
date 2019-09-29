import sqlite3
class Database:
    
    #step1 constructor to connect
    def __init__(self,name="db.sqlite3"):  #squlite3 is a type of database 1st time database is not made if we use it regulary then squlite3 will create
        self.con=sqlite3.connect(name)    # con contains the connection in fo between python code and databse
    
    #step2 query executes
    def run(self,query):                    #sql is a language of database
        try:
            self.con.execute(query)
            self.con.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def create_product_table(self):
        query ="""
        create table products(
            id integer primary key autoincrement,
            name text unique,
            price integer,
            qty integer
        )
        """        
        return self.run(query)
        
    def add(self,name,price,qty):
        query =f"""insert into products values(
            null, '{name}',{price},{qty}
            )"""
        return self.run(query)   

    def viewAll(self):
        query= "Select * from products"
        data=self.con.execute(query)
        return data.fetchall()
         
