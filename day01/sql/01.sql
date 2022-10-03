-- day01 slide 15

DROP DATABASE IF EXISTS test;

CREATE DATABASE test;

USE test;

\! echo "Membuat table";
CREATE TABLE item(
  ID int NOT NULL AUTO_INCREMENT,
  Item_Name varchar(20) NOT NULL,
  Item_Desc varchar(50),
  Item_Price Numeric,
  Created_Date Date,
  PRIMARY KEY(ID)
);

\! echo "insert value TARO 200 g";
INSERT INTO item (ID, Item_Name, Item_Desc, item_price, created_date) 
VALUE (1,'TARO 200 g','',15000,'2022-10-03');

\! echo "insert value TARO 200 g, duplikat";
INSERT INTO item (Item_Name, Item_Desc, item_price, created_date) 
VALUE ('TARO 200 g','',15000,'2022-10-03');

\! echo "insert value TARO 200 g, beda 2021-10-03";
INSERT INTO item (Item_Name, Item_Desc, item_price, created_date) 
VALUE ('TARO 200 g','',15000,'2021-10-03');

\! echo "insert value TARO 200 g, beda 300 g";
INSERT INTO item (Item_Name, Item_Desc, item_price, created_date) 
VALUE ('TARO 300 g','',15000,'2022-10-03');

\! echo "insert value TARO 200 g, beda harga 20000";
INSERT INTO item (Item_Name, Item_Desc, item_price, created_date) 
VALUE ('TARO 300 g','',20000,'2022-10-03');

\! echo "insert value Chitato 200 g";
INSERT INTO item (Item_Name, Item_Desc, item_price, created_date) 
VALUE ('Chitato 200 g','',20000,'2022-10-03');

\! echo "melihat ini table";
SELECT * FROM item;

\! echo "melihat beberapa kolom isi table";
SELECT item_name, item_price
FROM item;

\! echo "rename kolom";
SELECT item_name AS NAMA, item_price AS HARGA
FROM item;

\! echo "row yang unik, berdasarkan kolom yang dipilih";
SELECT DISTINCT item_name, item_price
FROM item;

\! echo "ORDER BY DESC"
SELECT *
FROM item
ORDER BY created_date DESC;

\! echo "WHERE=20000"
SELECT *
FROM item
WHERE Item_Price=20000;

\! echo "BETWEEN 15000 AND 17500"
SELECT *
FROM item
WHERE Item_Price
BETWEEN 15000 AND 17500;

\! echo "LIKE %200 g"
SELECT *
FROM item
WHERE item_name LIKE "%200 g";

\! echo "NOT LIKE %200 g"
SELECT *
FROM item
WHERE item_name NOT LIKE "%200 g";

\! echo "IN ('Chitato 200 g', 'TARO 200 g')"
SELECT *
FROM item
WHERE item_name IN ('Chitato 200 g', 'TARO 200 g')