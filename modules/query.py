def select_single(conn,data):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tbl_students WHERE student_name='"+ data +"'")
    rows = cur.fetchall()
    for row in rows:
        print(row)
 
def select_all(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tbl_students")
    rows = cur.fetchall()
    for row in rows:
        print(row)
        
def edit(conn,name):
    cur = conn.cursor()
    cur.execute("UPDATE tbl_students SET  student_name='"+ 'John' +"' WHERE student_id=1")
    

def delete(conn,id):
    cur = conn.cursor()
    cur.execute("DELETE from tbl_students  WHERE student_id="+ id +"")
    
    