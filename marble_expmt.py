import numpy as np

def is_square_matrix(m):
	return all([len(ms) == len(m) for ms in m])

"""
	m is a matrix of row vectors
	m[i][j] = row i, column j of m
"""
def boolean_matrix_squared(m):
	assert is_square_matrix(m)
	deg = len(m)
	prod = [[0 for i in range(deg)] for j in range(deg)]
	for i in range(deg):
		for j in range(deg):
			prod[i][j] = 1 if any([m[i][k] and m[k][j] for k in range(deg)]) else 0
	return prod

def matrix_times_vector(m, x):
	assert is_square_matrix(m) and len(m) == len(x)
	deg = len(m)
	return [sum([m[i][k] * x[k] for k in range(deg)]) for i in range(deg)]

def marble_expt(matrix, num_clicks, state):
	prod = matrix
	for k in range(num_clicks - 1):
		print("multiplying, k = " + str(k))
		prod = boolean_matrix_squared(prod)
	return matrix_times_vector(prod, state)

# Testing
M = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 0 , 1 ,0]]
X = [6, 2, 1, 5, 3, 10]
print(matrix_times_vector(M, X))
print(boolean_matrix_squared(M))
print([marble_expt(M, i, X) for i in range(5)])