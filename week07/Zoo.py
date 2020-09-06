from abc import ABCMeta, abstractmethod


class Animal(object):
    """
    动物类
    """
    def __new__(cls, *args, **kwargs):
        if cls is Animal:
            raise TypeError("Animal class can not be instantiated")
        return object.__new__(cls)

    def __init__(self, species, size, temper):
        self.species = species
        self.size = size
        self.temper = temper

    @property
    def is_dangerous(self):
        """
        判断是否凶猛
        :return: 是返回True，不是返回False
        """
        if (self.size == "大" or self.size == "中") and self.species == "食肉" and self.temper == "凶猛":
            return True
        return False


class Cat(Animal):
    """
    猫类
    """
    sound = "喵"

    def __init__(self, name, species, size, temper):
        self.name = name
        super().__init__(species, size, temper)

    @property
    def is_pet(self):
        """
        判断是否适合做宠物
        :return: 适合返回True，不适合返回False
        """
        if self.temper == "凶猛":
            return False
        return True


class Dog(Animal):
    """
    狗类
    """
    sound = "汪"

    def __init__(self, name, species, size, temper):
        self.name = name
        super().__init__(species, size, temper)

    @property
    def is_pet(self):
        """
        判断是否适合做宠物
        :return: 适合返回True，不适合返回False
        """
        if self.temper == "凶猛":
            return False
        return True


class Zoo(object):
    """
    动物园类
    """
    animal_type_dict = set()
    animals_dict = set()

    def __init__(self, name):
        self.name = name

    def add_animal(self, animal):
        if not issubclass(animal.__class__, Animal):
            return
        class_name = type(animal).__name__
        if class_name not in Zoo.animal_type_dict:
            Zoo.animal_type_dict.add(class_name)
            setattr(Zoo, class_name, class_name)

        Zoo.animals_dict.add(animal)


if __name__ == '__main__':
    z = Zoo('时间动物园')
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    dog1 = Dog('小白狗', '食肉', '大', '凶猛')

    print(cat1.is_pet)
    print(cat1.is_dangerous)
    have_cat = hasattr(z, 'Cat')
    have_dog = hasattr(z, 'Dog')
    print(have_cat)
    print(have_dog)

    z.add_animal(cat1)
    z.add_animal(dog1)
    have_cat = hasattr(z, 'Cat')
    have_dog = hasattr(z, 'Dog')
    print(have_cat)
    print(have_dog)
    print(Zoo.animals_dict)
    print(Zoo.animal_type_dict)

    cat2 = Cat('大花猫 2', '吃草', '大', '温顺')
    z.add_animal(cat2)
    z.add_animal(cat1)
    print(Zoo.animals_dict)
    print(Zoo.animal_type_dict)



