class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass

    def display_info(self):
        print(f"I am a {self.species} named {self.name}.")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, species="dog")

    def make_sound(self):
        return "Woof"


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, species="cat")

    def make_sound(self):
        return "Meow"


def main():
    dog1 = Dog("Buddy")
    cat1 = Cat("Whiskers")

    dog1.display_info()
    print("Dog says:", dog1.make_sound())

    cat1.display_info()
    print("Cat says:", cat1.make_sound())


if __name__ == "__main__":
    main()
