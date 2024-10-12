class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self, name, floors):
        self.name = name
        self.floors = floors
        House.houses_history.append(name)

    def __del__(self):
        print(f'{self.name} рухнул, дольщики ловят прораба')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Mатрёшки', 30)
print(House.houses_history)
h4 = House('Кооператив Берлога', 1)
print(House.houses_history)
del h2
del h3
print(House.houses_history)
