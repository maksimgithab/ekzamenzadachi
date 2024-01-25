import sqlite3


con = sqlite3.connect('base.db')
cursor = con.cursor()
cursor.execute("""insert into maksim(id, name) values (1, 'егор не ставь два пожалуйста')""")
cursor.execute("""insert into maksim(id, name) values (2, 'егор не ставь два пожалуйста')""")
cursor.execute("""insert into maksim(id, name) values (3, 'егор не ставь два пожалуйста')""")
con.commit()
con.close()