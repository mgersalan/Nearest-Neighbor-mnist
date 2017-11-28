# nearest-neighbor-minst

Nearest Neighbor function defined manually in Python and used for digit classification using MNIST Data Set. 
mnist-x.data contains 6000 images from MNIST data set as each line represents a 28x28 pixel values in numeric format.
mnist-y.data contains the labels of these images between 0 and 9.
Each image has a pixel value -1 or 1.
Goal is to classify 2 different hand written digits. It could be also extended to classifiying multiple labels or all.

## Implementation
target and opposite variables represents 2 hand written numbers which is going to be classified. For example to classify 2 and 8, target should be set to 2 and opposite should be set to 8 or vica versa. Classification with all labels could be applied with the same algorithm as well.
In the source code target is set to 4 and opposite is set to five. This gives us %98 accuracy. This ratio changes with different values of target and opposite variables.







