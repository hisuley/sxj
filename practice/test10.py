__author__ = 'pc'
import sqlite3


def convert(value):
    if value.startswith('~'):
        return value.strip('~')
    if not value:
        value = '0'
    return float(value)

coon = sqlite3.connect('food .db')
curs = coon.cursor()

curs.execute('''
CREAT TABLE food(
    id  TEXT    PRIMRY KEY,
    desc    TEXT,
    water   FLOAT,
    kcal    FLOAT,
    protein FLOAT,
    fat     FLOAT,
    ash     FLOAT,
    carbs   FLOAT,
    fiber   FLOAT,
    sugar   FLOAT
)
''')

query = 'INSERT INTO food VALUES (?,?,?,?,?,?,?,?,?,?)'

for line in open('ABBREV.txt'):
    fields = line.split('^')
    vals = [convert(f) for f in fields[:fields_count]]
    curs.execute(query, vals)

coon.commit()
coon.close()