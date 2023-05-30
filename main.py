from database import Database
from teacher import TeacherCRUD

db = Database("bolt://44.203.249.152:7687", "neo4j", "quarter-doorsteps-ways")
# db.drop_all()
teacher_db = TeacherCRUD(db)

teacher_db.create("Chris Lima", 1956, "189.052.396-66")

teacher = teacher_db.read("Chris Lima")
print(teacher)

teacher_db.update("Chris Lima", "162.052.777-77")

db.close()
