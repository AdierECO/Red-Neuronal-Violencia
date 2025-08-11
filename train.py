import os
import cv2
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
from utils.video_processor import prepare_dataset

# Configuración
INPUT_SHAPE = (224, 224, 3)
BATCH_SIZE = 32
EPOCHS = 20
DATA_DIR = "data/processed"
MODEL_PATH = "models/trained_model.h5"

def build_yolo_like_model(input_shape):
    """Construye un modelo inspirado en YOLO para clasificación binaria"""
    model = Sequential()
    
    # Capas convolucionales
    model.add(Conv2D(64, (7, 7), strides=(2, 2), padding='same', 
                     activation='relu', input_shape=input_shape))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Conv2D(192, (3, 3), padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Conv2D(128, (1, 1), padding='same', activation='relu'))
    model.add(Conv2D(256, (3, 3), padding='same', activation='relu'))
    model.add(Conv2D(256, (1, 1), padding='same', activation='relu'))
    model.add(Conv2D(512, (3, 3), padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    # Capas completamente conectadas
    model.add(Flatten())
    model.add(Dense(4096, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(1, activation='sigmoid'))
    
    return model

def load_and_preprocess_data(data_dir):
    """Carga y preprocesa los datos de imágenes"""
    violent_dir = os.path.join(data_dir, "violent")
    non_violent_dir = os.path.join(data_dir, "non_violent")
    
    violent_images = [os.path.join(violent_dir, f) for f in os.listdir(violent_dir) 
                     if f.endswith(('.jpg', '.jpeg', '.png'))]
    non_violent_images = [os.path.join(non_violent_dir, f) for f in os.listdir(non_violent_dir) 
                         if f.endswith(('.jpg', '.jpeg', '.png'))]
    
    X = []
    y = []
    
    for img_path in violent_images:
        img = cv2.imread(img_path)
        if img is not None:
            img = cv2.resize(img, (INPUT_SHAPE[0], INPUT_SHAPE[1]))
            X.append(img)
            y.append(1)  # 1 para violencia
    
    for img_path in non_violent_images:
        img = cv2.imread(img_path)
        if img is not None:
            img = cv2.resize(img, (INPUT_SHAPE[0], INPUT_SHAPE[1]))
            X.append(img)
            y.append(0)  # 0 para no violencia
    
    X = np.array(X) / 255.0  # Normalización
    y = np.array(y)
    
    return train_test_split(X, y, test_size=0.2, random_state=42)

def train():
    # Preparar el dataset si no existe
    if not os.path.exists(DATA_DIR):
        print("Preparing dataset...")
        prepare_dataset("data/violent", "data/non_violent", DATA_DIR)
    
    # Cargar y dividir datos
    X_train, X_test, y_train, y_test = load_and_preprocess_data(DATA_DIR)
    
    # Data augmentation
    datagen = ImageDataGenerator(
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest'
    )
    
    # Construir y compilar el modelo
    model = build_yolo_like_model(INPUT_SHAPE)
    model.compile(optimizer=Adam(learning_rate=0.001),
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    
    # Entrenamiento
    history = model.fit(
        datagen.flow(X_train, y_train, batch_size=BATCH_SIZE),
        steps_per_epoch=len(X_train) // BATCH_SIZE,
        epochs=EPOCHS,
        validation_data=(X_test, y_test)
    )
    
    # Guardar modelo
    model.save(MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")
    
    return history

if __name__ == "__main__":
    train()