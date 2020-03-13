import sqlite3

database_name = "intyme.db"

def show_tables():
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    tabData = []
    for tables in result:
        for table in tables:
            tabData.append(table)
    return tabData

def create_table(table_name, cols):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    sql_query = "CREATE TABLE " + table_name + "(" + cols + ");"
    print(sql_query)
    cursor.execute(sql_query)
    connection.commit()
    cursor.close()
    connection.close()

def show_table_columns(table_name):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    sql_query = "SELECT * FROM " + table_name
    cursor.execute(sql_query)
    num_fields = len(cursor.description)
    field_names = [i[0] for i in cursor.description]
    connection.commit()
    cursor.close()
    connection.close()
    return field_names

def insert_data(sql_query):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor.execute(sql_query)
    connection.commit()
    cursor.close()
    connection.close()

def cre_tab_cols():
    table_name = input("Enter the table name: ")
    cols = []
    while(True):
        column_name = input("Enter column name(q to quit): ")
        if column_name == "q":
            break
        datatype = input("Enter datatype for "+column_name+": ")
        entry = (column_name, datatype)
        cols.append(entry)
    columns = []
    for col in cols:
        c = " ".join(col)
        columns.append(c)
    final = ", ".join(columns)
    create_table(table_name,final)

def drop_table(table_ch):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    sql_query = "DROP TABLE " + table_ch + ";"
    print(sql_query)
    cursor.execute(sql_query)
    connection.commit()
    cursor.close()
    connection.close()
    return table_ch + " Deleted"

def rename_table():
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    sql_query = "ALTER TABLE bca6_a_timetable RENAME TO bca6_B_timetable;"
    cursor.execute(sql_query)
    connection.commit()
    cursor.close()
    connection.close()


def main():
    tablesData = []
    while (True):
        choice = int(input("\n0. Exit\n1. Create Table\n2. Check tables\n3. Insert data\n4. Drop table\n\t Enter your choice:"))
        if choice == 0:
            break
        elif choice == 1:
            cre_tab_cols()
        elif choice == 2:
            print("\nTables in database: ")
            for table in show_tables():
                print(table, "\t:\t", show_table_columns(table))
        elif choice == 3:
            tables_data = show_tables()
            print("\n\tTables in database are:")
            i = 0
            for table in tables_data:
                print(i, ":\t", table)
                i += 1
            table_ch = int(input("\tSeleet table: "))
            print(show_table_columns(tables_data[table_ch]))
            tab_columns = show_table_columns(tables_data[table_ch])
            values = []
            for column in tab_columns:
                values.append(input("\t" + column + ": "))
            print(tables_data[table_ch])
            print(tab_columns)
            print(values)
            sql_query = "INSERT INTO " + str(tables_data[table_ch]) + " (" + ",".join(
                tab_columns) + ")" + " VALUES" + str(tuple(values))
            print(sql_query)
            insert_data(sql_query)
        elif choice == 4:
            tables_data = show_tables()
            print("\n\tTables in database are:")
            i = 0
            for table in tables_data:
                print(i, ":\t", table)
                i += 1
            table_ch = int(input("\tSeleet table: "))
            print(drop_table(tables_data[table_ch]))

        else:
            print("\n\n\tInvalid Choice..")



if __name__ == '__main__':
    #main()
