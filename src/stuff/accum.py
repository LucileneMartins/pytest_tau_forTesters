class Accumulator:
    def __init__(self):
        self._count = 0

    @property
    def getCount(self):
        return self._count

    def add(self, addValue=1):
        self._count += addValue
