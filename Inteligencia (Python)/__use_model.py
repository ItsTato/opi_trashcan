import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image#type:ignore

model = tf.keras.models.load_model('botellas.h5')#type:ignore

def preprocess_image(img_path, target_size=(512, 512)): # -> np.array:
	img = image.load_img(img_path, target_size=target_size)
	img_array = image.img_to_array(img)
	img_array = np.expand_dims(img_array, axis=0)
	img_array /= 255.0
	return img_array

def predict_image(img_path) -> str:
	img_array = preprocess_image(img_path)
	prediction = model.predict(img_array)
	if prediction[0][0] > 0.5:
		return f"not a bottle (confidence: {round((1-round(float(prediction[0][0]),4))*100,4)}%)"
	else:
		return f"a bottle (confidence: {round((1-round(float(prediction[0][0]),4))*100,4)}%)"

print(f"OREO image is: {predict_image('./073032-3244125699.jpg')}")
print(f"BOTTLE image is: {predict_image('./1000ml-713765796.jpg')}")
