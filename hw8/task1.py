from collections import defaultdict


class KeyValueStorage:
    """
        This is a wrapper class  for some key-value storage file.
         File consists rows,  each other is represented as key and value separated by = symbol.

         This class has its(storage) keys and values accessible as collection items and as attributes.
    """

    def __init__(self, file_path):
        """
        :param file_path: type: str, takes path to file which is a key-value storage file.
        """
        self.file_path = file_path
        self.item = defaultdict(int)
        with open(self.file_path, 'r') as fi:
            for line in fi:
                k, v = line.strip('\n').split('=')
                if k.isnumeric() and k != v:
                    raise ValueError
                self.item[k] = v
            print(self.item)

    def __getitem__(self, key):
        """
        This method is use to implement call like self[key]
        :param key: type: str
        :return: Should return value with match to the 'key'
        """
        try:
            return int(self.item[key]) or float(self.item[key])
        except ValueError:
            return self.item[key]

    def __getattr__(self, key):
        """
        This method is use to implement call like self.key
        :param key: type: str
        :return: Should return value with match to the 'key'
        """
        try:
            return int(self.item[key]) or float(self.item[key])
        except ValueError:
            return self.item[key]


storage = KeyValueStorage(r'E:\University\EPAM\hw8\task1.txt')

print(storage['1'])