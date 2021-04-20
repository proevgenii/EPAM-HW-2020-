import sqlite3


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

    def __len__(self):
        """
        This method should return the  current amount of rows in the table, an integer >=0
        :return: int
        """
        self.cursor.execute(f"select count(*) from {self.table_name}")
        return self.cursor.fetchone()[0]

    def __getitem__(self, item):
        """
        This method is use to implement call like self[item]
        :param item: type: str
        :return: Should return single data row from table with name == 'item'
        """
        self.cursor.execute(
            f"SELECT * from {self.table_name} where name=:name", {"name": item}
        )
        return self.cursor.fetchone()

    def __contains__(self, item):
        """
        Called to implement membership test operators. Should return true if item is in table, false otherwise.
        :param item: type:str
        :return: bool
        """
        self.cursor.execute(f'SELECT name from {self.table_name} where name = "{item}"')
        data = self.cursor.fetchall()
        return True if data else False

    def __iter__(self):
        """
        Allows to iterate over a table rows
        :return: This method should return a new iterator object that can iterate over all the objects in the container.
        """

        def dict_fact(row):
            dict = {}
            for i, c in enumerate(self.cursor.description):
                dict[c[0]] = row[i]
            return dict

        yield from (
            dict_fact(row)
            for row in self.cursor.execute(f"SELECT * from {self.table_name}")
        )

    def __enter__(self):
        self.conn = sqlite3.connect(self.database_name)
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()


if __name__ == "__main__":
    with TableData(database_name="example.sqlite", table_name="presidents") as td:
        print(len(td))
        print(td["Trump"])
        for x in td:
            print(x["name"])
