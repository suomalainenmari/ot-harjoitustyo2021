class Calculator:
  def __init__(self, result=0.0):
    self.result = result

  def add(self,value):
    self.result = self.result+value

  def subtract(self,value):
    self.result=self.result-value

  def multiply(self,value):
    self.result=self.result*value

  def divide(self,value):
    self.result = self.result/value

  def clear(self):
    self.result = 0.0
