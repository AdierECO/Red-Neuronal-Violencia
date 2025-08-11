import cv2
import numpy as np
from tensorflow.keras.models import load_model

class ViolenceDetector:
    def __init__(self, model_path="models/trained_model.h5"):
        self.model = load_model(model_path)
        self.input_shape = self.model.input_shape[1:3]
        self.violence_threshold = 0.7  # Umbral para considerar violencia
        
    def preprocess_frame(self, frame):
        """Preprocesa un frame para la red neuronal"""
        frame = cv2.resize(frame, self.input_shape)
        frame = frame / 255.0  # Normalización
        return np.expand_dims(frame, axis=0)
    
    def detect_violence(self, frame):
        """Detecta violencia en un frame"""
        processed_frame = self.preprocess_frame(frame)
        prediction = self.model.predict(processed_frame)[0][0]
        return prediction > self.violence_threshold, prediction
    
    def run_realtime_detection(self, camera_index=0):
        """Ejecuta la detección en tiempo real desde la cámara"""
        cap = cv2.VideoCapture(camera_index)
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
                
            is_violence, confidence = self.detect_violence(frame)
            
            # Mostrar resultado
            label = "VIOLENCE" if is_violence else "No violence"
            color = (0, 0, 255) if is_violence else (0, 255, 0)
            
            cv2.putText(frame, f"{label} ({confidence:.2f})", 
                        (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 
                        1, color, 2, cv2.LINE_AA)
            
            cv2.imshow("Violence Detection", frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    detector = ViolenceDetector()
    detector.run_realtime_detection()