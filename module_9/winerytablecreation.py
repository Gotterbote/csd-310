import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "winery_user",
    "password": "winery",
    "host": "127.0.0.1",
    "port": "3307",
    "database": "winery",
    "raise_on_warnings": False
}

try:
    db = mysql.connector.connect(**config)
    
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    cursor = db.cursor()
    
    cursor.execute("DROP TABLE IF EXISTS hours;")
    
    cursor.execute("DROP TABLE IF EXISTS employee;")
    
    cursor.execute("DROP TABLE IF EXISTS quarters;")
    
    cursor.execute("DROP TABLE IF EXISTS delivery;")
    
    cursor.execute("DROP TABLE IF EXISTS supplier;")
    
    cursor.execute("DROP TABLE IF EXISTS supplies;")
    
    cursor.execute("DROP TABLE IF EXISTS distributor;")
    
    cursor.execute("DROP TABLE IF EXISTS wine;")
    
    cursor.execute("CREATE TABLE wine (Wine_ID INT NOT NULL AUTO_INCREMENT, Wine_type CHAR(200) NOT NULL, PRIMARY KEY(Wine_ID));")  
    
    cursor.execute("CREATE TABLE distributor (Distributor_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, Distributor_name CHAR(200), Wine_id INT NOT NULL, Cases_sold INT NOT NULL, FOREIGN KEY (Wine_id) REFERENCES wine(Wine_ID));")
    
    cursor.execute("CREATE TABLE supplies (Supply_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, Supply_name CHAR(200) NOT NULL);")
    
    cursor.execute("CREATE TABLE supplier (Supplier_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, Supplier_name CHAR(200) NOT NULL, Supply_id INT NOT NULL, FOREIGN KEY (Supply_id) REFERENCES supplies(Supply_id));")
    
    cursor.execute("CREATE TABLE delivery (Delivery_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, Supplier_id INT NOT NULL, Expected_date DATE NOT NULL, Actual_date DATE NOT NULL, FOREIGN KEY (Supplier_id) REFERENCES supplier(Supplier_id));")
    
    cursor.execute("CREATE TABLE quarters (Quarter_id INT NOT NULL PRIMARY KEY);")
    
    cursor.execute("CREATE TABLE employee (Employee_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, Employee_name CHAR(200) NOT NULL, Employee_role CHAR(200) NOT NULL);")
    
    cursor.execute("CREATE TABLE hours (Employee_id INT NOT NULL, Quarter_id INT NOT NULL, Hours int NOT NULL, FOREIGN KEY(Employee_id) REFERENCES employee(Employee_id), FOREIGN KEY(Quarter_id) REFERENCES quarters(Quarter_id));")
    
    cursor.execute("INSERT INTO wine (Wine_type) VALUES(%s);", ("Merlot",))
    
    db.commit()
    
    cursor.execute("INSERT INTO wine (Wine_type) VALUES(%s);", ("Cabernet",))
    
    db.commit()
    
    cursor.execute("INSERT INTO wine (Wine_type) VALUES(%s);", ("Chablis",))
    
    db.commit()
    
    cursor.execute("INSERT INTO wine (Wine_type) VALUES(%s);", ("Chardonnay",))
    
    db.commit()
    
    cursor.execute("INSERT INTO distributor (Distributor_name, Wine_id, Cases_sold) VALUES (%s,%s, %s);", ("Day Drinkers", 1, 230))
    
    db.commit()
 
    cursor.execute("INSERT INTO distributor (Distributor_name, Wine_id, Cases_sold) VALUES (%s,%s, %s);", ("Gilmores Spirits", 2, 510))
    
    db.commit()
 
    cursor.execute("INSERT INTO distributor (Distributor_name, Wine_id, Cases_sold) VALUES (%s,%s, %s);", ("Marks Bottle Mart", 3, 62))
    
    db.commit()
 
    cursor.execute("INSERT INTO distributor (Distributor_name, Wine_id, Cases_sold) VALUES (%s,%s, %s);", ("Get Smashed", 4, 130))
    
    db.commit()

    cursor.execute("INSERT INTO supplies (Supply_name) VALUES(%s);", ("Bottles",))
     
    db.commit()
    
    cursor.execute("INSERT INTO supplies (Supply_name) VALUES(%s);", ("Corks",))
    
    db.commit()

    cursor.execute("INSERT INTO supplies (Supply_name) VALUES(%s);", ("Labels",))
    
    db.commit()

    cursor.execute("INSERT INTO supplies (Supply_name) VALUES(%s);", ("Boxes",))
    
    db.commit()

    cursor.execute("INSERT INTO supplies (Supply_name) VALUES(%s);", ("Tubing",)) 
    
    db.commit()
 
    cursor.execute("INSERT INTO supplies (Supply_name) VALUES(%s);", ("Vats",))
    
    db.commit()
    
    cursor.execute("INSERT INTO supplier (Supplier_name, Supply_id) VALUES(%s, %s);", ("ABC Wine Supplies", 1))
    
    db.commit()

    cursor.execute("INSERT INTO supplier (Supplier_name, Supply_id) VALUES(%s, %s);", ("ABC Wine Supplies", 2))

    db.commit()

    cursor.execute("INSERT INTO supplier (Supplier_name, Supply_id) VALUES(%s, %s);", ("Top Notch Wine", 3))

    db.commit()

    cursor.execute("INSERT INTO supplier (Supplier_name, Supply_id) VALUES(%s, %s);", ("Top Notch Wine", 4))

    db.commit()

    cursor.execute("INSERT INTO supplier (Supplier_name, Supply_id) VALUES(%s, %s);", ("Wine Warehouse", 5))

    db.commit()

    cursor.execute("INSERT INTO supplier (Supplier_name, Supply_id) VALUES(%s, %s);", ("Wine Warehouse", 6))

    db.commit()

    cursor.execute("INSERT INTO delivery (Supplier_id, Expected_Date, Actual_Date) VALUES(%s, %s, %s);", (1, "2022-10-26", "2022-10-27",))
    
    db.commit()
 
    cursor.execute("INSERT INTO delivery (Supplier_id, Expected_Date, Actual_Date) VALUES(%s, %s, %s);", (3, "2022-10-28", "2022-10-30",))
    
    db.commit()
 
    cursor.execute("INSERT INTO delivery (Supplier_id, Expected_Date, Actual_Date) VALUES(%s, %s, %s);", (5, "2022-10-31", "2022-11-03",))
    
    db.commit()
 
    cursor.execute("INSERT INTO delivery (Supplier_id, Expected_Date, Actual_Date) VALUES(%s, %s, %s);", (6, "2022-11-05", "2022-11-05",))
    
    db.commit()
 
    cursor.execute("INSERT INTO delivery (Supplier_id, Expected_Date, Actual_Date) VALUES(%s, %s, %s);", (4, "2022-11-07", "2022-11-08",))
    
    db.commit()
 
    cursor.execute("INSERT INTO delivery (Supplier_id, Expected_Date, Actual_Date) VALUES(%s, %s, %s);", (2, "2022-11-11", "2022-11-13",))
    
    db.commit()
    
    cursor.execute("INSERT INTO quarters (Quarter_id) VALUES(%s);", (1,))
     
    db.commit()
    
    cursor.execute("INSERT INTO quarters (Quarter_id) VALUES(%s);", (2,))
    
    db.commit()
    
    cursor.execute("INSERT INTO quarters (Quarter_id) VALUES(%s);", (3,))
    
    db.commit()
    
    cursor.execute("INSERT INTO quarters (Quarter_id) VALUES(%s);", (4,))
    
    db.commit()
    
    cursor.execute("INSERT INTO employee (employee_name, employee_role) VALUES(%s,%s );", ("Jane Collins", "finances",))   
    
    db.commit()
    
    cursor.execute("INSERT INTO employee (employee_name, employee_role) VALUES(%s,%s );", ("Roz Murphy", "marketing",))   
    
    db.commit()
    
    cursor.execute("INSERT INTO employee (employee_name, employee_role) VALUES(%s,%s );", ("Bob Ulrich", "assistant",))   
    
    db.commit()
    
    cursor.execute("INSERT INTO employee (employee_name, employee_role) VALUES(%s,%s );", ("Henry Doyle", "production",))   
    
    db.commit()
    
    cursor.execute("INSERT INTO employee (employee_name, employee_role) VALUES(%s,%s );", ("Maria Costanza", "distribution",))   
    
    db.commit()
    
    cursor.execute("INSERT INTO employee (employee_name, employee_role) VALUES(%s,%s );", ("Stan Bacchus", "inventory manager",))   
    
    db.commit()
    
    cursor.execute("INSERT INTO hours (Employee_id, Quarter_id, Hours) Values(%s, %s, %s);", (1,1,200))
    
    db.commit()
 
    cursor.execute("INSERT INTO hours (Employee_id, Quarter_id, Hours) Values(%s, %s, %s);", (1,2,200))

    db.commit()
 
    cursor.execute("INSERT INTO hours (Employee_id, Quarter_id, Hours) Values(%s, %s, %s);", (1,3,200))
    
    db.commit()
 
    cursor.execute("INSERT INTO hours (Employee_id, Quarter_id, Hours) Values(%s, %s, %s);", (1,4,200))
    
    db.commit()
 
    cursor.execute("INSERT INTO hours (Employee_id, Quarter_id, Hours) Values(%s, %s, %s);", (2, 1, 300))
    
    db.commit()
 
    cursor.execute("INSERT INTO hours (Employee_id, Quarter_id, Hours) Values(%s, %s, %s);", (2, 2, 180))
    
    db.commit()
 
    cursor.execute("INSERT INTO hours (Employee_id, Quarter_id, Hours) Values(%s, %s, %s);", (2, 3, 175))
    
    db.commit()
 
    cursor.execute("INSERT INTO hours (Employee_id, Quarter_id, Hours) Values(%s, %s, %s);", (2, 4, 150))
    
    db.commit()
 
    cursor.execute("INSERT INTO hours (Employee_id, Quarter_id, Hours) Values(%s, %s, %s);", (3, 1, 350))
    
    db.commit()
 
    cursor.execute("INSERT INTO hours (Employee_id, Quarter_id, Hours) Values(%s, %s, %s);", (3, 2, 275))
    
    db.commit()
 
    cursor.execute("INSERT INTO hours (Employee_id, Quarter_id, Hours) Values(%s, %s, %s);", (3, 3, 350))
    
    db.commit()
 
    cursor.execute("INSERT INTO hours (Employee_id, Quarter_id, Hours) Values(%s, %s, %s);", (3, 4, 400))
    
    db.commit()
 
    cursor.execute("INSERT INTO hours (Employee_id, Quarter_id, Hours) Values(%s, %s, %s);", (4, 1, 450))
    
    db.commit()
 
    cursor.execute("INSERT INTO hours (Employee_id, Quarter_id, Hours) Values(%s, %s, %s);", (4, 2, 400))
    
    db.commit()
 
    cursor.execute("INSERT INTO hours (Employee_id, Quarter_id, Hours) Values(%s, %s, %s);", (4, 3, 200))
    
    db.commit()
 
    cursor.execute("INSERT INTO hours (Employee_id, Quarter_id, Hours) Values(%s, %s, %s);", (4, 4, 275))
    
    db.commit()
 
    cursor.execute("INSERT INTO hours (Employee_id, Quarter_id, Hours) Values(%s, %s, %s);", (5, 1, 500))
    
    db.commit()
 
    cursor.execute("INSERT INTO hours (Employee_id, Quarter_id, Hours) Values(%s, %s, %s);", (5, 2, 500))
    
    db.commit()
 
    cursor.execute("INSERT INTO hours (Employee_id, Quarter_id, Hours) Values(%s, %s, %s);", (5, 3, 500))
    
    db.commit()
 
    cursor.execute("INSERT INTO hours (Employee_id, Quarter_id, Hours) Values(%s, %s, %s);", (5, 4, 500))
    
    db.commit()
 
    cursor.execute("INSERT INTO hours (Employee_id, Quarter_id, Hours) Values(%s, %s, %s);", (6, 1, 430))
    
    db.commit()
 
    cursor.execute("INSERT INTO hours (Employee_id, Quarter_id, Hours) Values(%s, %s, %s);", (6, 2, 400))
    
    db.commit()
 
    cursor.execute("INSERT INTO hours (Employee_id, Quarter_id, Hours) Values(%s, %s, %s);", (6, 3, 390))
    
    db.commit()
 
    cursor.execute("INSERT INTO hours (Employee_id, Quarter_id, Hours) Values(%s, %s, %s);", (6, 4, 380))
    
    db.commit()

    input("\n\n  Press any key to continue...")
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")
        
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")
        
    else:
        print(err)
        
finally:
    db.close()