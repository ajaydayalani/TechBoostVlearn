from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from database import db

enrollment = db.Table('enrollment',
    db.Column('enrolled_course_id', db.Integer, db.ForeignKey('enrolled_courses.id'), primary_key=True),
)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    total_score = db.Column(db.Integer)
    user_role = db.relationship('UserRole', back_populates='user', uselist=False, cascade="all, delete, delete-orphan")
    enrolled_courses = db.relationship('EnrolledCourse', back_populates='user', cascade="all, delete-orphan")
    
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }
 
class UserRole(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    user = db.relationship('User', back_populates='user_role')
    role = db.relationship('Role', back_populates='user_roles')
 
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(255), unique=True)
    permissions = db.Column(db.Text)
    user_roles = db.relationship('UserRole', back_populates='role')

class EnrolledCourse(db.Model):
    __tablename__ = 'enrolled_courses'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    completion = db.Column(db.Float, nullable=False, default=0)
    user = db.relationship('User', back_populates='enrolled_courses')
 