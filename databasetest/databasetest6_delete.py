import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, Enum, BigInteger
from sqlalchemy.orm import sessionmaker

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





connnet = '{}://{}:{}@{}:{}/{}'.format(
    'mysql+pymysql',
    'ldd_biz', 'Hello1234',
    '172.16.157.238', 3306,
    'test',
)

engine = create_engine(connnet, echo=True)  # 连接字符串
Base = declarative_base()  # 基类，元类


class Student(Base):
    __tablename__ = 'ppl_student'  # 请指定表名

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column('username', String(64), nullable=False)

    age = Column(Integer)

    def __repr__(self):
        return "<Student {} {} {}> >".format(self.id, self.name, self.age)


Session = sessionmaker(bind=engine)
print(type(Session))
session = Session()
print(type(session))
# query方法将实体类传入，返回的类型是迭代对象，这个时候不查询，迭代它就执行SQL来查询数据库，封装数据到指定的类的实例
# get方法使用的是主键查询
# 如果要改的话，先从数据库中查询出来，需要改则改，如果不需要改就不改，

student =session.query(Student).get(7) # 主键查询方式

print(student)
print('-'*30)

try:
    session.delete(student)
    session.commit()
except Exception as e :
    print(e)
    session.rollback()



























