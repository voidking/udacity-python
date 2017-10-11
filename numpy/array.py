import numpy as np

a = [1, 2, 5, 3, 4]
b = np.array(a)

print('a=',a)
print('b=',b)
print('type(a):',type(a))
print('type(b)',type(b))  
print('b.dtype',b.dtype)
b2 = b.astype(np.float32)
print('b2.dtype',b2.dtype)                   

print('b.shape:', b.shape)                    
print('b.argmax():',b.argmax())                  
print('b.max():',b.max())                     
print('b.mean():',b.mean())            

c = [[1, 2], [3, 4]]    
d = np.array(c)

print('c=',c)
print('d=',d)
print('d.shape:',d.shape) 
print('d.size:',d.size)
print('d.max(axis=0):',d.max(axis=0)) # 找列最大值
print('d.max(axis=1):',d.max(axis=1)) # 找行最大值
print('d.mean(axis=0):',d.mean(axis=0))  # 求列平均数      
print('d.flatten():',d.flatten()) # 展开为一维数组
print('np.ravel(c)',np.ravel(c)) # 展开为一维数组

# 3x3的浮点型2维数组，并且初始化所有元素值为1
e = np.ones((3, 3), dtype=np.float32)
print('e=',e)

# 创建一个一维数组，元素值是把3重复4次，array([3, 3, 3, 3])
f = np.repeat(3, 4)
print('f=',f)

# 2x2x3的无符号8位整型3维数组，并且初始化所有元素值为0
g = np.zeros((2, 2, 3), dtype=np.uint8)
print('g=',g)
print('g.shape',g.shape)

h = g.astype(np.float)  # 用另一种类型表示
print('h=',h)

l = np.arange(10)       # 类似range，array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print('l=',l)

m = np.linspace(0, 6, 5)# 等差数列，0到6之间5个取值，array([ 0., 1.5, 3., 4.5, 6.])
print('m',m)

p = np.array(
    [[1, 2, 3, 4],
     [5, 6, 7, 8]]
)

np.save('p.npy', p)     # 保存到文件
q = np.load('p.npy')    # 从文件读取