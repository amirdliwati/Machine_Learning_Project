##    Y = X + Z
##    Z = Y - X !!!!!!!!!!!!????

import tensorflow as tf

x = tf.constant(4.)
y = tf.constant(12.)
z = tf.Variable(0.)

yy = tf.add(x,z)
deviation = tf.square(y - yy)

train_step = tf.train.GradientDescentOptimizer(0.01).minimize(deviation)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for i in range(1000):
    sess.run(train_step)

print('Estimating of Z:  ' , sess.run(z))