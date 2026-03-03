import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:

	final_ip = np.array(X)
	y = np.array(y).reshape(-1, 1)

	transpose = np.transpose(final_ip)

	A = np.dot(transpose, final_ip)
	A_inverse = np.linalg.inv(A)

	B = np.dot(transpose, y)

	theta = np.round(A_inverse.dot(transpose).dot(y), 4).flatten().tolist()

	return theta