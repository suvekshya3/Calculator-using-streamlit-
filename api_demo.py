from fastapi import FastAPI

from db_helper import run_sql_query
app = FastAPI()
@app.get("/students")
def get_students(age: int = None,college: str = None):
    QUERY = "SELECT * FROM students where 1=1"
    if age:
        QUERY =QUERY + f" AND age={age}"
    if college:
        QUERY =QUERY + f" AND college='{college}'"
        
    results= run_sql_query(QUERY)
    return{"students_details": results}
@app.get("/students/{student_id}")
def get_single_student_record(student_id: int):
    QUERY = f"SELECT * FROM students WHERE id={student_id};"
    results= run_sql_query(QUERY)
    return{"data": results}
@app.post("/students")
def create_student(student: dict):
    name = student.get("name")
    age = student.get("age")
    college = student.get("college")
    SQL_QUERY = f"INSERT INTO students (name, age, college)VALUES ('{name}', {age}, '{college}');"
    run_sql_query(SQL_QUERY)
    return {"message": "Student record created successfully"}
@app.put("/students/{student_id}")
def update_record(student:dict):
    student_id = student.get("id")
    name = student.get("name")
    age = student.get("age")
    college = student.get("college")
    SQL_QUERY = f"UPDATE students SET name='{name}', age={age}, college='{college}' WHERE id={student_id};"
    run_sql_query(SQL_QUERY)
@app.delete("/students/{student_id}")
def delete_record(student_id: int):
    SQL_QUERY = f"DELETE FROM students WHERE id={student_id};"
    run_sql_query(SQL_QUERY)