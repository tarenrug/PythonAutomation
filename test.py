class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)
        self.__method1("t")

        #hi=__method1
    
        print(self.items_list)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    def method1(self,t):
        for i in ["1","2","3",t]:
            self.items_list.append(i)


    __update = update   # private copy of original update() method
    method12 = method1
    __method1 = method1

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

dog=Mapping(["tennis1","tennis2"])

dog.update(["extra1","extra2"])

print(dog.items_list)

cat = MappingSubclass(["n1","n2","n3"])

cat.update(["extra3","extra4"],["values1","values2"])
cat.__method12("3")

print(cat.items_list)