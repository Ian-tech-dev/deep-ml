import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	if not np.any(np.array(gradient)):
		magnitude = 0.0
		direction = gradient
		descent_direction = direction
	else: 
		magnitude = np.linalg.norm(np.array(gradient))
		direction = (1/magnitude*(np.array(gradient))).tolist()
		descent_direction = (-1*np.array(direction)).tolist()

	result = {
		'magnitude':magnitude,
		'direction':direction,'descent_direction':descent_direction
		}

	return result
	# Your code here
	pass