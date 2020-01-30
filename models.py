from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/sample'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)



class Employee(db.Model):
    id  = db.Column("id",db.Integer(),primary_key=True)
    ename = db.Column("emp_name",db.String(50))
    adr = db.relationship('Address', backref='emp', uselist=True,
                          lazy=False,cascade='all,delete')

class Address(db.Model):
    id = db.Column("id", db.Integer(), primary_key=True)
    city = db.Column("city", db.String(50))
    eid = db.Column("emp_id",db.ForeignKey("employee.id"),
                    unique=False,nullable=False)

if __name__ == '__main__':
    db.create_all()

    e1 = Employee(id=101,ename='AAA')
    e2 = Employee(id=102, ename='BBB')
    db.session.add_all([e1,e2])
    db.session.commit()

    for item in range(1,11):
        ad1 = Address(id=item,city='Pune'+str(item))
        ad1.emp=e1
        db.session.add(ad1)
        db.session.commit()