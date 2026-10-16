import numpy as np

def calculate_dot_product(vec1, vec2):
	"""
	Calculate the dot product of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The dot product of the two vectors.
	"""
	# Your code here
	d= 0
	vec11= vec1.tolist()
	vec22= vec2.tolist()
	for i in range(len(vec11)):
		c = vec11[i] * vec22[i]
		d += c
	return d