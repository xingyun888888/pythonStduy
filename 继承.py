__author__ = 'Administrator'


class  People:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        pass
        print("%s is eating..." % self.name)

    def sleep(self):
        print("%s is sleeping..." % self.name)

    def talk(self):
        print("%s is talking..." % self.name)

class Man(People):
    def __init__(self,name,age,money):
        # People.__init__(self,name,age)
        super(Man,self).__init__(name,age)

        self.money = money
        print("%s 一出生就有%s money..." % (name,money))
    def piao(self):
        print("%s is piaoing...20s...isdone" % self.name)

    def sleep(self):
        #People.sleep(self)
        print("man is sleeping")

class Women(People):
    pass
    def get_birth(self):
        print("%s is born a baby...." % self.name)



m1 = Man("chenronghua",22,10000)

m1.eat()

m1.sleep()

m1.talk()

m1.piao()


w1 = Women("ronghua",26)

w1.get_birth()





