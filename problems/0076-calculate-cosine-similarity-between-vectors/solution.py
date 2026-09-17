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
	if len(v1) != len(v2):
		raise ValueError("Please ensure the vectors have the same dimensions")
	elif np.all(v1 ==0) or np.all(v2==0):
		raise ValueError("Zero vector present")
	else:
		dot_product = v1 @ v2
		l2_v1 = np.linalg.norm(v1)
		l2_v2 = np.linalg.norm(v2)
		result = dot_product/(l2_v1*l2_v2)
		return result
	pass