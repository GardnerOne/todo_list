import sqlite3

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.create_user_table()
        self.create_todo_table()

    def create_todo_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS "todo" (
                id INTEGER PRIMARY KEY,
                Title TEXT,
                Description TEXT,
                _is_done boolean,
                _is_deleted boolean,
                CreatedOn Date DEFAULT CURRENT_DATE,
                DueDate Date,
                UserId INTEGER FOREIGNKEY REFERENCES User(_id)
            )
            """
        self.conn.execute(query)

    def create_user_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS "user" (
                id INTEGER PRIMARY KEY,
                Username TEXT
            )
            """
        self.conn.execute(query)

class ToDoModel:
    _tablename = "todo"

    def __init__(self):
        self.conn =  sqlite3.connect('todo.db')

    def create(self, title, description):
        query = """
            INSERT INTO {tablename}
            (Title, Description)
            VALUES ('{title}', '{description}')
        """.format(tablename=_tablename, title=title, description=description)

        result = self.conn.execute(query)
        return result

    def read(self, id):
        query = """
            INSERT INTO {tablename}
            (Title, Description)
            VALUES ('{title}', '{description}')
        """.format(tablename=_tablename, title=title, description=description)

        result = self.conn.execute(query)
        return result
                
    def update(self, id, title, description):
            query = """
            INSERT INTO {tablename}
            (Title, Description)
            VALUES ('{title}', '{description}')
        """.format(tablename=_tablename, title=title, description=description)

        result = self.conn.execute(query)
        return result
        
    def delete(self, id):
            query = """
            INSERT INTO {tablename}
            (Title, Description)
            VALUES ('{title}', '{description}')
        """.format(tablename=_tablename, title=title, description=description)

        result = self.conn.execute(query)
        return result
        
