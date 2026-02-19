import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	nparraymatrix = np.array(matrix)
	eigenvalues = np.linalg.eigvals(nparraymatrix)
	return list(eigenvalues)