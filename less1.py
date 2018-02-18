class Fauna():
    def __init__(self, name, size, paws):
        self.name = name
        self.size = size
        self.paws = paws

    def __str__(self):
        return str({
            'name': self.name,
            'size': self.size,
            'paws': self.paws,
        })


class Birds(Fauna):
    name_bird = ['Утки', 'Куры', 'Гуси']

    def __init__(self, name_bird):
        self.name_bird = name_bird
        Fauna.__init__(self, name_bird, 'small', 2)

    def eggs(self, egg):
        print("{} дают {} шт яиц в день".format(self.name_bird, egg))

class Animal(Fauna):
    name_animal = ['Коровы', 'Козы', 'Овцы', 'Свиньи']

    def __init__(self, name_animal):
        self.name_animal = name_animal
        Fauna.__init__(self, name_animal, 'big', 4)


ducks = Birds('Утки')
chickens = Birds('Куры')
geese = Birds('Гуси')

Cows = Animal('Коровы')
Goats = Animal('Козы')
Sheep = Animal('Овцы')
Pigs = Animal('Свиньи')

# print(Birds._dict_)
print('\n Класс Птицы:',
      '\n Утки: {}'.format(ducks),
      '\n Куры: {}'.format(chickens),
      '\n Гуси: {}'.format(geese))

print('\n Класс Животные:',
      '\n Коровы: {}'.format(Cows),
      '\n Козы: {}'.format(Goats),
      '\n Овцы: {}'.format(Sheep),
      '\n Свиньи: {}'.format(Pigs))


