def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	result = []
	for i in matrix:
		res =[]
		for j in i:
			res.append(j*scalar)
		result.append(res)
	return result
	pass