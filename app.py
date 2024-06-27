import sqlite3

class Database:
    def __init__(self):
        self.mydb = sqlite3.connect('todo_list.db')
        self.cursor = self.mydb.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS task (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL,
                status TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.mydb.commit()

    def add_task(self, task):
        self.cursor.execute("INSERT INTO task (task, status) VALUES (?, 'not_done')", (task,))
        self.mydb.commit()

    def view_task(self):
        self.cursor.execute("SELECT * FROM task ORDER BY created_at DESC")
        tasks = self.cursor.fetchall()
        return tasks

    def delete_task(self, task_id):
        self.cursor.execute("DELETE FROM task WHERE id = ?", (task_id,))
        self.mydb.commit()

    def close_db(self):
        self.cursor.close()
        self.mydb.close()

db = Database()
