import requests
import OOP_with_database as OOP


if __name__ == '__main__':
    # kết nối với SQL
    helper = OOP.DBHelper('localhost', '3306', 'root', '123456789', 'synonym')

    # tạo bảng
    sql = "create table data(word_query nvarchar(255), word_relate nvarchar(255), similarity int," \
          "                 primary key (word_query, word_relate))"
    helper.createTable(sql)

    # scrap and backup
    f_3000word = open('3000words.txt','r')
    line = 0
    while True:
        word_query = f_3000word.readline()
        if word_query == None or word_query == '\n' or word_query == '':
            break
        word_query = word_query[:-1] # xóa ký tự xuống dòng
        line+=1 # check dòng
        print(word_query,line)

        API = 'https://tuna.thesaurus.com/relatedWords/' + word_query
        for k in range(10):
            API_limit = API + '?limit=' + str(k)
            req = requests.get(API_limit)

            st = req.text
            if len(st) < 20: break # trường hợp từ query không có dữ liệu

            # Xóa tất cả các dấu thừa
            st = st.replace("\"", "")
            st = st.replace("[", "")
            st = st.replace("{", "")
            st = st.replace("}", "")
            st = st.replace(",", ":") # Chuyển tất cả dấu , thành dấu :

            while True:
                i = st.find('synonyms') # vị trí đầu tiên của từ synonyms
                j = st.find('antonyms') # vị trí đầu tiên của từ antonyms
                if (i == -1 or j == -1 or i>j):
                    break
                lst = st[i:j].split(':')
                st = st[j+8:] # cập nhật chuỗi

                while True:
                    try:
                        p = lst.index('similarity')
                        similarity = int(lst[p + 1])
                        q = lst.index('term')
                        term = lst[q + 1]

                        lst = lst[q + 1:]
                        sql = 'insert into data(word_query, word_relate, similarity) values (%s, %s, %s)'
                        params = (word_query, term, similarity)
                        helper.insert(sql, *params)
                    except:
                        break

    f_3000word.close()