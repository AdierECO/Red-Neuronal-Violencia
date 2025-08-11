# **👁️ Sistema de Detección de Violencia en Tiempo Real**  
### *Detección de agresiones usando IA y visión por computadora*  

---

## **🛠 Tecnologías Utilizadas**  

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" alt="TensorFlow">
  <img src="https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white" alt="Keras">
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/YOLO-00FFFF?style=for-the-badge&logo=yolo&logoColor=black" alt="YOLO">
</p>

---

## **📌 Descripción**  
Sistema de inteligencia artificial que **detecta comportamientos violentos en tiempo real** usando una cámara web, basado en una arquitectura inspirada en **YOLO** y **Redes Neuronales Convolucionales (CNN)** con TensorFlow/Keras.  

✔ **Detección en tiempo real** (30+ FPS)  
✔ **Modelo pre-entrenado** incluido (`.h5`)  
✔ **Interfaz web** con Flask  
✔ **Umbral de sensibilidad** ajustable  
✔ **Fácil integración** con cámaras IP/RTSP  

---

## **📂 Estructura del Proyecto**  

```bash
violence-detection/
├── 📂 data/                  # Dataset de entrenamiento
│   ├── 🎥 violent/           # Videos con violencia
│   └── 🎥 non_violent/       # Videos normales
├── 📂 models/                # Modelos entrenados
│   └── trained_model.h5     # Modelo pre-entrenado
├── 📂 templates/             # Interfaz web (HTML/CSS)
│   └── index.html         
├── 📂 utils/                 # Herramientas
│   └── video_processor.py   # Procesamiento de video
├── 🐍 app.py                 # Servidor Flask
├── 🐍 realtime_detection.py  # Detección por cámara
├── 🐍 train.py               # Script de entrenamiento
└── 📝 requirements.txt       # Dependencias
```

---

## **⚙️ Instalación**  

1. **Clonar repositorio**:
   ```bash
   git clone https://github.com/tuusuario/violence-detection.git
   cd violence-detection
   ```

2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Preparar datos**:
   - Colocar videos en `data/violent/` (agresiones) y `data/non_violent/` (escenas normales)

---

## **🚀 Uso**  

### **1. Entrenar el modelo**  
```bash
python train.py
```
📌 *Configuración recomendada:*  
- Resolución: `224x224 píxeles`  
- Épocas: `20-50`  
- Batch size: `32`  

### **2. Ejecutar detección en tiempo real**  
```bash
python realtime_detection.py
```
🖥️ *Atajos:*  
- Presiona `Q` para salir  
- Cambia cámara con `camera_index`  

### **3. Interfaz web**  
```bash
python app.py
```
🌐 Abre en tu navegador: [http://localhost:5000](http://localhost:5000)  

---

## **📊 Rendimiento**  

| Métrica               | Valor       |
|-----------------------|-------------|
| **Precisión**         | 98.9%       |
| **Tiempo por frame**  | 15ms (GPU)  |
| **Umbral óptimo**     | 0.7         |
| **FPS**               | 30+         |

---

## **🤝 Cómo Contribuir**  

1. **Haz fork** del proyecto  
2. **Crea una rama**:  
   ```bash
   git checkout -b feature/nueva-funcion
   ```  
3. **Envía un Pull Request**  

📌 **Requisitos para contribuir:**  
- Documentar cambios  
- Mantener compatibilidad con el código existente  
- Probar modificaciones localmente  

---

## **📜 Licencia**  
MIT License - Ver [LICENSE](LICENSE) para detalles.  

---

## **⚠️ Nota Importante**  
Este proyecto es **para fines de investigación**. El autor no se hace responsable del uso indebido. Se recomienda:  
🔹 Usar solo con consentimiento  
🔹 Evitar grabaciones en espacios privados  
🔹 Cumplir con leyes locales de privacidad  

---

<p align="center">
  ✨ **¿Preguntas?** Abre un <a href="https://github.com/tuusuario/violence-detection/issues">issue</a> en GitHub  
</p>
