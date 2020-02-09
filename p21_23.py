# 类的继承：
# 继承的好处————  a、子类获得父类的全部功能
#                b、子类可以覆盖父类的方法，从而实现多态
class Animal():

    def __init__(self,name):
        self.name = name
        print('animai init...\n')

    def run(self):
        print('run...\n')

    def eat(self):
        print('eat...\n')


class Dog(Animal):
    def __init__(self,name):
        super(Dog, self).__init__(name=name)
        print('dog init...\n')

    def run(self):
        print('dog run...\n')

my_dog = Dog('wells')
# my_dog= Dog('wells')
my_dog.run()
my_dog.eat()
