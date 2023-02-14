class Jar:
    def __init__(self, capacity=12):
        if int(capacity)<0:
            raise ValueError('negative integer')
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return '🍪'* self._size

    def deposit(self, n):
        self._size = int(self._size) + int(n)
        if int(self._size) > int(self.capacity):
            raise ValueError('exceed capacity')



    def withdraw(self, n):
        self._size = int(self._size) - int(n)
        if int(self._size) < 0:
            raise ValueError('not enough cookie')


    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self,cap):
        if int(cap) < 0:
            raise ValueError("Negative integer")
        self._capacity = cap

    @property
    def size(self):
        return self._size

"""
def main():
    jar=Jar() #input('please enter capacity of jar: '))
    jar.deposit(6)    #input('how many cookie you want to add: '))
    jar.withdraw(2)     #input('how many cookie you want to eat: '))

    print (jar)



if __name__ == '__main__':
    main()"""