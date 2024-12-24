from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel

app=FastAPI()

@app.get('/')
def index():
  return {"name":"Hello WOrld"}


students={
  1:{
    "name":"john",
    "age":20,
    "class":"year 12"
  },
  2:{
    "name":"alfred",
    "age":19,
    "year":"year 11"
  }
}


class Student(BaseModel):
  name:str
  age:int
  year: str

class UpdateStudent(BaseModel):
  name:Optional[str]=None
  age:Optional[int]=None
  year:Optional[str]=None



# Getting Student by their ID -- Reading

@app.get("/get-student/{student_id}")
def student(student_id:int=Path(...,description="The ID of the student that you want to view",gt=0)):
  return students[student_id]

# Getting Student by their Name -- Reading
 
@app.get('/get-by-name/{student_id}')
def get_student_name(*,student_id:int,name:Optional[str]=None,test:int):
  for student_id in students:
    if students[student_id]['name']==name:
      return students[student_id]
    return {"Data":"Not Found"}
  
# Creating Student --- Creating
  
@app.post('/create_student/{student_id}')
def create_student(student_id:int,student:Student):
  if student_id in students:
    return {"Error":"Student Exsists"}
  students[student_id]=student.dict()
  return students[student_id]

# Updating Student Details---Updating


@app.put('/update-student/{student_id}')
def update_student(student_id:int,student:UpdateStudent):
  if student.name is not None:
      students[student_id]["name"] = student.name

  if student.age is not None:
      students[student_id]["age"] = student.age

  if student.year is not None:
      students[student_id]["year"] = student.year

  return students[student_id]


# Deleting 
@app.delete('/delete-student/{student_id}')
def delete_student(student_id:int):
  if student_id not in students:
    return {"Error":"Student does not exist"}
  del students[student_id]
  return {"message":"Student deleted Successfully"}