import tensorflow as tf
import numpy as np

matrix1 = np.array([(2,2,2),(2,2,2),(2,2,2)],dtype='int32')
matrix2 = np.array([(1,1,1),(1,1,1),(1,1,1)],dtype='int32')
matrix3 = np.array([(2,7,2),(1,4,2),(9,0,2)],dtype='float32')

print('matrix1',matrix1)
print('matrix2',matrix2)
print('matrix3',matrix3)

matrix1 = tf.constant(matrix1)
matrix2 = tf.constant(matrix2)

matrix_mul = tf.matmul(matrix1,matrix2)
matrix_det = tf.matrix_determinant(matrix3)

with tf.Session() as sess:
    result1 = sess.run(matrix_mul)
    result2 = sess.run(matrix_det)

print(result1)
print(result2)