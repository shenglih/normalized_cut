
import numpy as np
import scipy.linalg as la
import scipy.sparse.linalg as sla

def SpectralClustering(W, D, K):
	"""
	W: np.array: word vector?
	D: np.array: degree matrix?
	K: 

	main program of multiclass spectral clustering
	"""
	N = len(W) # number of templates
	# compute degree matrix
	D = np.diag(np.dot(W,[1]*N))
	W = W + 0.1
	print("Step 1 completed")

	# find optimal eigensolution Z^ast by:
	kernel = (D**(-0.5)) @ W @ (D**(-0.5))
	V, S = sla.eigs(kernel) # tol = 1e-3
	Z = np.dot(D**(-0.5), V[:,:K])
	print("Step 2 completed")

	# normalize Z^ast by
	ZZ = np.dot(Z, np.transpose(Z))
	X_tilde_ast = np.dot(np.multiply(ZZ, np.eye(N))**(-0.5), Z)
	print("Step 3 completed")

	return X_tilde_ast



def trace_function(X, J):
	"""
	to calcualte X_t or X_s in eq. 8
	X: numpy array: |E|X|T| entity-template matrix
	J: numpy array: |E|X|S| entity-sentence matrix
	"""
	A = np.dot(np.transpose(J),X)
	return np.trace(np.dot(A, np.transpose(A)))


def discretization(X_tilde_ast, K, N):






	return X_ast
