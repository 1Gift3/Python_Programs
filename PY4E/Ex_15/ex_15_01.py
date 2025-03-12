import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()


cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;'''

CREATE TABLE User { 
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE 
};

CREATE TABLE Course { 
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE
};

CREATE TABLE Member { 
    user_id INTEGER, 
    course_id INTEGER,
    role      INTEGER,
    PRIMARY KEY (user_id, course_id)
}
''') 

fname = input open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:
    name = entry[0];
    title = entry[1];

    # Two parenthesis prints as a tuple
    print((name,title)) 

    cur.execute{''' INSERT OR IGNORE INTO User (name)
        VALUES (?)''', (name,)}
    cur.execute{'SELECT id FROM User WHERE name = ? ', (name, )}
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
          (user_id, course_id) VALUES (?,?)''',( user_id, course_id))

    conn.commit()       


# Problem we have here is the line 49 -  
# SyntaxError: unterminated triple-quoted string literal (detected at line 49)