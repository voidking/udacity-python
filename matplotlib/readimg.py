import matplotlib.pyplot as plt

# 读取图片并显示
plt.figure('A image')
result_img = plt.imread('result.png')
plt.imshow(result_img)

# # Z是上小节生成的随机图案，img0就是Z，img1是Z做了个简单的变换
# img0 = Z
# img1 = 3*Z + 4

# # cmap指定为'gray'用来显示灰度图
# fig = plt.figure('Auto Normalized Visualization')
# ax0 = fig.add_subplot(121)
# ax0.imshow(img0, cmap='gray')

# ax1 = fig.add_subplot(122)
# ax1.imshow(img1, cmap='gray')

plt.show()