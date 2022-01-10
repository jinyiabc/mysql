import mysql.connector

from config import PASSWORD


class MediumDB():
    def __init__(self):
        pass

    def writetodb(self):
        # Config
        config = {
            'user': 'root',
            'password': PASSWORD,
            'host': 'localhost',
            'database': 'mediumtutorialdb',
            'port': 3306,
            'raise_on_warnings': True,
        }

        # Connect to DB
        conn = mysql.connector.connect(**config)

        # Create Cursor
        c = conn.cursor()

        # Query
        query = (f"INSERT INTO `mediumtutorialdb`.`mediumtable` (`Name`, `Age`) VALUES ('bob', '38')")
        # Execute
        c.execute(query)

        # Commit
        conn.commit()

        # End Session
        c.close()
        conn.close()
        print('Sent To DB!\n')

if __name__ == '__main__':
    x = MediumDB()
    x.writetodb()
