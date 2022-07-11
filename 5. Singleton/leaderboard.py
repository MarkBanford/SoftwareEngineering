class Leaderboard:
    _table = {}

    def __new__(cls):
        return cls

    @classmethod
    def print(cls):
        print("-------------------Leaderboard-------------")
        for k, v in sorted(cls._table.items()):
            print(f'|\t{k}\t|\t{v}\t')
        print()

    @classmethod
    def add_winner(cls, position, name):
        cls._table[position] = name
