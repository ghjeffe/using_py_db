import re
import sqlite3

MAILFILE = 'mbox.txt'
DBFILE = 'mbox_orgs.sqlite'
mbox_orgs = {}

with open(MAILFILE, mode='r', encoding='utf8') as fh:
    for line in fh:
        if line.startswith('From:'):
            user, org = line.split('@')
            if not mbox_orgs.get(org, False):
                mbox_orgs[org] = 1
            else:
                mbox_orgs[org] += 1
            
conn = sqlite3.connect(DBFILE)
cursor = conn.cursor()
cursor.execute('create table Counts (org TEXT, count INTEGER)')
for org, count in mbox_orgs.items():
    cursor.execute('insert into Counts values (?, ?)', (org.strip('\n'), count))
conn.commit()
cursor.close()