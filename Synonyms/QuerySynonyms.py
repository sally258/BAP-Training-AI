import OOP_with_database as OOP

if __name__ == '__main__':
    # kết nối với SQL
    helper = OOP.DBHelper('localhost', '3306', 'root', '123456789', 'synonym')

    query = input('Nhập từ query: ')
    sql = "select * from data where word_query = \'" + query + "\' order by similarity desc"
    lst = helper.select(sql)
    print('word_relate\t tsimilarity')
    for i in range(len(lst)):
        print(lst[i][1] + '\t' + str(lst[i][2]))