import sqlite3  
  
conn = sqlite3.connect('javatpoint.db')  
  
print ("created database successfully")  


conn.execute('''CREATE TABLE Employee2
       (ID INT PRIMARY KEY     NOT NULL, 
       NAME           TEXT    NOT NULL, 
       AGE            INT     NOT NULL, 
       ADDRESS        CHAR(50), 
       SALARY         INT);''') 

print("Table created successfully")  

conn.execute("INSERT INTO Employee2 (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Ajeet', 27, 'Delhi', 20000.00 )");  
  
conn.execute("INSERT INTO Employee2 (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 22, 'London', 25000.00 )");  
  
conn.execute("INSERT INTO Employee2 (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'Mark', 29, 'CA', 200000.00 )");  
  
conn.execute("INSERT INTO Employee2 (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Kanchan', 22, 'Ghaziabad ', 65000.00 )");  
  
conn.commit()  
print("Records inserted successfully")     



data = conn.execute("select * from Employee2");  
  
for row in data:  
   print("ID = ", row[0])  
   print("NAME = ", row[1])  
   print("ADDRESS = ", row[2])  
   print("SALARY = ", row[3]) 
  
conn.close();  