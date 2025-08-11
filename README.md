<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Violence Detection System | YOLO Real-Time Aggression Detection</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        h1 {
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }
        h2 {
            margin-top: 30px;
            border-left: 4px solid #3498db;
            padding-left: 10px;
        }
        code {
            background-color: #f8f9fa;
            padding: 2px 5px;
            border-radius: 3px;
            font-family: 'Courier New', Courier, monospace;
        }
        pre {
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }
        .highlight {
            background-color: #fffde7;
            padding: 15px;
            border-left: 4px solid #ffd600;
            margin: 20px 0;
        }
        .screenshot {
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 5px;
            max-width: 100%;
        }
        .badge {
            display: inline-block;
            padding: 3px 7px;
            border-radius: 3px;
            font-size: 14px;
            font-weight: bold;
            margin-right: 5px;
        }
        .badge-python {
            background-color: #3776ab;
            color: white;
        }
        .badge-ai {
            background-color: #ff6d00;
            color: white;
        }
        .badge-yolo {
            background-color: #00c853;
            color: white;
        }
    </style>
</head>
<body>
    <h1>Violence Detection System</h1>
    
    <p>
        <span class="badge badge-python">Python</span>
        <span class="badge badge-ai">Computer Vision</span>
        <span class="badge badge-yolo">YOLO</span>
    </p>
    
    <p>Sistema de detección de agresión en tiempo real usando redes neuronales convolucionales inspiradas en YOLO. Procesa flujo de video desde cámaras IP o webcams para identificar comportamientos violentos.</p>
    
    <div class="highlight">
        <strong>✨ Características principales:</strong>
        <ul>
            <li>Detección en tiempo real (30+ FPS)</li>
            <li>Modelo pre-entrenado incluido (.h5)</li>
            <li>Interfaz web con Flask</li>
            <li>Entrenamiento personalizado con tus propios datasets</li>
            <li>Umbral configurable de sensibilidad</li>
        </ul>
    </div>

    <h2>📦 Requisitos</h2>
    <ul>
        <li>Python 3.8+</li>
        <li>OpenCV 4.5+</li>
        <li>TensorFlow 2.6+</li>
        <li>Flask 2.0+ (para la interfaz web)</li>
    </ul>

    <h2>🚀 Instalación</h2>
    <pre><code># Clonar repositorio
git clone https://github.com/tuusuario/violence-detection.git
cd violence-detection

# Instalar dependencias
pip install -r requirements.txt</code></pre>

    <h2>🎯 Uso</h2>
    
    <h3>1. Entrenamiento del modelo</h3>
    <pre><code>python train.py</code></pre>
    <p><em>Nota: Coloca tus videos de entrenamiento en <code>data/violent/</code> y <code>data/non_violent/</code></em></p>
    
    <h3>2. Detección por cámara</h3>
    <pre><code>python realtime_detection.py</code></pre>
    <p><img src="https://example.com/screenshot-terminal.jpg" alt="Terminal Detection" class="screenshot"></p>
    
    <h3>3. Interfaz web</h3>
    <pre><code>python app.py</code></pre>
    <p>Accede en tu navegador a: <code>http://localhost:5000</code></p>
    <p><img src="https://example.com/screenshot-web.jpg" alt="Web Interface" class="screenshot"></p>

    <h2>🛠 Estructura del Proyecto</h2>
    <pre><code>violence-detection/
├── data/               # Videos de entrenamiento
├── models/             # Modelos pre-entrenados
├── templates/          # Interfaz web
├── utils/              # Utilidades de procesamiento
├── app.py              # Servidor Flask
├── realtime_detection.py # Detección en tiempo real
└── train.py            # Script de entrenamiento</code></pre>

    <h2>📊 Rendimiento</h2>
    <p>Métricas promedio en dataset de validación:</p>
    <ul>
        <li><strong>Precisión:</strong> 98.9%</li>
        <li><strong>Tiempo de inferencia:</strong> 15ms por frame (RTX 3060)</li>
        <li><strong>Umbral recomendado:</strong> 0.7</li>
    </ul>

    <h2>🤝 Contribución</h2>
    <p>¡Las contribuciones son bienvenidas! Por favor lee el <a href="CONTRIBUTING.md">CONTRIBUTING.md</a> antes de enviar un PR.</p>

    <h2>📜 Licencia</h2>
    <p>Este proyecto está bajo licencia MIT - ver <a href="LICENSE">LICENSE</a> para más detalles.</p>

    <div class="highlight">
        <strong>📌 Nota:</strong> Este proyecto es para fines de investigación. El autor no se hace responsable del uso indebido del mismo.
    </div>
</body>
</html>
