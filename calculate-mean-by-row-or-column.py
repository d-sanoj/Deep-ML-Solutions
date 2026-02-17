import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	
	if mode == 'row':
		means = list(np.mean(matrix, axis=1))
	if mode == 'column':
		means = list(np.mean(matrix, axis=0))
	return means