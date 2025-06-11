class Foo:
    def hello(self):
        print(self.__class__.__name__.lower())

class Bar(Foo):
    def hello(self):
        super().hello()
        bar=Bar() 
        bar.hello()