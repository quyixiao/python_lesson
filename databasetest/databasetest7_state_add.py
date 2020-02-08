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


def getstate(entity, i):
    insp = sqlalchemy.inspect(entity)
    state = "sessionid={} ,attached={} \n transient={},persistent={}\npending={},deleted={},detached={}".format(
        insp.session_id,
        insp._attached,
        insp.transient,
        insp.persistent,
        insp.pending,
        insp.deleted,
        insp.detached
    )
    print(i, state)
    print(insp.key)


print('-' * 30)
student = session.query(Student).get(10)
getstate(student, 1)
try:
    # transient 实体类演示加入的session中，同时并没有保存到数据库中
    # pending   transient的实体被add()到session中，状态切换到pending，但是还没有flush到数据库中
    # persistent    session中的实例对象对应的数据库中的真实记录，pending状态在提交成功后，可以变成persistent状态，或者查询成功返回的实体也是persistent状态
    # deleted 实体被删除且已经flush但未commit完成，事务提交成功，实例变成detached，事务失败，返回persistent状态
    # detached 删除成功的实体进入这个状态
    student = Student(id=2, name='sam', age=30)
    getstate(student, 2)
    student = Student(name='sammy', age=30)
    getstate(student, 3)
    session.add(student)
    getstate(student, 4)
    session.commit()
    getstate(student,6)
except Exception as e:
    session.rollback()
