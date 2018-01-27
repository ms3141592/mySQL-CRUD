
# Create, read, update and delete

from db_controller import MySQL_CRUD


class TestCRUD:
    MENU = ['t_connect_sql()', 't_create_db()', 't_create_tb()', 't_look_tb()',
            't_add_tb()', 't_row_remove()', 't_remove_tb()', 't_remove_db()']

    def __init__(self):
        self.col_length = 0

    def t_connect_sql(self):
        print(0)
        host = input('hostname = ')
        user = input('username = ')
        pw = input('password = ')
        self.db = MySQL_CRUD(host, user, pw)

    def t_create_db(self):
        db_name = input('create or login to database = ')
        self.db.create_db(db_name)
        print(1)

    def t_create_tb(self):
        tb_name = input('create table = ')
        tb_cols = ''
        try:
            self.col_length = int(input('how many columns = '))
            for i in range(1, self.col_length+1):
                tb_cols += input('enter sql for column {} = '.format(i))
                if i is not self.col_length:
                    tb_cols += ', '
            print(tb_cols)
            self.db.create_db_table(tb_name, tb_cols)
        except ValueError as ve:
            print(ve)
        print(2)

    def t_look_tb(self):
        tb_name = input('table = ')
        col_val = input('column sort = ')
        self.db.show_db_table(tb_name, col_val)
        print(3)

    def t_add_tb(self):
        tb_name = input('table = ')
        len = self.db.tb_columns(tb_name)
        li = []
        for i in range(len):
            li.append(input('enter value for column {} = '.format(i)))

        self.db.insert_into_db(tuple(li), tb_name)
        print(4)

    def t_row_remove(self):
        tb = input('table = ')
        fld = input('field = ')
        name = input('value = ')
        name = '"{}"'.format(name)
        self.db.delete_table_row(tb, fld, name)
        print(5)

    def t_remove_tb(self):
        tb = input('table = ')
        self.db.drop_db_table(tb)
        print(6)

    def t_remove_db(self):
        db = input('database = ')
        self.db.drop_db(db)
        print(7)

    def run(self):
        while True:
            print('-----mySQL CRUD test-----')
            print('0. connect to mySQL\n'
                  '1. create a database\n'
                  '2. create a tale\n'
                  '3. look at table\n'
                  '4. add to table\n'
                  '5. remove from table\n'
                  '6. remove table\n'
                  '7. remove database\n'
                  '9. EXIT')
            try:
                i = int(input('> '))

                if i is 9:
                    break

                ret = 'self.{}'.format(self.MENU[i])
                exec(ret)
            except (IndexError, ValueError) as e:
                print(e)


t = TestCRUD()

if __name__ == '__main__':
    """
    # full method rundown start to finish
    db = MySQL_CRUD('localhost', 'root', 'root')

    db.create_db('sports_allstars')
    db.create_db_table('basketball',
                       'first_name VARCHAR(16) NOT NULL, last_name VARCHAR(16) NOT NULL, position VARCHAR(5), number INT')
    db.create_db_table('baseball',
                       'first_name VARCHAR(16) NOT NULL, last_name VARCHAR(16) NOT NULL, position VARCHAR(5), number INT')

    db.tb_columns('basketball')

    db.insert_into_db(('michael', 'jordan', 'SG', 23), 'basketball')
    db.insert_into_db(('lebron', 'james', 'SF/PF', 23), 'basketball')

    db.insert_into_db(('derek', 'jeter', 'SS', 2), 'baseball')
    db.insert_into_db(('ken', 'griffey', 'CF', 24), 'baseball')

    db.show_db_table('basketball', 'first_name')
    db.show_db_table('baseball', 'last_name')

    db.delete_table_row('basketball','last_name', '"James"')
    db.delete_table_row('baseball', 'first_name', '"ken"')

    db.drop_db_table('basketball')
    db.drop_db_table('baseball')

    db.drop_db('sports_allstars')
    """

    t.run()
