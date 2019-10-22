import os
import numpy as np
import pywt
data = np.ones((4,4), dtype=np.float64)
coeffs = pywt.dwt2(data, 'haar')
array = []
cA, (cH, cV, cD) = coeffs
cA
# array([[ 2.,  2.],
#        [ 2.,  2.]])
cV
# array([[ 0.,  0.],
    #    [ 0.,  0.]])
# print(cA)
# print(cV)

output_2d_list = []
current_working_directory = os.path.abspath('.')

for filename in os.listdir(current_working_directory):
    if filename.endswith('.txt'):

        
        try:
           
                with open(filename, 'r') as current_file:
                    print(output_2d_list)

                    
                    for line in current_file.readlines():
                        point = line.split(', ')
                        x = float(point[0])
                        y = float(point[1])
                        point_as_array = [x, y]
                        output_2d_list.append(point_as_array)
        except IOError:
            print ("Something went wrong when attempting to read file.")


data = output_2d_list
coeffs = pywt.dwt2(data, 'haar')
array = []
cA, (cH, cV, cD) = coeffs
# cA
# array([[ 2.,  2.],
#        [ 2.,  2.]])
# cV
# array([[ 0.,  0.],
    #    [ 0.,  0.]])
print(cA)
print(cV)

# print (output_2d_list)
