from collections import defaultdict


class KeyValueStorage:
    """
    This is a wrapper class  for some key-value storage file.
    File consists rows,  each other is represented as key and value separated by = symbol.
    This class has its(storage) keys and values accessible as collection items and as attributes.
    """

    def __init__(self, file_path: str) -> None:
        """
        :param file_path: takes path to file which is a key-value storage file.
        """

        self.item = defaultdict(int)
        with open(file_path, "r") as fi:
            for line in fi:
                k, v = line.replace(" ", "").strip().split("=")
                if k.isnumeric() and k != v:
                    raise ValueError
                self.item[k] = v

    def __getitem__(self, key: str):
        """
        This method is use to implement call like self[key]
        :return: Should return value with match to the 'key'
        """
        try:
            return int(self.item[key]) or float(self.item[key])
        except ValueError:
            return self.item[key]

    def __getattr__(self, key: str):
        """
        This method is use to implement call like self.key
        :return: Should return value with match to the 'key'
        """
        try:
            return int(self.item[key]) or float(self.item[key])
        except ValueError:
            return self.item[key]
