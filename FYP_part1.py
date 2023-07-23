import face_recognition
import cv2
import numpy as np
import pandas as pd
import csv
import os
from datetime import datetime
import FolderScanner as fs


df = pd.DataFrame({
    'Name': [],
    'ID': []
})

def CsvFileCheck():
    try:
        now = datetime.now()
        current_date= now.strftime("%Y-%m-%d")
        df_data = pd.read_csv(current_date+' .csv')
        print(df_data)

    except:
        print("ERROR HANDLED")

def SaveFile():
    try:
        now = datetime.now()
        current_date= now.strftime("%Y-%m-%d")
        df.to_csv(current_date+' .csv', index=False)
    except:
        print("ERROR HANDLED")




folder_path = "E:\FYP\ImageData\CS"
files = fs.get_files_in_folder(folder_path)
fs.get_The_Student_Details(files)

known_faces_names = fs.StudentsData
load_images =  [face_recognition.load_image_file(x) for x in files]
known_face_encoding = [face_recognition.face_encodings(x)[0] for x in load_images]

CsvFileCheck()

video_capture = cv2.VideoCapture(0)

face_locations = []
face_encodings = []
s=True

while True:
    _,frame=video_capture.read()
    small_frame = cv2.resize(frame, (0,0), fx=0.25,fy=0.25)
    rgb_small_frame = small_frame[:,:,::-1]
    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces (known_face_encoding, face_encoding)
            face_distance = face_recognition.face_distance (known_face_encoding, face_encoding)
            best_match_index = np.argmin (face_distance)
            if matches[best_match_index]:
                record = known_faces_names[best_match_index]
                record_exists = (df['Name'] == record['Name']) & (df['ID'] == record['ID'])
                if not record_exists.any():
                    df = df.append(record, ignore_index=True)
                    print("Record added to the DataFrame.")
        cv2.imshow("attendence system", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

SaveFile()
video_capture.release()
cv2.destroyAllWindows()