import sqlite3
import os.path


class TableData:
    """
    This is a wrapper class  for database table.
    That when initialized with database name and table acts as collection object (implements Collection protocol).
    """

    def __init__(self, database_name: str, table_name: str):
        """

        :param database_name: type: str  takes database name
        :param table_name: type: str takes name of table in database
        """
        self.database_name = database_name
        self.table_name = table_name
        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()

    def __len__(self):
        """
        This method should return the  current amount of rows in the table, an integer >=0
        :return: int
        """
        self.cursor.execute(f'select count(*) from {self.table_name}')
        data = self.cursor.fetchall()
        return data[0][0]

    def __getitem__(self, item):
        """
        This method is use to implement call like self[item]
        :param item: type: str
        :return: Should return single data row from table with name == 'item'
        """
        data = self.cursor.execute(f" SELECT * from {self.table_name}")
        names = [description[0] for description in data.description]
        if item in names:
            data = [data[0] for data in self.cursor.execute(f'SELECT {item} from {self.table_name} ').fetchall()]
            return data
        else:
            self.cursor.execute(f'SELECT * from {self.table_name} where name = "{item}"')
            data = self.cursor.fetchall()
        return data if data else (
            f' There is no row: "{item}" in table: "{self.table_name}" in DB: "{self.database_name}"')

    def __contains__(self, item):
        """
        Called to implement membership test operators. Should return true if item is in table, false otherwise.
        :param item: type:str
        :return: bool
        """
        self.cursor.execute(f'SELECT name from {self.table_name} where name = "{item}"')
        data = self.cursor.fetchall()
        return True if data else False

    #def __next__(self):
      #  self.cursor.execute(f'Select * from {self.table_name}')
       # return self.cursor.__next__()

    def __iter__(self):
        """
        Allows to iterate over a table rows
        :return: This method should return a new iterator object that can iterate over all the objects in the container.
        """
        self.cursor.execute(f'Select * from {self.table_name}')
        return self.cursor.__iter__()
