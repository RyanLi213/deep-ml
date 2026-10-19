import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	
	def dot_product(vec1, vec2):
		sum1 = 0
		for i in range(len(vec1)):
	
			sum1 += vec1[i]*vec2[i]
		return sum1

	if len(v1) == len(v2):
		c = dot_product(v1,v2)
		d = c/(np.linalg.norm(v1)*np.linalg.norm(v2))
	else:
		raise ValueError
	
	return d