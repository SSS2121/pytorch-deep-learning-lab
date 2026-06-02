# PyTorch Deep Learning Lab 🧠

[EN] This repository is a technical log of my learning journey in Deep Learning with PyTorch. It documents the evolution from fundamental tensor manipulation to the implementation of Convolutional Neural Networks (CNN), Natural Language Processing, and Graph Analytics.

[ES] Este repositorio es una bitácora técnica de mi aprendizaje en Deep Learning con PyTorch. Documenta la evolución desde la manipulación fundamental de tensores hasta la implementación de Redes Neuronales Convolucionales (CNN), Procesamiento de Lenguaje Natural y Análisis de Grafos.

---

## Content / Contenido

### 1. Tensor Fundamentals / Fundamentos de Tensores (`tensor_basics_guide.py`)
- **[EN]** Core data structures, reshaping (squeeze/flatten), and device management (CPU/CUDA).
- **[ES]** Estructuras de datos core, reshaping y gestión de dispositivos.

### 2. Classic Architectures / Arquitecturas Clásicas: LeNet
- **[EN]** MNIST & CIFAR-10 classification using CNNs (Conv2d, Pooling, ReLU).
- **[ES]** Clasificación de MNIST y CIFAR-10 usando CNNs.

### 3. NLP & Neural Chatbots / Chatbots con Redes Neuronales

#### 3a. Intent Classifier Chatbot (`neural_chatbot_intents.py`)
- **[EN]** Educational multi-intent chatbot using MLPs, bag-of-words, and dynamic thresholding.
  - 12 intent categories (greetings, jokes, Python/ML explanations, sentiments)
  - 4-layer architecture with BatchNorm1d and adaptive dropout
  - Curriculum: Demonstrates layer stacking, loss curves, and confidence-based filtering
- **[ES]** Chatbot educativo multi-intención usando MLPs, bolsa de palabras y umbral adaptativo.
  - 12 categorías de intención con respuestas contextuales
  - Arquitectura de 4 capas con normalización por lotes
  - Curva de entrenamiento visualizada con matplotlib

#### 3b. E-commerce Chatbot: "Tienda de Gatos" (`chatbot_tienda_gatos.py`) ⭐ **Production-Ready**
- **[EN]** Specialized chatbot for a real-world cat products e-commerce built on production best practices.
  - **Scope**: 38+ intent categories (product recommendations, shipping, health advice, payment)
  - **NLP**: NLTK stemming for robust preprocessing (handles inflections: "envíos" → "envío")
  - **Architecture**: 3-layer MLP with class-weighted loss to correct generalization bias
  - **Export**: ONNX + JSON metadata for JavaScript deployment (no backend needed)
  - **Evaluation**: Classification report, accuracy metrics, confusion analysis
  - **Curriculum**: 300 epochs, class balancing, convergence visualization
- **[ES]** Chatbot especializado para tienda de gatos de productos en línea basado en mejores prácticas.
  - **Alcance**: 38+ categorías de intención (recomendaciones, envíos, salud, pagos)
  - **NLP Avanzado**: Stemming con NLTK para preprocesamiento robusto
  - **Arquitectura**: MLP optimizada de 3 capas con ponderación de clases
  - **Exportación**: ONNX + metadata JSON para despliegue en JavaScript
  - **Evaluación**: Reporte de clasificación, métricas de precisión, análisis de confusión
  - **Técnicas**: Balanceo de clases, regularización adaptativa, diagnóstico de generalización

**Key Technical Improvements / Mejoras Técnicas Clave:**
```python
# Stemming: "comprar" "compra" "comprando" → stem "compr"
# Weight balancing: Re-weight 'gato_grande_pesado' to prevent confusion with 'pagos'
# ONNX export: Portable across browsers, Node.js, and embedded systems
# Metadata architecture: Decouples tokenizer vocabulary from model inference
```

### 4. Visual Similarity & Graph Analytics / Análisis de Similitud Visual y Grafos (`pytorch_visual_graph_similarity.ipynb`)
- **[EN] Embedding Extraction**: Using pre-trained **ResNet-18** as a feature extractor.
- **[EN] K-NN Graphs**: Constructing visual networks using Euclidean distances.
- **[EN] Edge Pruning**: Optimizing topology via statistical thresholding with **NetworkX**.
- **[ES] Extracción de Embeddings**: Uso de **ResNet-18** pre-entrenada como extractor de características.
- **[ES] Grafos K-NN**: Construcción de redes de similitud visual mediante distancias Euclidianas.
- **[ES] Podado de Aristas**: Optimización de la topología del grafo mediante umbrales estadísticos.

---

## Tech Stack / Tecnologías
- **Deep Learning**: PyTorch, Torchvision.
- **NLP**: NLTK, scikit-learn.
- **Graph Analytics**: NetworkX.
- **Processing & Viz**: NumPy, Scikit-learn, Matplotlib.
- **Export & Deployment**: ONNX, ONNX Runtime (Web).

## Skills Demonstrated / Habilidades Demostradas
- **[EN]** Designing neural architectures and custom training loops.
- **[EN]** Understanding high-dimensional data representations (embeddings).
- **[EN]** NLP preprocessing pipelines (tokenization, stemming, bag-of-words).
- **[EN]** Model evaluation and class imbalance correction.
- **[EN]** Cross-platform model export (ONNX for JavaScript deployment).
- **[ES]** Diseño de arquitecturas neuronales y ciclos de entrenamiento personalizados.
- **[ES]** Comprensión de representaciones de datos en alta dimensión (embeddings).
- **[ES]** Pipelines de preprocesamiento NLP (tokenización, stemming, bolsa de palabras).
- **[ES]** Evaluación de modelos y corrección de desbalance de clases.
- **[ES]** Exportación multiplataforma (ONNX para despliegue en JavaScript).

---

Developed as part of my specialization in Artificial Intelligence. / Desarrollado como parte de mi especialización en Inteligencia Artificial.
