class cal4:
    def setdata(self, num):
        self.num = num

    def square(self):
        return self.num**2

    def display(self):
        result = self.square()
        print(f"the Square of {self.num} is: {result}")

num = float(input("Enter Number:"))
c = cal4()
c.setdata(num=num)
c.display()

