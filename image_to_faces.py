import face_recognition
from PIL import Image
import matplotlib.pyplot as plt
import os

# dirs
img_dir = 'images'
faces_dir = 'faces'


# create the new directory
if not os.path.exists(faces_dir):
	os.mkdir(faces_dir)


for folder in os.listdir(img_dir):
	if not os.path.isdir(os.path.join(img_dir, folder)):
		continue

	# create new folder in the faces directory
	if not os.path.exists(os.path.join(faces_dir, folder)):
		os.mkdir(os.path.join(faces_dir, folder)

	for image_name in os.listdir(os.path.join(img_dir, folder)):
		if not os.path.isfile(os.path.join(img_dir, folder, image_name)):
			continue

		image=face_recognition.load_image_file(
		    os.path.join(img_dir, folder, image_name))
		face_locations=face_recognition.face_locations(
		    image, number_of_times_to_upsample=0, model='cnn')

		for face_location in locations:
			top, right, bottom, left=face_location
			face_image=image[top:bottom, left:right]
			pil_image=Image.fromarray(face_image)

			# Saving the image
			pil_image.save(os.path.join(faces_dir, folder))
			print(f'Saving image: {image_name} at: {faces_dir}/{folder}')
