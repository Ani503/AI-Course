class student:
    def __init__(self, name, roll, mark):
        self.name = name
        self.roll = roll
        self.mark = mark
        print("hii")
    def study(self):
        print("I, "+str(self.name)+"my roll no is " +str(self.roll) + " and marks are " +str(self.mark))
s = student("Sayan", "49", "8.44")
s.study()
