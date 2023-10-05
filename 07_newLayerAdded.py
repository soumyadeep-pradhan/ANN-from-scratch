import numpy as np

inputs = [[1,2,3,2.5],
            [2,5,-1,2],
            [-1.5,2.7,3.3,-.8]]

weights1 = [[.2,.8,-.5,1],
           [.5,-.91,.26,-.50],
           [-.26,-.27,.17,.87]]
bias1 = [2,3,.5]
weights2 = [[.1,-.14,.5],
           [-.5,.12,-.33],
           [-.44,.73,-.13]]
bias2 = [-1,2,-.5]

# output = np.dot(weights,inputs)
layer1_output = np.dot(inputs, np.array(weights1).T) + bias1
layer2_output = np.dot(layer1_output, np.array(weights2).T) + bias2

print(layer2_output)