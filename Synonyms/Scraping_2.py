import requests
import OOP_with_database as OOP
import json

if __name__ == '__main__':
    # kết nối với SQL
    helper = OOP.DBHelper('localhost', '3306', 'root', '123456789', 'synonym')

    # tạo bảng
    sql = "create table data2(word_query nvarchar(255), word_relate nvarchar(255), similarity int," \
          "                 primary key (word_query, word_relate))"
    helper.createTable(sql)

    req = requests.get('https://tuna.thesaurus.com/relatedWords/happy')
    res = req.json()

    # scrap and backup
    f_3000word = open('3000words.txt','r')
    line = 0
    while True:
        word_query = f_3000word.readline()
        if word_query == None or word_query == '\n' or word_query == '':
            break
        word_query = word_query[:-1]  # xóa ký tự xuống dòng
        line += 1  # check dòng
        print(word_query, line)

        API = 'https://tuna.thesaurus.com/relatedWords/' + word_query

        req = requests.get(API)
        res = json.loads(req.text)
        res_data = res['data']
        if res_data == None:
            continue

        for i in range(len(res_data)):
            res_data_synonyms = res_data[i]['synonyms']
            if res_data_synonyms == None:
                continue
            for j in range(len(res_data_synonyms)):
                term = res_data_synonyms[j]['term']
                similarity = int(res_data_synonyms[j]['similarity'])

                sql = 'insert into data2(word_query, word_relate, similarity) values (%s, %s, %s)'
                params = (word_query, term, similarity)
                helper.insert(sql, *params)


    f_3000word.close()