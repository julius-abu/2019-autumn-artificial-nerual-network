# -*- coding: utf-8 -*-

import tensorflow as tf
FLAGS = tf.app.flags.FLAGS

class Model:
    def __init__(self,
                 learning_rate=0.001,
                 learning_rate_decay_factor=0.9995):
        self.x_ = tf.placeholder(tf.float32, [None, 32, 32, 3])
        self.y_ = tf.placeholder(tf.int32, [None])

        # TODO:  fill the blank of the arguments
        self.loss, self.pred, self.acc = self.forward(True)
        self.loss_val, self.pred_val, self.acc_val = self.forward(False, reuse=True)

        self.learning_rate = tf.Variable(float(learning_rate), trainable=False, dtype=tf.float32)
        self.learning_rate_decay_op = self.learning_rate.assign(self.learning_rate * learning_rate_decay_factor)

        self.global_step = tf.Variable(0, trainable=False)
        self.params = tf.trainable_variables()
        
        # TODO:  maybe you need to update the parameter of batch_normalization?
        with tf.control_dependencies(tf.get_collection(tf.GraphKeys.UPDATE_OPS)):
            self.train_op = tf.train.AdamOptimizer(self.learning_rate).minimize(self.loss, global_step=self.global_step,
                                                                                var_list=self.params)

        self.saver = tf.train.Saver(tf.global_variables(), write_version=tf.train.SaverDef.V2,
                                    max_to_keep=3, pad_step_number=True, keep_checkpoint_every_n_hours=1.0)

    def forward(self, is_train, reuse=None):
    
        with tf.variable_scope("model", reuse=reuse):
            # TODO: implement input -- Conv -- BN -- ReLU -- Dropout -- MaxPool -- Conv -- BN -- ReLU -- Dropout -- MaxPool -- Linear -- loss
            #        the 10-class prediction output is named as "logits"
            # Your Conv Layer 
            conv1 = tf.layers.conv2d(self.x_, 40, 8, kernel_initializer=tf.truncated_normal_initializer(stddev=0.1))
            # Your BN Layer: use batch_normalization_layer function
            bn1 = batch_normalization_layer(conv1, is_train)
            # Your Relu Layer
            relu1 = tf.nn.relu(bn1)
            # Your Dropout Layer: use dropout_layer function
            drop1 = dropout_layer(relu1, FLAGS.drop_rate, is_train)
            # Your MaxPool
            pool1 = tf.layers.max_pooling2d(drop1, 2, 2)
            # Your Conv Layer ????
            conv2 = tf.layers.conv2d(pool1, 40, 8, kernel_initializer=tf.truncated_normal_initializer(stddev=0.1))
            # Your BN Layer: use batch_normalization_layer function
            bn2 = batch_normalization_layer(conv2, is_train)
            # Your Relu Layer
            relu2 = tf.nn.relu(bn2)
            # Your Dropout Layer: use dropout_layer function
            drop2 = dropout_layer(relu2, FLAGS.drop_rate, is_train)
            # Your MaxPool
            pool2 = tf.layers.max_pooling2d(drop2, 2, 2)
            # Your Linear Layer
            temp = tf.reshape(pool2, [-1, 160])
            logits = tf.layers.dense(temp, units = 10, kernel_initializer=tf.truncated_normal_initializer(stddev=0.1))
            # logits = tf.Variable(tf.constant(0.0, shape=[100, 10]))  # deleted this line after you implement above layers

        loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(labels=self.y_, logits=logits))
        pred = tf.argmax(logits, 1)  # Calculate the prediction result
        correct_pred = tf.equal(tf.cast(pred, tf.int32), self.y_)
        acc = tf.reduce_mean(tf.cast(correct_pred, tf.float32))  # Calculate the accuracy in this mini-batch
        
        return loss, pred, acc

def batch_normalization_layer(incoming, is_train=True):
    # TODO: implement the batch normalization function and applied it on fully-connected layers
    # NOTE:  If isTrain is True, you should use mu and sigma calculated based on mini-batch
    #       If isTrain is False, you must use mu and sigma estimated from training data
    return tf.layers.batch_normalization(incoming, 3, training=is_train)
    
def dropout_layer(incoming, drop_rate, is_train=True):
    # TODO: implement the dropout function and applied it on fully-connected layers
    # Note: When drop_rate=0, it means drop no values
    #       If isTrain is True, you should randomly drop some values, and scale the others by 1 / (1 - drop_rate)
    #       If isTrain is False, remain all values not changed
    return tf.layers.dropout(incoming, drop_rate, training=is_train)
