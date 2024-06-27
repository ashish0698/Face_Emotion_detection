
##This code runs in python output terminal not in browswer

# import cv2
# from keras.models import model_from_json
# import numpy as np

# json_file = open("emotiondetector.json", "r")
# model_json = json_file.read()
# json_file.close()
# model = model_from_json(model_json)

# model.load_weights("emotiondetector.h5")
# haar_file = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
# face_cascade = cv2.CascadeClassifier(haar_file)

# def extract_features(image):
#     feature = np.array(image)
#     feature = feature.reshape(1, 48, 48, 1)
#     return feature / 255.0

# webcam = cv2.VideoCapture(0)
# labels = {0: 'angry', 1: 'disgust', 2: 'fear', 3: 'happy', 4: 'neutral', 5: 'sad', 6: 'surprise'}

# while True:
#     i, im = webcam.read()
#     gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(im, 1.3, 5)

#     try:
#         for (p, q, r, s) in faces:
#             image = gray[q:q + s, p:p + r]
#             cv2.rectangle(im, (p, q), (p + r, q + s), (255, 0, 0), 2)
#             image = cv2.resize(image, (48, 48))
#             img = extract_features(image)
#             pred = model.predict(img)
#             prediction_label = labels[pred.argmax()]

#             # Set color based on emotion
#             if prediction_label == 'neutral':
#                 text_color = (0, 255, 0)  # Green
#             elif prediction_label == 'sad':
#                 text_color = (0, 0, 255)  # Red
#             elif prediction_label == 'happy':
#                 text_color = (255, 255, 0)  # Yellow
#             elif prediction_label == 'surprise':
#                 text_color = (0, 255, 255)  # Cyan
#             else:
#                 text_color = (0, 0, 255)  # Default to Red

#             cv2.putText(im, '% s' % (prediction_label), (p - 10, q - 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2,
#                         text_color)

#         cv2.imshow("Output", im)
#         cv2.waitKey(27)
#     except cv2.error:
#         pass
