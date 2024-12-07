# Apoptosis A

# Import super class
from signaling_entities import SignalingEntities

class ApoptosisA(SignalingEntities):
    def __init__(self, name:str, input:float):
        # Call base class to define name variable
        super().__init__(name)
        # Store input data in variables
        self.inputC = input

    def activate(self, threshold:float=0.1):
        # Activate kinase if C signal breaches threshold
        if self.inputC > threshold:
            self.output = self.inputC
        # Print error message only when unnecessary
        elif not (self.inputC > threshold) and self.input > 0:
            self.output = 0
            print("Error: The signal from C is not big enough for the Apoptose (A) to breach through to the next signal.")
        return self.output