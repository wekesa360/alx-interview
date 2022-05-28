"""
Given an n x n 2D matrix, rotate it 90 degrees clockwise.
"""

def rotate_2d_matrix(matrix):
    rotated_matrix = []
    m_len = len(matrix)
    for i in range(m_len):
        for m in matrix:
            rotated_matrix.append(m[i])
        n = rotated_matrix[::-1]
    n_len = len(n)
    chunk_size = len(matrix[0])
    rotated_matrix = list()
    for i in range(0, n_len, chunk_size):
        rotated_matrix.append(n[i:i+chunk_size])
