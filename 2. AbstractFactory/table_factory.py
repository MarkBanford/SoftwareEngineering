from big_table import BigTable
from small_table import SmallTable


class TableFactory:

    @staticmethod
    def get_table(table):
        if table == "SmallTable":
            return SmallTable()
        if table == "BigTable":
            return BigTable()
        return None
