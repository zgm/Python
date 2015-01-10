import MySQLdb
import time


class DBModel():

    def __init__(self):
        self.conn = MySQLdb.connect(host='localhost',user='root',passwd='zhanggmcn',port=3306)
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    def create_DB(self):
        cursor = self.conn.cursor()
        cursor.execute('create database if not exists timer')
        cursor.close()

        self.conn.select_db('timer')
        cursor = self.conn.cursor()
        cursor.execute('drop table if exists timer_info')
        cursor.execute('create table timer_info(time int, info varchar(20))')
        cursor.close()

    def insert_timer(self, time, info):
        self.conn.select_db('timer')
        cursor = self.conn.cursor()
        cursor.execute('insert into timer_info values(%s,%s)',(time, info))
        cursor.close()

    def delete_timer(self, time, info):
        self.conn.select_db('timer')
        cursor = self.conn.cursor()
        cursor.execute('delete from timer_info where time={0}'.format(time))
        cursor.close()

    def select(self):
        self.conn.select_db('timer')
        cursor = self.conn.cursor()
        cursor.execute('select time, info from timer_info')

        result = []
        for row in cursor.fetchall():
            result.append(row)
        cursor.close()
        return result


def timer():
    db = DBModel()
    db.create_DB()

    db.insert_timer(1234, '1234')
    print db.select()

    db.insert_timer(12345, '12345')
    print db.select()

    db.delete_timer(1234, '1234')
    print db.select()

    check_time, interval = 0, 10
    timer = []
    for i in range(1000000):
        time = time.time()
        if time>check_time+interval:
            check_time = time
            timer.extend( db.select() )

        for t in timer:
            if t[0]<time:
                print t
            else:
                continue




if __name__ == '__main__':
    timer()


