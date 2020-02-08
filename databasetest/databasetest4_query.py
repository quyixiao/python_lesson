import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, Enum, BigInteger
from sqlalchemy.orm import sessionmaker

#
from sqlalchemy.ext.declarative import declarative_base
# 生产环境很少这样的创建表，都是系统上线的时候由脚本生成
# 生成环境很少的删除表，宁可废弃都不能删除
# session对象线程不安全，所以不同线程使用不同的session对象
# Session类
# s主键没有值，就是新增，主键有值，
# query方法将实体传入，返回的类的对象
# 编写如下程序来删除数据，会发生什么
# 会产生一个异常
# 状态
# 每一个实体，都有一个状态属性_sa_instance_state，其类型是sqlalchemy.orm.state.instanceState，可以使用
# sqlalchemy.inspect(entity)函数查看状态
# 常见的状态值有transient,pending,persistent,deleted,detached
# transient 实体类演示加入的session中，同时并没有保存到数据库中
# pending   transient的实体被add()到session中，状态切换到pending，但是还没有flush到数据库中
# persistent    session中的实例对象对应的数据库中的真实记录，pending状态在提交成功后，可以变成persistent状态，或者查询成功返回的实体也是persistent状态
# deleted 实体被删除且已经flush但未commit完成，事务提交成功，实例变成detached，事务失败，返回persistent状态
# detached 删除成功的实体进入这个状态
# 新建的一个实体，状态是transient临时的
#一旦add()后，transient变成了pending状态
# 成功commit()后，pending变成了persistent
# 成功查询返回的实体对象，也是persient状态
# persient状态的实体，修改依然是persient状态
# persient状态的实体，删除后，flush后但没有commit，就变成了deteled状态，成功提交，变成了detached
#
# url:jdbc:mysql://172.16.157.238:3306/linzi_biz?characterEncoding=utf-8&allowMultiQueries=true
# username:ldd_biz
# password:Hello1234

# connnet = 'mysql+?://username:pwd@ip:port/databasename?key=value'.format()
import logging



FORMAT = '%(asctime)s 【%(levelname)s】 [%(filename)s:%(lineno)d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)


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
# 删除和更新之前要查询之后才能进行删除，更新

query = session.query(Student)
for student in query:
    print(student,type(student))

student = Student()
student.id = 5
student.name = 'zhangsan'
student.age=50
print(student)
print('-'*30)
session.add(student)
try:
    session.commit()
except Exception as e :
    logging.error(e)
    session.rollback()
student =session.query(Student).get(5) # 主键查询方式
print(student)



























