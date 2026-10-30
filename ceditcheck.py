import os,sqlite3
dbname=os.path.join(os.path.dirname(__file__),"attend.db")
conn=sqlite3.connect(dbname)
conn.row_factory=sqlite3.Row
c=conn.cursor()
userid=3
name=input("Enter your name ")
password=input("Enter password")
class update:
    def __init__(self,nam,passw):
        self.name=nam
        self.password=passw
    def userupdate(self):
        c.execute("""select * from users where id=?""",(userid,)) 
        listing=c.fetchone()
        if not self.name:
            self.name=listing["fullname"]
            return True,self.name  
        if not self.password:
            self.password=listing["password"]
            return True, self.password
        
u=update(name,password)
ok,msg=u.userupdate() 
print(msg)       
                
        
            
             
        