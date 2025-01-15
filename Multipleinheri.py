class Parent1:
    def display(self):
        print("This is Parent1.")


class Parent2:
    def display(self):
        print("This is Parent2.")


class Parent3:
    def display(self):
        print("This is Parent3.")


class Child(Parent1, Parent2, Parent3):
    def display_child(self):
        print("This is the Child class.")

    def display(self):
        super().display()
        print("This is the Child's display method.")


def main():
    child_obj = Child()
    child_obj.display()


if __name__ == "__main__":
    main()
