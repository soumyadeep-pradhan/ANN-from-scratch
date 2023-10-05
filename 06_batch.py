import numpy as np

inputs = [[1,2,3,2.5],
            [2,5,-1,2],
            [-1.5,2.7,3.3,-.8]]

weights = [[.2,.8,-.5,1],
           [.5,-.91,.26,-.50],
           [-.26,-.27,.17,.87]]
bias = [2,3,.5]

# output = np.dot(weights,inputs)
output = np.dot(inputs, np.array(weights).T) + bias

print(output)