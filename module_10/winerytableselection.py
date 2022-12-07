import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "winery_user",
    "password": "wine",
    "host": "127.0.0.1",
    "database": "winery",
    "raise_on_warnings": False
}

try:
    db = mysql.connector.connect(**config)
    
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    cursor = db.cursor()
    
    cursor.execute("SELECT * FROM wine")
    
    wines = cursor.fetchall()
    
    print("\n-- DISPLAYING Wine RECORDS --")
    
    for wine in wines:
        print("Wine ID: {}\nWine Type: {}\n".format(wine[0], wine[1]))
        
    cursor.execute("SELECT * FROM distributor")
    
    distributors = cursor.fetchall()
    
    print("\n-- DISPLAYING Distributor RECORDS --")
    
    for distributor in distributors:
        print("Distributor ID: {}\nDistributor Name: {}\nWine ID: {}\nCases Sold: {}\n\n".format(distributor[0], distributor[1], distributor[2], distributor[3]))
        
    cursor.execute("SELECT * FROM supplies")
    
    supplies = cursor.fetchall()
    
    print("\n-- DISPLAYING Supplies RECORDS --")
    
    for supply in supplies:
        print("Supply ID: {}\nSupply Name: {}\n\n".format(supply[0], supply[1]))
        
    cursor.execute("SELECT * FROM supplier")
    
    suppliers = cursor.fetchall()
    
    print("\n-- DISPLAYING Supplier RECORDS --")
    
    for supplier in suppliers:
        print("Supplier ID: {}\nSupplier Name: {}\nSupply ID: {}\n\n".format(supplier[0], supplier[1], supplier[2]))
        
    cursor.execute("SELECT * FROM delivery")
    
    deliveries = cursor.fetchall()
    
    print("\n-- DISPLAYING Delivery RECORDS --")
    
    for delivery in deliveries:
        print("Delivery ID: {}\nSupplier ID: {}\nExpected Date: {}\nActual Date: {}\n\n".format(delivery[0], delivery[1], delivery[2], delivery[3]))
        
    cursor.execute("SELECT * FROM employee")
    
    employees = cursor.fetchall()
    
    print("\n-- DISPLAYING Employee RECORDS --")
    
    for employee in employees:
        print("Employee ID: {}\nEmployee Name: {}\nEmployee Role: {}\n".format(employee[0], employee[1], employee[2]))
        
    cursor.execute("SELECT * FROM quarters")
    
    quarters = cursor.fetchall()
    
    print("\n-- DISPLAYING Quarters RECORDS --")
    
    for quarter in quarters:
        print("Quarter ID: {}\n".format(quarter[0]))
        
    cursor.execute("SELECT * FROM hours")
    
    hours = cursor.fetchall()
    
    print("\n-- DISPLAYING Hours RECORDS --")
    
    for hour in hours:
        print("Employee ID: {}\nQuarter ID: {}\nHours: {}\n".format(hour[0], hour[1], hour[2]))

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