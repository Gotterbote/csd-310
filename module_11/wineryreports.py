import mysql.connector
from mysql.connector import errorcode

db = ""
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
    
    cursor.execute("SELECT Supplier_name, Supply_name, Expected_date, Actual_date, DATEDIFF(Actual_date, Expected_date) AS DateDiff FROM delivery INNER JOIN supplier ON supplier.Supplier_id = delivery.Supplier_id INNER JOIN supplies ON supplies.Supply_id = supplier.Supply_id GROUP BY MONTH(Expected_date), delivery.Supplier_id")
    
    result1 = cursor.fetchall()
    
    print("\n-- Report 1 - Suppliers and Deliveries --")
    
    for record in result1:
        print("Supplier Name: {}\nSupply Name: {}\nExpected Date: {}\nActual Date: {}\nTime Gap: {}\n".format(record[0], record[1], record[2], record[3], record[4]))
        
    cursor.execute("SELECT Distributor_name, Wine_type, Cases_sold FROM distributor INNER JOIN wine ON wine.Wine_id = distributor.Wine_id ORDER BY Cases_sold ASC")
    
    result2 = cursor.fetchall()
    
    print("\n-- Report 2 - Distributors, Wine Types --")
    
    for record in result2:
        print("Distributor Name: {}\nWine Type: {}\nCases Sold: {}\n".format(record[0], record[1], record[2]))
        
    cursor.execute("SELECT quarters.Quarter_id, Employee_name, Employee_role, Hours FROM employee INNER JOIN hours ON employee.Employee_id = hours.Employee_id INNER JOIN quarters ON quarters.Quarter_id = hours.Quarter_id")

    result3 = cursor.fetchall()

    print("\n-- Report 3 - Employees, Hours --")

    for record in result3:
        print("Quarter: {}\nEmployee Name: {}\nEmployee Role: {}\nHours: {}\n".format(record[0], record[1], record[2], record[3]))

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