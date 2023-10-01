inputs = [1, 2, 3, 2.5]
weights_1 = [0.2, .8, -.5, 1]
weights_2 = [0.5, -.91, .26, -.5]
weights_3 = [-0.26, -.27, .17, .87]
bias_1  = 2 
bias_2  = 3 
bias_3  = .5 

weights = [weights_1,weights_2,weights_3]
biases = [bias_1, bias_2, bias_3]

layer_outputs = [] #output of current layer
for neuron_wieghts, neuron_bias in zip(weights,biases):
    neuron_output = 0
    for n_input, weight in zip(inputs, neuron_wieghts):
        neuron_output += n_input*weight
    neuron_output+=neuron_bias
    layer_outputs.append(neuron_output)



print(layer_outputs)

