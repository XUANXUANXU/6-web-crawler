import pymongo
from bson.objectid import ObjectId
# mongo_conn = pymongo.MongoClient(host='localhost',port=27017)
# mongo_conn = pymongo.MongoClient('mongodb://localhost:27017/')
mongo_conn = pymongo.MongoClient('mongodb://xuan:zxcvbnm000@localhost:27017/')
db = mongo_conn.class1803
stu_col = db.students
# 增
def add_data():
    i1 = {
        'name':'小明',
        'age':22,
        'gender':'男',
        'class':'1804',
    }
    i2 = {
        'name':'小话',
        'age':20,
        'gender':'女',
        'class':'1804',
    }
    i3 = {
        'name':'小刚',
        'age':17,
        'gender':'女',
        'class':'1804',
    }
    result = stu_col.insert([i1,i2,i3])
    print(result)
# 删
def dele_data():
    result = stu_col.remove({'name':'小明'},multi=False)
    print(result)
# 改
def update_data():
    # result = stu_col.update({'name':'小话'},{'$set':{'age':10}})
    result = stu_col.save({'_id':ObjectId("5ba9dfb5902f0c3c271bf169"),'name':'轩'})
    print(result)
# 查
def find_data():
    # result = use_col.find({'name':'liyong'})
    # print([i for i in result])
    result = stu_col.find({}).limit(1)
    print([i for i in result])
if __name__ == '__main__':
    # add_data()
    # dele_data()
    update_data()
    # find_data()
    


