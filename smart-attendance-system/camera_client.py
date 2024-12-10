import cv2, csv, time, os
import mediapipe as mp
mp_face = mp.solutions.face_detection
out = 'attendance.csv'
os.makedirs('data', exist_ok=True)
out = os.path.join('data', 'attendance.csv')
if not os.path.exists(out):
    with open(out,'w') as f: f.write('ts,faces\n')
cap = cv2.VideoCapture(0)
with mp_face.FaceDetection(model_selection=0, min_detection_confidence=0.5) as detector:
    print('Press q to quit. Logging to', out)
    while True:
        ret, frame = cap.read()
        if not ret: break
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        res = detector.process(img)
        faces = res.detections or []
        for d in faces:
            bbox = d.location_data.relative_bounding_box
            h,w,_ = frame.shape
            x = int(bbox.xmin * w); y = int(bbox.ymin * h)
            ww = int(bbox.width * w); hh = int(bbox.height * h)
            cv2.rectangle(frame, (x,y), (x+ww, y+hh), (0,255,0), 2)
        ts = int(time.time())
        with open(out,'a') as f: f.write(f"{ts},{len(faces)}\n")
        cv2.imshow('Attendance', frame)
        if cv2.waitKey(200) & 0xFF == ord('q'):
            break
cap.release(); cv2.destroyAllWindows()