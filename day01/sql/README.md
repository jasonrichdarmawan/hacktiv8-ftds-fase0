$ docker run --detach --network some-network --name some-mariadb --env MARIADB_ROOT_PASSWORD=root  mariadb:latest

$ docker run -it --network some-network --rm -v /Volumes/T7Touch/Learn/hacktiv8-ftds-fase0/day01/sql:/sql mariadb mariadb -hsome-mariadb -uroot -proot

    MariaDB [(none)]>
    ```
    source sql/01.sql
    ```