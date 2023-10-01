
#every neuron has unique connection to every single previous neuron
# 3 neurons are feeding into the neuron we are going to build
# their outputs becomes the neurons that we are coding
# every unique inputs has unique weights associated with it
#every unique neuron has unique bias
inputs = [1.2, 5.1, 2.1]
weights = [3.1, 2.1, 8.7]
bias = 3

output = inputs[0]*weights[0]+inputs[1]*weights[1]+inputs[2]*weights[2]+bias

print(output)