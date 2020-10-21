from csvReader import csvToList
from mySqlAPI import MySQLAPI


def main():
    val = csvToList('main.csv')

    database = input("\ndatabase: ")
    password = input("password: ")
    table = input("table: ")

    mySqlAPI = MySQLAPI(database, password)

    mySqlAPI.list_to_db(table, val)

    print(mySqlAPI.db_to_list(table))


if __name__ == '__main__':
    main()
