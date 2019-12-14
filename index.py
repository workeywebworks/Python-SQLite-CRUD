import modules.config as cfg
import modules.query as qry
import modules.insert as ist
  
if __name__ == '__main__':
    print("Receipt Name")
    print("-------------------")
    print("1] Add New Record")
    print("2] Search a record")
    print("3] Delete a record")
    
    choice=input("Please enter your choice here: ")
    print("You have entered: " + choice)
    if(choice=="1"):
        conn = cfg.create_connection(cfg.database)
        
        data=('12356','Sample Record')
        ist.create(conn,data)
        
        qry.select_all(conn)
        print("Record has been created successfully")
    if(choice=="2"):
        conn = cfg.create_connection(cfg.database)
        qry.select_all(conn)
        
        search = input("Please enter your search: ")
        qry.select_single(conn,search)
    else:    
        print("Wrong choice. Program will now exit")