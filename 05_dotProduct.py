import numpy as np

inputs = [1,2,3,2.5]
weights = [[.2,.8,-.5,1],
           [.5,-.91,.26,-.50],
           [-.26,-.27,.17,.87]]
bias = 2

output = np.dot(weights,inputs )+bias
print(output)