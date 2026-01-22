class Animals:
    pass

class Pets(Animals):
    pass

class Dogs(Pets):
    @staticmethod
    def Bark():
        print('Dog barks.')

a = Dogs()
a.Bark()