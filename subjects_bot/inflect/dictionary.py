import sqlite3

class Dictionary():

    def __init__(self):
        self.con = sqlite3.connect("dictionary.db")
        self.cur = self.con.cursor()

    def create_tables(self):
        """Create tables in the database."""

        # Entry table
        self.cur.execute("""
            CREATE TABLE entry (
                id INTEGER PRIMARY KEY,
                lemma TEXT,
                pos TEXT
            )
        """)

        # Inflection table
        self.cur.execute("""
            CREATE TABLE inflection (
                id INTEGER PRIMARY KEY,
                entry_id INTEGER,
                form TEXT NOT NULL,
                gender TEXT,
                number TEXT,
                FOREIGN KEY(entry_id) REFERENCES entry(id)
            )
        """)

        self.con.commit()

    def add_entry(self, lemma, pos):
        self.cur.execute("""
            INSERT INTO entry VALUES(?, ?, ?)
        """, [None, lemma, pos])

        return self.cur.lastrowid
    
    def add_inflection(self, entry_id, form, gender=None, number=None):
        self.cur.execute("""
            INSERT INTO inflection VALUES(?, ?, ?, ?, ?)
        """, [None, entry_id, form, gender, number])

        return self.cur.lastrowid

    def get_inflection(self, word):
        res = self.cur.execute("""
            SELECT gender, number
            FROM inflection
            WHERE form == :word
        """, {"word": word})

        gender, number = res.fetchone()

        return {"gender": gender, "number": number}
    
    def inflect_adjective(self, adjective, gender, number):
        res = self.cur.execute("""
            SELECT target.form
            FROM inflection
            LEFT OUTER JOIN inflection AS target
                ON target.entry_id == inflection.entry_id
                AND target.gender == :gender
                AND target.number == :number
            LEFT OUTER JOIN entry ON entry.id == inflection.entry_id
            WHERE inflection.form == :adjective AND entry.pos == "adj"
        """, {"gender": gender, "number": number, "adjective": adjective})

        return res.fetchone()[0]

    def commit(self):
        self.con.commit()
