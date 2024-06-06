import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

print(sqlalchemy.__version__)

engine = create_engine('sqlite:///college.db', echo=True)
# print(engine.driver)

meta = MetaData()

students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('lastname', String)
)

meta.create_all(engine)

ins = students.insert().values(name='Tomek', lastname='Pierwszy')
conn = engine.connect()
result = conn.execute(ins)