import sqlalchemy

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, Date, Enum, BigInteger
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import and_, or_, not_
from sqlalchemy.ext.declarative import declarative_base
# 生产环境很少这样的创建表，都是系统上线的时候由脚本生成
# 生成环境很少的删除表，宁可废弃都不能删除
# 第一种情况将数据
# 总结
# 在开发中，一般都会采用ORM框架，这样就可以使用对象操作了
# 定义表映射的类，使用Column的描述器定义类的属性，使用ForegnKey来定义外键约束
# 如果一个对象中，想查看其它的对应的对象的内容，就要使用relationshipg来定义
# 是否使用外键
# 嫌弃派
# 开发难度增加，大数据的时候影响插入，修改，删除的效率
# 在业务层保证数据的唯一性
# 完整代码
# 可以不使用外键约束
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

    departments = relationship('Dept_emp')

    def __repr__(self):
        return "<Emp {} {} {} {} {} {} {} >".format(self.emp_no, self.birth_date,
                                                 self.first_name, self.last_name,
                                                 self.gender, self.hire_date,
                                                 self.departments)


class Department(Base):
    __tablename__ = 'departments'  # 请指定表名
    dept_no = Column(String(32), primary_key=True)
    dept_name = Column(String(64), nullable=False)

    def __repr__(self):
        return "<Dept {} {}>".format(self.dept_no, self.dept_name)


class Dept_emp(Base):
    __tablename__ = 'dept_emp'  # 请指定表名
    emp_no = Column(Integer, ForeignKey('employees.emp_no'), primary_key=True)
    dept_no = Column(String(32), ForeignKey('departments.dept_no'), primary_key=True)
    from_date = Column(Date, nullable=False)
    to_date = Column(Date, nullable=False)

    def __repr__(self):
        return "<Dept_emp {} {} {} {} >".format(self.emp_no, self.dept_no,
                                                self.from_date, self.to_date)


def show(emps):
    for emp in emps:
        print(emp)


Session = sessionmaker(bind=engine)
print(type(Session))
session = Session()
print(type(session))
# 查询10010员工的所有的部门编号及员工信息

query = session.query(Employee,Dept_emp).filter(Employee.emp_no == 12)\
    .filter(Employee.emp_no == Dept_emp.emp_no)

print(query)
print(query.all())

print('*'*100)
query = session.query(Employee).join(Dept_emp).filter(Employee.emp_no == 12)\
    .filter(Employee.emp_no == Dept_emp.emp_no)

print(query)
print(query.all())

print(33333333,'*'*100)
query = session.query(Employee).join(Dept_emp,Employee.emp_no == Dept_emp.emp_no).filter(Employee.emp_no == 12)

print(query)
print(query.all())

print(44444444,'*'*100)
query = session.query(Employee).join(Dept_emp,Employee.emp_no == Dept_emp.emp_no)\
    .join(Department,Dept_emp.dept_no== Department.dept_no)\
    .filter(Employee.emp_no == 12)

print(query)
print(query.all())
#Base.metadata.create_all(engine)


