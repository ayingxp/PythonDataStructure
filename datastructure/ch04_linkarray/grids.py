from  arrays import Array
# from  arrays import Array

class Grid(object):
    def __init__(self, rows, columns, fillValue=None):
        self._data = Array(rows)
        for i in range(rows):
            self._data[i] = Array(columns, fillValue)


    def getHeight(self):
        return len(self._data)


    def getWidth(self):
        return len(self._data[0])


    def __getitem__(self, index):
        return self._data[index]

    def __str__(self):
        results = ""
        for row in self._data:
            for item in row:
                results += str(item) + " "
            results += "\n"
        return results


if __name__ == "__main__":
    grid = Grid(5,4, 9)
    print(grid)
    print(grid[0])

    print(grid.getHeight(), grid.getWidth())