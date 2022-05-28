"""
Given an n x n 2D matrix, rotate it 90 degrees clockwise.
"""

def rotate_2d_matrix(matrix):
    rotate_matrix = []
    for i in range(0, len(matrix)):
        rotate_matrix.append([j[i] for j in reversed(matrix)])
    matrix.clear()
    matrix += rotate_matrix