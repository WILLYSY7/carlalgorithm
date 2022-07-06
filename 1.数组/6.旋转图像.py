'''

涉及到的题目
leetcode 48

'''
'''
leetcode 48
48. 旋转图像
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。

示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[7,4,1],[8,5,2],[9,6,3]]

示例 2：
输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        offset = n//2 - 1
        for os in range(offset+1):
            '''找出每一圈的四个顶角，并逐圈缩小'''
            A = [os, os]
            B = [os, n-1-os]
            C = [n-1-os, os]
            D = [n-1-os, n-1-os]
            for _ in range(n-2*os-1):
                '''四个顺次交换位置，完成顺时针90度翻转'''
                matrix[A[0]][A[1]], matrix[B[0]][B[1]], matrix[C[0]][C[1]], matrix[D[0]][D[1]] = \
                matrix[C[0]][C[1]], matrix[A[0]][A[1]], matrix[D[0]][D[1]], matrix[B[0]][B[1]]
                '''更新顶角位置继续完成翻转'''
                A[1] += 1
                B[0] += 1
                C[0] -= 1
                D[1] -= 1
                # print(matrix)