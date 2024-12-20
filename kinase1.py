# Kinase, for K1

# Import super class
from signaling_entities import SignalingEntities

class Kinase1(SignalingEntities):
    def __init__(self, name:str, input1:float, input2:float):
        # Call base class to define name variable
        super().__init__(name)
        # Store input data in variables
        self.input1 = input1
        self.input2 = input2
    
    def activate(self, threshold: float = 1):
        # Activate kinase if sum of stimuli breaches threshold
        # Calculate the sum of the inputs (r1 and r2)
        sum_inputs = self.input1 + self.input2
        # Set conditions for activation
        if sum_inputs > threshold:
            self.output = sum_inputs
        elif not (sum_inputs > threshold) and self.input1 > 0 and self.input2 > 0:
            self.output = 0
        return self.output