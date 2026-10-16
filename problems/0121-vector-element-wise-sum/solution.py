def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	# Return the element-wise sum of vectors 'a' and 'b'.
	# If vectors have different lengths, return -1.
	if len(a) == len(b):
		new_list = []
		for i in range(len(a)):
				new_list.append(a[i]+b[i])
	else:
		new_list = -1
	return new_list