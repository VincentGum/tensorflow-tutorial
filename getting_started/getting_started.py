import tensorflow as tf

node1 = tf.constant(3.0, dtype=tf.float32)
node2 = tf.constant(4.0)

print(node1, node2)

sess = tf.Session()
print(sess.run([node1, node2]))

node3 = tf.add(node1, node2)
print("node3: ", node3)
print("sess.run(node3): ", sess.run(node3))

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b

print(sess.run(adder_node, feed_dict={a: 3, b: 4.5}))
print(sess.run(adder_node, feed_dict={a: [1, 3], b: [2, 4]}))

add_and_triple = adder_node * 3
print(sess.run(add_and_triple, feed_dict={a: 3, b: 4.5}))

W = tf.Variable(0.3)
b = tf.Variable(-0.3)
x = tf.placeholder(tf.float32)
linear_model = tf.multiply(W, x) + b

init = tf.global_variables_initializer()
sess.run(init)

print(sess.run(linear_model, feed_dict={x: [1, 2, 3, 4]}))

y = tf.placeholder(tf.float32)
squared_deltas = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_deltas)
print(sess.run(loss, feed_dict={x: [1, 2, 3, 4], y: [0, -1, -2, -3]}))

fixW = tf.assign(W, -1)
fixB = tf.assign(b, 1)
sess.run([fixW, fixB])
print(sess.run([W, b]))
print(sess.run(loss, feed_dict={x: [1, 2, 3, 4], y: [0, -1, -2, -3]}))

optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

sess.run(init)
for i in range(1000):
    sess.run(train, feed_dict={x: [1, 2, 3, 4], y: [0, -1, -2, -3]})

print(sess.run([W, b]))
