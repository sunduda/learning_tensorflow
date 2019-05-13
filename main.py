import tensorflow as tf

x = tf.Variable(3, name="x")
y = tf.Variable(4, name="x")
f = x * x * y + y + 2
