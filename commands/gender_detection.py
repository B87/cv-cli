import cv2
import numpy as np
import time

from commands.base import BaseCommand
from core.results import ImageResult, ImageBox



class GenderDetection(BaseCommand):
	
	MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
	gender_list = ['male', 'female']
	padding = 20

	face_cascade = cv2.CascadeClassifier("data/models/haarcascade_frontalface_alt.xml")

	gender_net = cv2.dnn.readNet('data/models/gender_net.caffemodel', 'data/models/deploy_gender.prototxt')
	face_net = cv2.dnn.readNet('data/models/opencv_face_detector_uint8.pb', 'data/models/opencv_face_detector.pbtxt')

	def cli_str_key(self) -> str:
		return 'gender-detection'

	def processImage(self, image) -> ImageResult:
		image_boxes = []
		frame_face, bboxes = self.getFaceBox(image)
		if not bboxes:
			print("No face Detected, Checking next frame")

		for bbox in bboxes:
			face = image[max(0, bbox[1]-self.padding) : min( bbox[3]+self.padding, image.shape[0]-1 ), max( 0, bbox[0]- self.padding ) : min( bbox[2]+self.padding, image.shape[1]-1 )]
			blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), self.MODEL_MEAN_VALUES, swapRB=False)
			self.gender_net.setInput(blob)
			gender_preds = self.gender_net.forward()
			gender = self.gender_list[gender_preds[0].argmax()]

			image_boxes.append(ImageBox(bbox[0], bbox[1], bbox[2], bbox[3], [gender]))

			print("Gender : {}, conf = {:.3f}".format(gender, gender_preds[0].max()))
			
			label = "{}".format(gender)
			cv2.putText(frame_face, label, (bbox[0], bbox[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2, cv2.LINE_AA)
			cv2.imshow("Age Gender Demo", frame_face)
		return ImageResult(image, image_boxes)

	def getFaceBox(self, frame, conf_threshold=0.7):
		frameOpencvDnn = frame.copy()
		frameHeight = frameOpencvDnn.shape[0]
		frameWidth = frameOpencvDnn.shape[1]
		blob = cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)
		self.face_net.setInput(blob)
		detections = self.face_net.forward()
		bboxes = []
		for i in range(detections.shape[2]):
			confidence = detections[0, 0, i, 2]
			if confidence > conf_threshold:
				x1 = int(detections[0, 0, i, 3] * frameWidth)
				y1 = int(detections[0, 0, i, 4] * frameHeight)
				x2 = int(detections[0, 0, i, 5] * frameWidth)
				y2 = int(detections[0, 0, i, 6] * frameHeight)
				bboxes.append([x1, y1, x2, y2])
				cv2.rectangle(frameOpencvDnn, (x1, y1), (x2, y2), (0, 255, 0), int(round(frameHeight/150)), 8)
		return frameOpencvDnn, bboxes
		# Convert from rgb to grey scaled image		
		#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		#faces = face_cascade.detectMultiScale(gray, 1.1, 4)
		#if(len(faces)>0):
		#	print("Found %s faces" % (str(len(faces))))

		#for (x, y, w, h ) in faces:
			# Get Face 
			#face_img = image[y:y+h, h:h+w].copy()
			#blob = cv2.dnn.blobFromImage(face_img, 1, (227, 227), MODEL_MEAN_VALUES, swapRB=False)

			#Predict Gender
			#gender_net.setInput(blob)
			#gender_preds = gender_net.forward()
			#gender = gender_list[gender_preds[0].argmax()]
			#print("Gender : " + gender)

			# crop image
			#crop_img = image[y:y+h, x:x+w].copy()

	