class Calculator:
    """Class that performs calculations
    """

    def __init__(self, result: float=0.0):
        """Constructor for the class, creates calculator-object for the user interface to use

        Args:
            result (float, optional): The starting result of the calculator. Defaults to 0.0.
        """
        self.result = result

    def add(self, value):
        """Add given value to the existing result

        Args:
            value : Number to be added to the result
        """
        self.result = self.result+value

    def subtract(self, value):
        """Subtract given value from existing result

        Args:
            value : Number to be subtracted from the result
        """
        self.result = self.result-value

    def multiply(self, value):
        """Multiply existing result with the given value

        Args:
            value : Number which the existing result is multiplied with
        """
        self.result = self.result*value

    def divide(self, value):
        """Divide existing result with the given value

        Args:
            value : Number which divides the existing result
        """
        if value == 0:
            self.result = "Error"
        else:
            self.result = self.result/value

    def clear(self):
        """Set the existing result to 0.0
        """
        self.result = 0.0

    def counternumber(self):
        """Multiply the existing result with -1
        """
        self.result = self.result*(-1.0)

    def to_percentage(self):
        """Divide the existing result with 100.0
        """
        self.result = self.result/100.0
