class Calculator:
    def __init__(self, result=0.0):
        self.result = result

    def add(self, value):
        self.result = self.result+value

    def subtract(self, value):
        self.result = self.result-value

    def multiply(self, value):
        self.result = self.result*value

    def divide(self, value):
        if value == 0:
            self.result = "Error"
        else:
            self.result = self.result/value

    def clear(self):
        self.result = 0.0

    def counternumber(self):
        self.result = self.result*(-1)

    def to_percentage(self):
        self.result = self.result/100
