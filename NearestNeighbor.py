import pandas as pd

images = pd.read_table("/Users/Gur/Desktop/AI/NN/mnist-x.data",header = None)
labels = pd.read_table("/Users/Gur/Desktop/AI/NN/mnist-y.data",header = None)

images = images[0]
labels = labels[0]
splitted_images = []

for i in range(0,len(images)):
    splitted_images.append((images.get(i).split(','),labels.get(i)))

training_images = splitted_images[:5000]
test_images = splitted_images[-1000:]



target = 4;
opposite = 5;

opposite_cluster =[]
target_cluster = []
test_cluster = []

for tup in training_images:
    if tup[1] == target:
        target_cluster.append(tup)
    if tup[1] == opposite:
        opposite_cluster.append(tup)

for tup in test_images:
    if tup[1] == target or tup[1] == opposite :
        test_cluster.append(tup)




def nearest_neighbor(test_vector):
    test_vector = [int(x) for x in test_vector]
    nearest_target = 9999;
    target_label = target_cluster[0][1]
    opposite_label = opposite_cluster[0][1]

    target_cluster_vectors = [x[0] for x in target_cluster]
    opposite_cluster_vectors = [x[0] for x in opposite_cluster]

    for vector in target_cluster_vectors:
        vector = [int(x) for x in vector]
        distance_target = 0;
        for i in range(0,len(vector)):
            distance_target = distance_target + abs((test_vector[i] - vector[i]))
        if distance_target < nearest_target:
            nearest_target = distance_target

    nearest_opposite = 9999;

    for vector in opposite_cluster_vectors:
        vector = [int(x) for x in vector]
        distance_opposite = 0;
        for i in range(0,len(vector)):
            distance_opposite = distance_opposite + abs((test_vector[i] - vector[i]))
        if distance_opposite < nearest_opposite:
            nearest_opposite = distance_opposite

    if nearest_target < nearest_opposite:
        return target_label
    elif nearest_target > nearest_opposite:
        return opposite_label


my_test = test_cluster[1]
test_label = test_cluster[0][1]
rest = nearest_neighbor(my_test[0])

## test
right_guess = 0
wrong_guess = 0
for i in range (0,len(test_cluster)):

    test_vector = test_cluster[i][0]
    test_label = test_cluster[i][1]
    guess = nearest_neighbor(test_vector)

    if guess == int(test_label):
        right_guess = right_guess + 1
    elif guess != int(test_label):
        wrong_guess = wrong_guess + 1


print ("Accuracy is = ",right_guess / (right_guess + wrong_guess))
