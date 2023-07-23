import face_recognition
import cv2
import numpy as np
import pandas as pd
import csv
import os
from datetime import datetime
import FolderScanner as fs


folder_path = "E:\FYP\ImageData\CS"
files = fs.get_files_in_folder(folder_path)
fs.get_The_Student_Details(files)

known_faces_names = fs.StudentsData
load_images =  [face_recognition.load_image_file(x) for x in files]
known_face_encoding = [face_recognition.face_encodings(x)[0] for x in load_images]
 
video_capture = cv2.VideoCapture(0)

# students = known_faces_names.copy()

# face_locations = []
# face_encodings = []
# face_names = []
# s=True
# now = datetime.now()
# current_date= now.strftime("%Y-%m-%d")
# f = open(current_date+' .csv', 'w+',newline = '')
# Inwriter = csv.writer(f)






# while True:
#     _,frame=video_capture.read()
#     small_frame = cv2.resize(frame, (0,0), fx=0.25,fy=0.25)
#     rgb_small_frame = small_frame[:,:,::-1]
#     if s:
#         face_locations = face_recognition.face_locations(rgb_small_frame)
#         face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
#         face_names = []
#         for face_encoding in face_encodings:
#             matches = face_recognition.compare_faces (known_face_encoding, face_encoding)
#             name=""
#             face_distance = face_recognition.face_distance (known_face_encoding, face_encoding)
#             best_match_index = np.argmin (face_distance)
#             if matches[best_match_index]:
#                 name = known_faces_names[best_match_index]
#             face_names.append(name)
#             if name in known_faces_names:
#                 if name in students:
#                     students.remove(name)
#                     print (students)
#                     current_time = now.strftime("%H-%m-%S")
#                     Inwriter.writerow([name, current_time])

#         cv2.imshow("attendence system", frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

# video_capture.release()
# cv2.destroyAllWindows()
# f.close()