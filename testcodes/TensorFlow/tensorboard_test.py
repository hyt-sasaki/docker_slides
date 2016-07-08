# -*- coding:utf-8 -*-
import tensorflow as tf


def inference(input_placeholder):
    with tf.name_scope('hidden_layer'):
        W = tf.Variable(tf.zeros([784, 10]), name='Weights')
        b = tf.Variable(tf.zeros([10]), name='bias')
        y = tf.nn.softmax(tf.matmul(input_placeholder, W) + b)

        tf.histogram_summary('Weights', W)
        tf.histogram_summary('bias', b)
        tf.histogram_summary('outputs', y)

    return y


def loss(output, labels_placeholder):
    with tf.name_scope('cross_entropy'):
        cross_entropy =\
            -tf.reduce_sum(labels_placeholder * tf.log(output))
        tf.scalar_summary('cross entropy', cross_entropy)
    return cross_entropy


def accuracy(labels_placeholder, inference):
    with tf.name_scope('test'):
        correct_prediction = tf.equal(
            tf.arg_max(inference, 1), tf.argmax(labels_placeholder, 1)
        )
        acc = tf.reduce_mean(tf.cast(correct_prediction, 'float'))
        tf.scalar_summary('accuracy', acc)
        return acc


def training(loss, learning_rate):
    with tf.name_scope('train'):
        train_step = \
            tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)

    return train_step


if __name__ == '__main__':
    from tensorflow.examples.tutorials.mnist import input_data

    flags = tf.app.flags
    FLAGS = flags.FLAGS
    flags.DEFINE_integer('max_steps', 1000, 'Number of steps to run trainer.')
    flags.DEFINE_float('learning_rate', 0.01, 'Initial learning rate.')

    mnist = input_data.read_data_sets('/tmp/data/', one_hot=True)

    labels_ph = tf.placeholder('float', [None, 10], 'labels')
    inputs_ph = tf.placeholder('float', [None, 784], 'inputs')

    with tf.Session() as sess:
        output = inference(inputs_ph)
        loss = loss(output, labels_ph)
        acc = accuracy(labels_ph, output)
        training_op = training(loss, FLAGS.learning_rate)

        merged = tf.merge_all_summaries()
        writer = tf.train.SummaryWriter('/tmp/mnist_logs', sess.graph)
        init = tf.initialize_all_variables()
        sess.run(init)

        for step in range(FLAGS.max_steps):
            if step % 10 == 0:
                feed = {
                    inputs_ph: mnist.test.images,
                    labels_ph: mnist.test.labels
                }
                result = sess.run([merged, acc], feed_dict=feed)
                summary_str = result[0]
                acc_str = result[1]
                writer.add_summary(summary_str, step)
                print 'Accuracy rate at step %s: %s' % (step, acc_str)
            else:
                batch_xs, batch_ys = mnist.train.next_batch(100)
                feed = {inputs_ph: batch_xs, labels_ph: batch_ys}
                sess.run(training_op, feed_dict=feed)
