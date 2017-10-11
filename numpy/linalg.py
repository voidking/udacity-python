import numpy as np

a = np.array([3, 4])
print('a=',a)
# 求范数，默认二范数，平方和开平方
print('np.linalg.norm(a) = ',np.linalg.norm(a))

# 求范数，一范数，绝对值求和
print('np.linalg.norm(a,ord=1) = ',np.linalg.norm(a,ord=1))

# 求范数，无穷范数，绝对值中的最大者
print('np.linalg.norm(a,ord=np.inf) = ',np.linalg.norm(a,ord=np.inf))

b = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
c = np.array([1, 0, 1])

# 矩阵和向量之间的乘法
np.dot(b, c)                    # array([ 4, 10, 16])
np.dot(c, b.T)                  # array([ 4, 10, 16])

np.trace(b)                     # 求矩阵的迹，15
np.linalg.det(b)                # 求矩阵的行列式值，0
np.linalg.matrix_rank(b)    # 求矩阵的秩，2，不满秩，因为行与行之间等差

d = np.array([
    [2, 1],
    [1, 2]
])

'''
对正定矩阵求本征值和本征向量
本征值为u，array([ 3.,  1.])
本征向量构成的二维array为v，
array([[ 0.70710678, -0.70710678],
       [ 0.70710678,  0.70710678]])
是沿着45°方向
eig()是一般情况的本征值分解，对于更常见的对称实数矩阵，
eigh()更快且更稳定，不过输出的值的顺序和eig()是相反的
'''
u, v = np.linalg.eig(d)

# Cholesky分解并重建
l = np.linalg.cholesky(d)

'''
array([[ 2.,  1.],
       [ 1.,  2.]])
'''
np.dot(l, l.T)

e = np.array([
    [1, 2],
    [3, 4]
])

# 对不镇定矩阵，进行SVD分解并重建
U, s, V = np.linalg.svd(e)

S = np.array([
    [s[0], 0],
    [0, s[1]]
])

'''
array([[ 1.,  2.],
       [ 3.,  4.]])
'''
np.dot(U, np.dot(S, V))