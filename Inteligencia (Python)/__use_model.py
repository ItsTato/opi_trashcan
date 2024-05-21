import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image#type:ignore
import sys

# Load the trained model
model = tf.keras.models.load_model('botellas.h5')#type:ignore

def preprocess_image(img_path, target_size=(512, 512)):
	"""
	Load and preprocess an image for prediction.
	Args:
		img_path (str): Path to the image.
		target_size (tuple): Target size for the image.
	Returns:
		np.array: Preprocessed image.
	"""
	img = image.load_img(img_path, target_size=target_size)
	img_array = image.img_to_array(img)
	img_array = np.expand_dims(img_array, axis=0)
	img_array /= 255.0
	return img_array

def predict_image(img_path) -> str:
	img_array = preprocess_image(img_path)
	prediction = model.predict(img_array)
	if prediction[0][0] > 0.5:
		return f"not a bottle (confidence: {(1-round(float(prediction[0][0]),4))*100}%)"
	else:
		return f"a bottle (confidence: {(1-round(float(prediction[0][0]),4))*100}%)"

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python predict.py <path_to_image>")
		sys.exit(1)

	img_path = sys.argv[1]
	result = predict_image(img_path)
	print(f"The image is: {result}")
