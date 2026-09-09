## الفرق بين placeholder و constant  في البلايس هولدر نستطيع ادخال البيانات أثناء تشغيل البرنامج

import tensorflow as tf

x = tf.placeholder(tf.float32)
y = 2*x**2

var_grad = tf.gradients(y,x)
with tf.Session() as sess:
    var_grad_val = sess.run(var_grad,feed_dict={x:1})

print(var_grad_val)