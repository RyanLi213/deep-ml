import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
		new_shape1 = np.array(new_shape)
		new_shape1 = new_shape1.tolist()
		a1 = np.array(a).flatten().tolist()
		if int(new_shape1[0])*int(new_shape1[1] )== len(a1):
			reshaped_matrix = np.reshape(a,new_shape)
			return reshaped_matrix
		else:
			return []