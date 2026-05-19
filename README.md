# PyTorch Deep Learning Lab 🧠

Este repositorio es una bitácora técnica de mi aprendizaje en **Deep Learning con PyTorch**. Aquí documento la evolución desde la manipulación fundamental de tensores hasta la implementación y entrenamiento de arquitecturas de Redes Neuronales Convolucionales (CNN) y modelos de clasificación de lenguaje.

## Contenido del Repositorio

### 1. Fundamentos de Tensores (`pytorch_3.py`)
Exploración de la estructura de datos core de PyTorch.
- Creación y manipulación de tensores (`zeros`, `ones`, `randn_like`).
- Conversión de tipos (Float, Long, Double) y gestión de dispositivos (CPU vs CUDA).
- Técnicas de *reshaping* (`unsqueeze`, `squeeze`, `flatten`) esenciales para el pre-procesamiento de datos.

### 2. Arquitecturas Clásicas: LeNet (`pytorch_1.py` & `pytorch_4.py`)
Implementación de la arquitectura **LeNet** para tareas de visión artificial:
- **MNIST:** Clasificación de dígitos manuscritos (escala de grises).
- **CIFAR-10:** Clasificación de imágenes a color.
- **Conceptos aplicados:** Capas convolucionales (`nn.Conv2d`), capas de pooling, funciones de activación (`ReLU`, `tanh`) y optimizadores (`Adam`, `SGD`).

### 3. NLP & Chatbot con Redes Neuronales (`pytorch_2.py`)
Desarrollo de un chatbot inteligente basado en intenciones:
- **Pre-procesamiento:** Limpieza de texto, tokenización y vectorización (*Bag-of-Words*).
- **Modelo:** Red neuronal densa (MLP) con capas de BatchNorm y Dropout para mejorar la generalización.
- **Flujo:** Entrenamiento de 80 épocas con gestión de `LabelEncoder` y evaluación con umbrales de confianza (*thresholding*).

## Tecnologías utilizadas
* **Deep Learning:** PyTorch, TorchVision.
* **Procesamiento:** NumPy, Scikit-learn.
* **Visualización:** Matplotlib, NetworkX (para representación de grafos de arquitectura).

## Lo que este repositorio demuestra
* Habilidad para diseñar arquitecturas de red (*forward pass*).
* Comprensión del ciclo de entrenamiento (`optimizer.zero_grad`, `loss.backward`, `step`).
* Capacidad de aplicar modelos tanto a datos tabulares (NLP) como a datos visuales (Imágenes).

---
*Desarrollado como parte de mi ruta de especialización en Inteligencia Artificial.*
