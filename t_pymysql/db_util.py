import typing

import pymysql
import pymysql.cursors


class DbUtil:
    connection = None

    def __init__(self, db_config: dict = None):
        if db_config is None:
            db_config = {}
        self.db_config = db_config
        self.__connect()

    def __connect(self):
        if self.connection is None:
            self.connection = pymysql.connect(
                host=self.db_config.get('HOST'),
                port=self.db_config.get('PORT'),
                user=self.db_config.get('USERNAME'),
                password=self.db_config.get('PASSWORD'),
                db=self.db_config.get('DATABASE'),
                charset=self.db_config.get('CHARSET'),
                cursorclass=pymysql.cursors.DictCursor
            )

    def close(self):
        if self.connection is not None:
            self.connection.close()

    def execute(self, sql) -> bool:
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(sql)
                self.connection.commit()
                return True
            except Exception as e:
                print(e)
                self.connection.rollback()
                return False

    def fetchone(self, sql) -> typing.Dict | None:
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(sql)
                return cursor.fetchone()
            except Exception as e:
                print(e)
                return None

    def fetchall(self, sql) -> typing.Tuple | None:
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(sql)
                return cursor.fetchall()
            except Exception as e:
                print(e)
                return None

    def insert(self, sql) -> int:
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(sql)
                self.connection.commit()
                return self.connection.affected_rows()
            except Exception as e:
                print(e)
                self.connection.rollback()
                return 0


def tt():
    with DbUtil() as sql:
        print("sssssss")
        raise Exception("asdasd")
        pass

    a = 1
    print("asdasd")
    return a


if __name__ == '__main__':
    config = {
        "HOST": "192.168.200.253",
        "PORT": 3400,
        "USERNAME": "root",
        "PASSWORD": "123456",
        "DATABASE": "cad",
        "CHARSET": "utf8mb4",
    }
    dbutil = DbUtil(config)

    # 插入数据
    # insert_sql = "INSERT INTO `province`(`name`,`code`,`url`) values('山西省', '121212', 'http://shanxi.com'),('河北省', '2222', 'http://hebei.com')"
    # res = dbutil.execute(insert_sql)
    # print("res:", res)
    # if res > 0:
    #     print("插入成功")
    # else:
    #     print("插入失败")

    # 查询单条数据
    # fetchone_sql = "SELECT * from `province` where name = '山西省1'"
    # province_record = dbutil.fetchone(fetchone_sql)
    # print("province_record:", province_record)

    # 查询多条数据
    fetchall_sql = "SELECT * from `province`"
    province_records = dbutil.fetchall(fetchall_sql)
    print("province_records:", province_records)