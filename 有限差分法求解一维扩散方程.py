# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 11:13:12 2023

@author: 86319
"""

import math

# 定义f(x)函数
def f(x):
    return math.pow(math.e, x)

# 定义主函数
def main():
    n = 11
    m = 101  # 总时长除以时间间隔
    P1 = 2
    P2 = 0  # 常系数，网格密度和边界条件的系数有关
    b1, b2, a1, a2, c1, c2 = 1, -1, 1, 1, 0, 0
    h = 0.1
    dt = 0.1
    B = [0] * n
    max = 0
    Max = 1
    A = [[0] * n for i in range(n)]
    # 系数矩阵导入完毕
    A[0][0] = b1 * P1 + h * a1
    A[0][1] = -b1
    A[n - 1][n - 1] = b2 * P1 + h * a2
    A[n - 1][n - 2] = -b2
    for i in range(1, n - 1):
        A[i][i] = 2 * P1
        A[i][i - 1] = -1
        A[i][i + 1] = -1
    # 用来存储解，第一个维度表示位置，第二个维度表示时间
    u = [[0] * m for i in range(n)]
    # 赋初值
    for i in range(n):
        u[i][0] = f(i * h)
    # 接下来应用雅可比迭代解方程
    for i in range(n):
        for j in range(1, 100):
            u[i][j] = 0
    for T in range(100):  # 循环时间
        zj = [0] * n  # 中间值
        B[0] = (b1 * P2 - h * a1) * u[0][T] + b1 * u[1][T] + 2 * h * c1
        B[10] = b2 * u[9][T] + (b2 * P2 - h * a2) * u[10][T] + 2 * h * c2
        for i in range(1, n - 1):
            B[i] = u[i - 1][T] + 2 * P2 * u[i][T] + u[i + 1][T]
        while Max >= 1e-4:
            for l in range(n):
                zj[l] = u[l][T + 1]
                u[l][T + 1] = 0
            for r in range(n):
                u[r][T + 1] = u[r][T + 1] + (B[r] / A[r][r])
                for p in range(n):
                    if p != r:
                        u[r][T + 1] = u[r][T + 1] - ((A[r][p] / A[r][r]) * zj[p])
            for o in range(n):
                if max < abs(u[o][T + 1] - zj[o]):
                    max = abs(u[o][T + 1] - zj[o])  # 寻找插值绝对值的最大值
            Max = max
            max = 0
        # 整个while语句结束后我们会获得当前时间节点的解
        Max = 1  # 赋值以便开始下一次循环
        if (T + 1) % 10 == 0:
            print("时间：      u值：       坐标：       真值：     ")
            for i in range(n):
                print((T + 1) * dt, u[i][T + 1], i * h, math.pow(math.e, i * h + 0.1 * (T + 1) * dt))
main()