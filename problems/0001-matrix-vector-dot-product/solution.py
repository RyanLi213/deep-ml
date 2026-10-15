import numpy as np

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	A = np.array(a)
	B = np.array(b)
	a1 = A.shape[1]
	b1 = B.shape[0]
	if a1 == b1:
		c = A @ b
		return c
	else:
		return -1

	pass