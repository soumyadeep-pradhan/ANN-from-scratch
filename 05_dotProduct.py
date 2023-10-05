import numpy as np

inputs = [1,2,3,2.5]
weights = [[.2,.8,-.5,1],
           [.5,-.91,.26,-.50],
           [-.26,-.27,.17,.87]]
bias = 2

output = np.dot(weights,inputs)+bias # dont switch weights and inputs order
print(output)

# np.dot(weights, inputs) = [np.dot(weights[0],inputs), np.dot(weights[1],inputs), np.dot(weights[2],inputs)]