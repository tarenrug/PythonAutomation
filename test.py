class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)
        self.__method1("t")

        print(self.items_list)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    def method1(self,t):
        for i in ["1","2","3",t]:
            self.items_list.append(i)

    __update = update   # private copy of original update() method
    __method1 = method1
    __method12=method1

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

dogs=Mapping(["tennis1","tennis2"])
dogs.method1("15")

dogs.update(["extra1","extra2"])


print(dogs.items_list)

cat = MappingSubclass(["n1","n2","n3"])

cat.update(["extra3","extra4"],["values1","values2"])
cat._Mapping__method1("3")

print(cat.items_list)