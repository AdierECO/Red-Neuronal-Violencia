from flask import Flask, render_template, Response
import cv2
from realtime_detection import ViolenceDetector

app = Flask(__name__)
detector = ViolenceDetector()

def generate_frames():
    camera = cv2.VideoCapture(0)
    
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            is_violence, confidence = detector.detect_violence(frame)
            
            # Añadir anotación al frame
            label = "VIOLENCE" if is_violence else "No violence"
            color = (0, 0, 255) if is_violence else (0, 255, 0)
            
            cv2.putText(frame, f"{label} ({confidence:.2f})", 
                        (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 
                        1, color, 2, cv2.LINE_AA)
            
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), 
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)