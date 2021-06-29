from mysql import connector
from mysql.connector import errorcode

class DBHelper():
    def __init__(self, host: str, port: str, user: str, password: str, database: str):
        """
        :param host:
        :param port:
        :param user:
        :param password:
        :param database:
        """

        self.__host = host
        self.__port = port
        self.__user = user
        self.__password = password
        self.__database = database

        self.__conn = None
        self.__cur = None

        self.checkConnect()

    def get(self):
        return self.__conn, self.__cur

    def checkConnect(self):
        """
        Kiểm tra kết nối với SQL, nếu chưa kết nối thì kết nối
        :return:
        """
        if not self.__conn:
            self.connectMysql()
            self.__cur = self.__conn.cursor()

    def connectMysql(self):
        """
        Kết nối với MySQL
        :return:
        """
        try:
            self.__conn = connector.connect(host=self.__host,
                                            port=self.__port,
                                            user=self.__user,
                                            password=self.__password,
                                            database=self.__database,
                                            charset='utf8')
        except:
            pass

    def createTable(self, sql: str):
        """
        Tạo table mới bằng dòng lệnh sql
        :param sql: câu lệnh truy vấn sql
        :return:
        """
        try:
            self.checkConnect()
            self.__cur.execute(sql)
        except:
            pass

    def insert(self, sql: str, *params: tuple):
        """
        Chèn một dòng dữ liệu
        :param sql: câu lệnh truy vấn sql
        :param params: danh sách tham số truyền dữ liệu
        :return:
        """
        try:
            self.checkConnect()
            self.__cur.execute(sql, params)
            self.__conn.commit()
        except:
            pass

    def inserts(self, sql: str, *list_params: list):
        """
        Chèn nhiều dòng dữ liệu
        :param sql: câu lệnh truy vấn sql
        :param params: danh sách các tupple, mỗi tupple là danh sách tham số của một dòng dữ liệu
        :return:
        """
        try:
            self.checkConnect()
            self.__cur.executemany(sql, list_params)
            self.__conn.commit()
        except:
            pass

    def update(self, sql: str, *params: tuple):
        """
        Update dữ liệu theo câu lệnh truy vấn sql
        :param sql: câu lệnh truy vấn sql
        :param params: danh sách tham số
        :return:
        """
        try:
            self.checkConnect()
            self.__cur.execute(sql, params)
            self.__conn.commit()
        except:
            pass

    def delete(self, sql: str, *params: tuple):
        """
        Xóa dữ liệu theo câu lệnh truy vấn sql
        :param sql: câu lệnh truy vấn sql
        :param params: danh sách tham số
        :return:
        """
        try:
            self.checkConnect()
            self.__cur.execute(sql, params)
            self.__conn.commit()
        except:
            pass

    def select(self, sql: str):
        """
        Hàm select truy vấn lấy dữ liệu trong database theo câu lệnh truy vấn sql
        Câu lệnh truy vấn này sẽ trả về một bảng dữ liệu trong MySQL
        Đối với python sẽ trả về một list các tupple
            + size of list là số dòng dữ liệu truy vấn
            + mỗi dòng là một tupple gồm các cột của dòng dữ liệu đó
        :param sql: câu lệnh truy vấn sql
        :return:
        """
        try:
            self.checkConnect()
            self.__cur.execute(sql)
            result = self.__cur.fetchall()

            return result
        except:
            pass

    def close(self):
        """
        Đóng kết nối với SQL
        :return:
        """
        try:
            self.__conn.close()
            self.__conn.close()
        except:
            pass
if __name__ == '__main__':
    # connect SQL
    helper = DBHelper('localhost','3306','root','123456789','Test')

    # test tạo bảng
    # sql = "create table test2(id1 int, id2 int)"
    # helper.createTable(sql)

    # test thêm một dòng dữ liệu
    # sql = "insert into test2(id1, id2) values (%s, %s)"
    # params = (1,2)
    # helper.insert(sql, *params)

    # test thêm nhiều dòng dữ liệu
    # sql = 'insert into test2(id1, id2) values (%s, %s)'
    # list_params = [(3,4),(5,6),(7,8)]
    # helper.inserts(sql, *list_params)

    # test update dữ liệu
    # sql = 'update test2 set id2 = %s where id1 = %s'
    # params = (99,1)
    # helper.update(sql, *params)

    # test xóa dữ liệu
    # sql = 'delete from test2 where id1 = %s'
    # params = (1,)
    # helper.delete(sql, *params)

    # test câu lệnh select
    # sql = 'select * from test2'
    # lst = helper.select(sql)
    # for x in lst:
    #     print(x)