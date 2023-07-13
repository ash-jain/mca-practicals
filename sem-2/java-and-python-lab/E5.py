"""
* Student Name - Aakash Jain.
* Roll No. - 222010019.
* Subject - Java and Python Lab.
* Lab Experiment 5 - Design a program for exception handling, multithreading and database operations.
"""

import sqlite3
import threading


class Database:
    def __init__(self, title) -> None:
        self.conn = sqlite3.connect(title, check_same_thread=False)
        self.cur = self.conn.cursor()


    def __del__(self) -> None:
        self.conn.commit()
        self.conn.close()
        print('Closing...')


    def createTable(self, title) -> None:
        try:
            self.cur.execute("""
                CREATE TABLE {} (RollNo INTEGER, Name TEXT, Degree TEXT, Semester INTEGER, Year INTEGER);
            """.format(title))
            print('Table created.')
        except sqlite3.OperationalError as e:
            print('Table already exists.')


    def populate(self, title) -> None:
        self.cur.executemany(f"INSERT INTO {title} VALUES (?, ?, ?, ?, ?)", insertions)


    def insert(self, table, id_, name, degree, semester, year) -> None:
        try:
            self.cur.execute(f"INSERT INTO {table} VALUES('{name}', {id_}, '{degree}', {semester}, {year})")
        except Exception as e:
            self.createTable(table)
            self.cur.execute(f"INSERT INTO {table} VALUES('{name}', {id_}, '{degree}', {semester}, {year})")
        finally:
            print('Data inserted.')


    def getTableData(self, table) -> None:
        try:
            print(f'{table.capitalize()} data: ')
            for row in self.cur.execute(f'SELECT * FROM {table};'):
                print(row)
        except sqlite3.OperationalError as e:
            print('Table does not exist.')


if __name__ == '__main__':

    db = Database('./E5.db')
    res = -1

    insertions = [
        ("Aakash Jain", 222010019, "MCA", 2, 2023),
        ("Jeet Joshi", 222010020, "MCA", 2, 2023),
        ("Om Kharat", 222010027, "MCA", 2, 2023),
        ("Kanishka Patil", 222010037, "MCA", 2, 2023),
        ("Yogesh Umalkar", 222010063, "MCA", 2, 2023),
        ("Ankush Waghbhaneria", 222010065, "MCA", 2, 2023),
    ]



    while (res := int(input("Enter operation number:\n1. Create.\n2. Insert.\n3. Populate.\n4. Print.\n5. Exit.\n")))!= 5:
        print()

        if res == 1:
            db.createTable('students')
        elif res == 2:
            try:
                id_ = int(input("Enter Roll No: "))
                name = input("Enter Name: ")
                degree = input("Enter Degree: ")
                semester = int(input("Enter Semester: "))
                year = int(input("Enter Year: "))
                print()
            except ValueError as e:
                print('Enter accurate data.')
            finally:
                t1 = threading.Thread(target=db.insert, args=('students', id_, name, degree, semester, year))
                t1.start()
                t1.join()
        elif res == 3:
            db.populate('students')
        elif res == 4:
            db.getTableData('students')
        else:
            print("Enter correct operation!")

        print()
