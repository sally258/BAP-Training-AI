# SYNONYMS
## SETUP

* Install mysql-connector-python:
    ```pip install mysql-connector-python```

* Install requests
    ```pip install request```

## PYTHON FILE

* OOP_with_databas.py: Bridge between python and MySQL

* QuerySynonyms.py: Find synonyms in the database

* Scraping.py: scrap: Get data from website (scrap bằng xử lý chuỗi (file text))

* Scraping_2.py: scrap bằng request.json

## Mô tả
* Sử dụng một bảng dữ liệu gồm 3 cột, cột đầu tiên là từ query (nằm trong 3000 từ)
cột thứ 2 là từ đồng nghĩa với từ query và cột thứ 3 là mức độ đồng nghĩa so với từ query

* Bảng gồm hai khóa chính là từ query (cột 1) và từ đồng nghĩa với từ query (cột 2) cho nên
sẽ không tồn tại từ query và từ đồng nghĩa giống nhau mà mức độ đồng nghĩa khác nhau

* Hết rồi ạ