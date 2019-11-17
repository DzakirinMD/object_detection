import tensorflow as tf
graph_def_file = "C:/tensorflow1/models/research/object_detection/inference_tflite/tflite_graph.pb"
input_arrays = ["normalized_input_image_tensor"]
output_arrays = ["detection_boxes", "detection_classes", "detection_scores", "num_boxes"]

converter = tf.lite.TFLiteConverter.from_frozen_graph(
  graph_def_file,
  input_arrays,
  output_arrays,
  input_shapes={'normalized_input_image_tensor':[1, 300, 300, 3]}

  )
tflite_model = converter.convert()
converter.allow_custom_ops = True
target_ops=TFLITE_BUILTINS,SELECT_TF_OPS
open("converted_model.tflite", "wb").write(tflite_model)