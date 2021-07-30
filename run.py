class Number(object):
    def __init__(self, num1: int, num2: int):
        self.num1 = num1
        self.num2 = num2
    
    def add(self) -> int:
        return self.num1 + self.num2

    def substract(self) -> int:
        return abs(self.num1 - self.num2)


if __name__ == '__main__':
    num1 = input('please enter the first number: ')
    num2 = input('please enter the second number: ')

    number = Number(int(num1), int(num2))
    print('sum is:', number.add())
    print('substract is:', number.substract())