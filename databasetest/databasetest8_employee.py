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
print('----------and--------')
query = session.query(Employee).filter(Employee.emp_no > 12).filter(Employee.emp_no < 30)
show(query)
print('*' * 30)
query = session.query(Employee).filter((Employee.emp_no > 12) & (Employee.emp_no <= 40))
show(query)
print('*' * 30)

query = session.query(Employee).filter(and_(Employee.emp_no > 12, Employee.emp_no < 40))
show(query)
print('=' * 100)

print('---------------or------------------')
query = session.query(Employee).filter((Employee.emp_no < 20) | (Employee.emp_no >= 40))
show(query)
print('*' * 30)
query = session.query(Employee).filter(or_(Employee.emp_no < 20, Employee.emp_no >= 40))
show(query)
print('*' * 30)
query = session.query(Employee).filter(not_(Employee.emp_no < 20))
show(query)
print('*' * 30)
query = session.query(Employee).filter(~(Employee.emp_no < 20))
show(query)

print('---------------in------------------')
query = session.query(Employee).filter(Employee.emp_no.in_([30, 40]))
show(query)
print('*' * 100)
print('---------------not in------------------')
query = session.query(Employee).filter(~Employee.emp_no.in_([30, 40]))
show(query)
print('*' * 100)

print('--------------like------------------')
query = session.query(Employee).filter(Employee.emp_no.like('%30'))
show(query)
print('*' * 100)

print('--------------ilike---忽略大小写---------------')
query = session.query(Employee).filter(Employee.emp_no.ilike('%30'))
show(query)
print('*' * 100)

print('--------------order by ---------------')
query = session.query(Employee).order_by(Employee.emp_no.desc())
show(query)

print('-------------limit ---------------')
query = session.query(Employee).order_by(Employee.emp_no.desc()).limit(2)
show(query)




print('-------------offeset ---------------')
query = session.query(Employee).order_by(Employee.emp_no.desc()).offset(3)
show(query)


print('-------------all() ---------------')

query = session.query(Employee).filter(Employee.emp_no<20).order_by(Employee.emp_no.desc())
print(query,'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
print(query.all()) # 将满足结果的所有的返回回来,all的话，是直接得到所有的东西
print('*' * 100) #
print(query.first()) #
print('*' * 100)
print(query.one()) #这个方法，有且只有一个，如果多一个，少一个都抛出异常
#

print('-------------count ---------------')
query = session.query(Employee)
print(query.count()) # 结果集中的条数，这个东西返回的数据只有一个
print(len(list(query))) # 查找长度，下面返回的数据多
# 这个是所有的结果来了，现在的只有一部分数据来
# 中间有多少人跟我没有关系，
#
