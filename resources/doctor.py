from flask_restful import Resource, reqparse, abort
from models import db, Doctor

doctor_put_args = reqparse.RequestParser()
doctor_put_args.add_argument('name', type=str, help='Name is required', required=True)
doctor_put_args.add_argument('age', type=int, help='Age is required', required=True)
doctor_put_args.add_argument('gender', type=str, help='Gender is required', required=True)
doctor_put_args.add_argument('doctor_id', type=int, help='doctor ID is required', required=True)
doctor_put_args.add_argument('year', type=str, help='Year is required', required=True)

def abort_if_doctor_exists(human_id):
    doctor = Doctor.query.get(human_id)
    if doctor:
        abort(409, message=f'doctor with ID {human_id} already exists.')

def abort_if_doctor_not_exists(human_id):
    doctor = Doctor.query.get(human_id)
    if not doctor:
        abort(404, message=f'doctor with ID {human_id} not found.')

class DoctorApi(Resource):
    def put(self, human_id):
        abort_if_doctor_exists(human_id)
        args = doctor_put_args.parse_args()
        doctor = Doctor(id=human_id, name=args['name'], age=args['age'], gender=args['gender'], doctor_id=args['doctor_id'], year=args['year'])
        db.session.add(doctor)
        db.session.commit()
        return {"message": "doctor added successfully."}, 201

    def get(self, human_id):
        abort_if_doctor_not_exists(human_id)
        doctor = Doctor.query.get(human_id)
        return {
            "id": doctor.id,
            "name": doctor.name,
            "age": doctor.age,
            "gender": doctor.gender,
            "doctor_id": doctor.doctor_id,
            "year": doctor.year
        }, 200
    def delete(self, human_id):
        abort_if_doctor_not_exists(human_id)
        doctor = Doctor.query.get(human_id)
        db.session.delete(doctor)
        db.session.commit()
        return {"message": "doctor deleted successfully"}, 204