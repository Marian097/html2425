import sqlite3


class DB:
    def __init__(self, db) -> None:
        self.db=db
        self.conection=None
        self.cursor=None 
        
    def open_db(self):
        self.conection=sqlite3.connect(self.db)
        self.cursor=self.conection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS clients (id INTEGER PRIMARY KEY AUTOINCREMENT, nume TEXT, prenume TEXT, email TEXT, parola TEXT)")
        self.conection.commit()
        print("Conexiune reusita.")

            
    def close_db(self):
        if self.conection:
            self.conection.close()
            print("Conexiune inchisa")
            
            
            



         