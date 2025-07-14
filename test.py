if __name__ == "__main__":
    class Dog:
        wings = False
        def __init__(self,color):
            self.color = color
        @classmethod
        def wing(cls):
            cls.wings = True


    class Bark(Dog):
        pass


    print(Dog.wings)