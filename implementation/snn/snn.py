class Neuron:
    pass


class SpikingNeuralNetwork:
    def __init__(self, input_pattern):
        #  1. Initialize output neuron repository,R={}
        self.R = {}
        #  2. Set eSNN parameters: mod = [0,1], C = [0, 1], sim =[0,1]
        self._parameters = {
            "mod": 1,
            "C": 1,
            "sim": 1,
        }
        # input_pattern = M-dimensional training input pattern
        self.input_pattern = input_pattern
        # output neurons
        self.output_neurons = []
        #  3. for all input pattern i that belongs to the same class
        for input_vector in self.input_pattern:
            #  4. Encode input pattern into firing time of multiple pre-synaptic neurons j
            encoded_input_vector = self.encode_input_pattern(input_vector)
            for j in encoded_input_vector:
                #  5. Create a new output neuron i for this class and
                #     calculate the connection weights as w_ji = mod ** order(j)
                self.create_new_output_vector(encoded_input_vector)
                #  6. Calculate PSP_(max(i)) = Sum(j) * w_ji * mod ** order(j)
                psp = self.psp(encoded_input_vector, j)
                #  7. Calculate PSP threshold value γ_i = PSP_(max(i)) * C
                y = psp * self._parameters.get("C")
                #  8. if The new neuron weight vector sim of trained output neuron weight vector in R

                #  9. Update the weight vector and threshold of the most similar neuron in the same output class group

                # 10. w = (w_new + w * N) / (N + 1)

                # 11. z = (z_new + z * N) / (N + 1); where N is the number of previous merges of the most similar neuron

                # 12. else

                # 13. Add the weight vector and threshold of the new neuron to the neuron repository R

                # 14. end if

                # 15. end for

                # 16. Repeat above for all input patterns of other output classes

    def encode_input_pattern(self, input_vector):
        return []

    def create_new_output_vector(self, encoded_input_vector):
        return Neuron()

    def psp(self, encoded_input_vector, j):
        return 2
