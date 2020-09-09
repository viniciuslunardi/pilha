import array as arr


class Pilha:
    def init(self, len):
        self.__len = len
        self.__arr = arr.array("i", [])
        self.__limit = 0

    def pop(self):
        if self.__limit:
            del self.__arr[self.__limit - 1]
            self.__limit -= 1

    def push(self, num):
        if self.__limit != self.__len:
            self.__arr.append(num)
            self.__limit += 1

    def top(self):
        print(self.__arr[self.__limit - 1])
        return self.__arr[self.__limit - 1]

    def is_empty(self):
        if not self.__limit:
            return True
        else:
            return False

    def is_full(self):
        res = False
        if self.__limit == self.__len:
            res = True
        return res

    def num_elements(self):
        print(self.__limit)
        return self.__limit

    def str(self):
        return "O ARRAY: " + str(self.__arr)
