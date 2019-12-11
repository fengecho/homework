
"""detect_image.py

This script is used to test my whether there are tomatoes in the image, It is modified from the following example from TensorFlow Object Detection API:

https://github.com/tensorflow/models/blob/master/research/object_detection/object_detection_tutorial.ipynb
https://github.com/jkjung-avt/hand-detection-tutorial/blob/master/detect_image.py
"""

import sys
import numpy as np
import cv2
import tensorflow as tf



PATH_TO_FROZEN_GRAPH = 'model_exported/frozen_inference_graph.pb'
#define the score threshold
Threshold = 0.5

def has_tomatoes(image_path):

    # load detection graph
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(PATH_TO_FROZEN_GRAPH, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')

    # define input/output tensors
    image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
    detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
    # load input image
    img = cv2.imread(image_path)
    if img is None:
        sys.exit('failed to load image: %s' % image_path)
    img = img[..., ::-1]  # BGR to RGB

    # run inference
    with detection_graph.as_default():
        with tf.Session() as sess:
            scores = sess.run(
                [detection_scores],
                feed_dict={image_tensor: np.expand_dims(img, 0)})

    #check whether a memebre in the list is bigger than threshold
    if any(i>= Threshold for i in scores[0][0]):
        print("True, there is/are tomatoes")
    else:
        print("No, there is not tomato")






