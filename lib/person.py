class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("Hello World!")

    def walk(self):
        print("The person is walking.")


guido = Person("Guido")
guido.walk()
guido.talk()
