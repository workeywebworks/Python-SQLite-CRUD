def create(conn,data):
    
    qry='''INSERT INTO 
    tbl_students(student_id,student_name)
     VALUES(?,?)'''
    cur = conn.cursor()             
    cur.execute(qry,data)
 