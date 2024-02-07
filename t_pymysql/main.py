import pymysql.cursors

connection = pymysql.connect(host='192.168.200.253',
                             port=3400,
                             user='root',
                             password='123456',
                             database='cad',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


def main():
    print("=== main start ===")
    # r = has_exception()  # has_exception, no_exception
    # print(connection.cursor())
    # print("r:", r)
    cc()


def no_exception() -> str:
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `province`"
            res = cursor.execute(sql)
            print("res:", res)
            print("num:", cursor.rowcount)
            result = cursor.fetchone()
            print("result:", result)
            # return "123"
    return "345"

def cc(c:dict={}):
    print(c)

def has_exception() -> str:
    with connection:
        with connection.cursor() as cursor:
            try:
                # Read a single record
                sql = "SELECT * FROM `province`"
                res = cursor.execute(sql)
                print("res:", res)
                print("num:", cursor.rowcount)
                result = cursor.fetchone()
                print("result:", result)
                ss = "asdasd"
            except Exception as e:
                print(e)
                return ""
            else:
                # return ss
                print(22)
                pass
    print(cursor)


if __name__ == '__main__':
    main()
