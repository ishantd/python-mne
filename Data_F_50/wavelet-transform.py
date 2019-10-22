import os
import numpy as np
import pywt
data = np.ones((4,4), dtype=np.float64)
coeffs = pywt.dwt2(data, 'haar')
# array = []
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

# Iterates over all files contained within the same folder as the python script.
for filename in os.listdir(current_working_directory):
    if filename.endswith('.txt') or filename.endswith('.py'):

        # Ensuring that if something goes wrong during read, that the program exits gracefully.
        # try:
            for i in range (1,2):
                filename = "Data_F_Ind000" + str(i) + ".txt"
                print(filename)
                with open(filename, 'r') as current_file:

                    # Reads each line of the file, and creates a 1d list of each point: e.g. [1,2].
                    for line in current_file.readlines():
                        point = line.split(', ')
                        x = float(point[0])
                        y = float(point[1])
                        point_as_array = [x, y]
                        output_2d_list.append(point_as_array)
        # except IOError:
            # print ("Something went wrong when attempting to read file.")

# For testing purposes to see the output of the script.
# In production, you would be working with output_2d_list as a variable instead.
print (output_2d_list)
