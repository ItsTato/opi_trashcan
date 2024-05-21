import tensorflow
from tensorflow.keras.preprocessing.image import ImageDataGenerator#type:ignore
from tensorflow.keras.applications import MobileNetV2#type:ignore
from tensorflow.keras.models import Sequential#type:ignore
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D#type:ignore

import os
from os import path

import tqdm

data_dir:str = path.join(".","data")
valid_img_ext:list[str] = [".jpg",".jpeg",".png",".bmp"]# ,".gif"] xd. me di cuenta que no tengo gifs haha

def filter_directory(dir:str) -> None:
	all_files:list[str] = []
	for root, _, files in os.walk(dir):
		for file in files: all_files.append(os.path.join(root, file))
	for file_path in tqdm.tqdm(all_files, desc="Filtering", unit="files", ascii=False):
		if not any(file_path.lower().endswith(ext) for ext in valid_img_ext):
			os.remove(file_path)
			print(f"Begone! Eliminated {file_path}.")
	print(f"Filtering for {dir} ended.")

filter_directory(path.join(".","data"))

train_datagen = ImageDataGenerator(rescale=1.0/255,validation_split=0.2)
train_generator = train_datagen.flow_from_directory(
	data_dir,
	target_size=(512,512),
	batch_size=32,
	class_mode="binary",
	subset="training"
)

validation_generator = train_datagen.flow_from_directory(
	data_dir,
	target_size=(512,512),
	batch_size=32,
	class_mode="binary",
	subset="validation"
)

base_model:MobileNetV2 = MobileNetV2(input_shape=(512,512,3),include_top=False,weights="imagenet")
base_model.trainable = False

model:Sequential = Sequential([
	base_model,
	GlobalAveragePooling2D(),
	Dense(1,activation="sigmoid")
])

model.compile(optimizer="adam",loss="binary_crossentropy",metrics=["accuracy"])

model.fit(
	train_generator,
	validation_data=validation_generator,
	epochs=1
)

model.save("botellas.h5")
