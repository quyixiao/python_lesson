import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, Enum, BigInteger
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_, not_

#
from sqlalchemy.ext.declarative import declarative_base
# 生产环境很少这样的创建表，都是系统上线的时候由脚本生成
# 生成环境很少的删除表，宁可废弃都不能删除
#
# url:jdbc:mysql://172.16.157.238:3306/linzi_biz?characterEncoding=utf-8&allowMultiQueries=true
# username:ldd_biz
# password:Hello1234

# connnet = 'mysql+?://username:pwd@ip:port/databasename?key=value'.format()
import logging
import enum
from sqlalchemy import func

connnet = '{}://{}:{}@{}:{}/{}'.format(
    'mysql+pymysql',
    'ldd_biz', 'Hello1234',
    '172.16.157.238', 3306,
    'test',
)

engine = create_engine(connnet, echo=True)  # 连接字符串
Base = declarative_base()  # 基类，元类


class Gender(enum.Enum):
    M = 'M'
    F = 'F'


class Employee(Base):
    __tablename__ = 'employees'  # 请指定表名

    emp_no = Column(Integer, primary_key=True)
    birth_date = Column(Date, nullable=False)
    first_name = Column(String(14), nullable=False)
    last_name = Column(String(16), nullable=False)
    gender = Column(Enum(Gender), nullable=False)
    hire_date = Column(Date, nullable=False)

    def __repr__(self):
        return "<Emp {} {} {} {} {} {} >".format(self.emp_no, self.birth_date,
                                                 self.first_name, self.last_name,
                                                 self.gender, self.hire_date)


def show(emps):
    for emp in emps:
        print(emp)


Session = sessionmaker(bind=engine)
print(type(Session))
session = Session()
print(type(session))

query = session.query(Employee).filter(Employee.emp_no > 1)
show(query)
print('----------func--------')
query = session.query(func.count(Employee.emp_no))
print(query.all()) # 返回的是一个list 元组
print('*'*100)
print(query.first()) # 也返回的是一个元组
print('*'*100)
print(query.one()) # one 返回的是一个元组
print('*'*100)
print(query.scalar()) # 有且只有一个的第一个元素


print('='*100)
query = session.query(func.sum(Employee.emp_no))
print(query.all()) # 返回的是一个list 元组
print('*'*100)
print(query.first()) # 也返回的是一个元组
print('*'*100)
print(query.one()) # one 返回的是一个元组
print('*'*100)
print(query.scalar()) # 有且只有一个的第一个元素
# 关联查询数据，一个部门可能有多个员工，这样就可以有一对多的关系，
# 在多对我的情况下，中间表关联起来，
# 从语句看出员工，部门之间的关系是多对多的关系。
#
query = session.query(Employee.gender,func.count(Employee.emp_no)).group_by(Employee.gender)
print(query.all())

