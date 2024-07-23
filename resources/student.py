from flask_restful import Resource, reqparse, abort
from models import db, Student

student_put_args = reqparse.RequestParser()
student_put_args.add_argument('name', type=str, help='Name is required', required=True)
student_put_args.add_argument('age', type=int, help='Age is required', required=True)
student_put_args.add_argument('gender', type=str, help='Gender is required', required=True)
student_put_args.add_argument('student_id', type=int, help='Student ID is required', required=True)
student_put_args.add_argument('year', type=str, help='Year is required', required=True)

def abort_if_student_exists(human_id):
    student = Student.query.get(human_id)
    if student:
        abort(409, message=f'Student with ID {human_id} already exists.')

def abort_if_student_not_exists(human_id):
    student = Student.query.get(human_id)
    if not student:
        abort(404, message=f'Student with ID {human_id} not found.')

class StudentApi(Resource):
    def put(self, human_id):
        abort_if_student_exists(human_id)
        args = student_put_args.parse_args()
        student = Student(id=human_id, name=args['name'], age=args['age'], gender=args['gender'], student_id=args['student_id'], year=args['year'])
        db.session.add(student)
        db.session.commit()
        return {"message": "Student added successfully."}, 201

    def get(self, human_id):
        abort_if_student_not_exists(human_id)
        student = Student.query.get(human_id)
        return {
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "gender": student.gender,
            "student_id": student.student_id,
            "year": student.year
        }, 200
    
    def delete(self, human_id):
        abort_if_student_not_exists(human_id)
        student = Student.query.get(human_id)
        db.session.delete(student)
        db.session.commit()
        return {"message": "Student deleted successfully"}, 204


