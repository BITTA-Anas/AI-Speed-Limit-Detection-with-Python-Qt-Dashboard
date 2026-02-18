<<<<<<< HEAD
# 🚗 AI Speed Limit Detection with Python Qt Dashboard

A real-time speed limit sign detection and visualization system using computer vision, OCR, and a modern Qt/QML graphical interface.

**[English](#english) | [Français](#français)**

---

## English

### Overview

**AI Speed Limit Detection** is a comprehensive real-time traffic sign detection application that combines advanced computer vision with an elegant graphical interface. The system detects speed limit signs from video input, extracts numerical values using OCR, and displays them dynamically on a customizable gauge interface.

### Key Features

- **🎯 Real-time Detection**: Uses YOLOv8 for accurate speed limit sign detection
- **🔤 OCR Integration**: Tesseract OCR for robust digit extraction from signs
- **⚡ GPU Acceleration**: Optional CUDA support for enhanced performance
- **🎨 Dynamic UI**: Qt6/QML interface with real-time gauge updates
- **📊 Data Logging**: Persistent storage of detected speed limits
- **🔄 IPC Communication**: JSON-based inter-process communication between Python and C++
- **🛣️ Traffic Compliant**: Recognizes French standard speed limits (20, 30, 40, 50, 60, 80, 100, 120 km/h)

### Architecture

```
┌─────────────────────────────────────────────────────────┐
│  Video Input (Webcam)                                   │
└────────────────┬────────────────────────────────────────┘
                 │
┌────────────────▼────────────────────────────────────────┐
│  Python Processing Layer (Main.py / test.py)            │
│  ├─ YOLOv8 Detection                                    │
│  ├─ OpenCV Image Processing                             │
│  ├─ Tesseract OCR                                       │
│  └─ JSON Export                                         │
└────────────────┬────────────────────────────────────────┘
                 │
┌────────────────▼────────────────────────────────────────┐
│  vitesse_limite.json                                    │
└────────────────┬────────────────────────────────────────┘
                 │
┌────────────────▼────────────────────────────────────────┐
│  C++ Qt Application Layer                               │
│  ├─ SpeedLimitReader (Data Monitor)                     │
│  ├─ Qt6/QML Engine                                      │
│  └─ Dynamic Gauge Interface                             │
└─────────────────────────────────────────────────────────┘
```

### Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Detection** | YOLOv8 | Real-time object detection |
| **Image Processing** | OpenCV | Video capture & preprocessing |
| **OCR** | Tesseract | Digit recognition |
| **UI Framework** | Qt6 | Cross-platform GUI |
| **UI Rendering** | QML | Modern declarative UI |
| **Build System** | CMake | Cross-platform compilation |
| **IPC** | JSON | Inter-process communication |


#### Software Dependencies

**Python Environment:**
- Python 3.8+

**System Software:**
- Tesseract OCR 5.0+
- Qt6 Runtime (5.0+)
- Webcam or video input device

### Installation

#### Step 1: Clone Repository
```bash
git clone https://github.com/BITTA-Anas/AI-Speed-Limit-Detection-with-Python-Qt-Dashboard.git
cd AI-Speed-Limit-Detection-with-Python-Qt-Dashboard
```

#### Step 2: Python Dependencies Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

**requirements.txt:**
```
opencv-python==4.8.1.78
pandas==2.0.3
ultralytics==8.0.200
pytesseract==0.3.10
numpy==1.24.3
torch==2.0.1
torchvision==0.15.2
```

#### Step 3: Install Tesseract OCR

**Windows:**
1. Download installer: https://sourceforge.net/projects/tesseract-ocr.mirror/
2. Run installer (default path: `C:\Program Files\Tesseract-OCR`)
3. Add to PATH environment variable

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install tesseract-ocr
```

**macOS:**
```bash
brew install tesseract
```

#### Step 4: Install Qt6 Development Tools

**Windows/Linux/macOS:**
```bash
# Using Qt installer
# Download from https://www.qt.io/download

# Or on Linux (Ubuntu):
sudo apt-get install qt6-base-dev qt6-qml-dev
```

#### Step 5: Build C++ Application

```bash
mkdir build
cd build
cmake ..
cmake --build . --config Release
```

#### Step 6: Configure Paths

Edit `Main.py` and `test.py` to match your Tesseract installation:
```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

### Usage

#### Running the Detection System (Python)

**Basic Mode:**
```bash
python Main.py
```

**Advanced Mode (with threading and GPU support):**
```bash
python test.py
```

**Controls:**
- ESC: Exit application
- Mouse Movement: Display coordinates (optional debug feature)

#### Running the GUI Application (C++)

```bash
# From build directory
./JaugeDynamique
# Or on Windows
JaugeDynamique.exe
```

**GUI Controls:**
- ⬆️ Arrow Up: Accelerate
- ⬇️ Arrow Down: Brake
- L Key: Toggle Speed Limiter

#### Complete Workflow

```bash
# Terminal 1: Start Python detection
python Main.py

# Terminal 2: Start Qt GUI
./build/JaugeDynamique
```

The system automatically communicates through `vitesse_limite.json` file.

### Configuration

#### Speed Limit Thresholds

Modify valid speeds in `Main.py` (line ~75):
```python
vitesses_valides = {20, 30, 40, 50, 60, 80, 100, 120}
```

#### Detection Sensitivity

Adjust YOLO model in `Main.py` (line ~14):
```python
model = YOLO('Model.pt')  # Change confidence threshold
results = model.predict(frame, conf=0.5)  # Default: 0.5
```

#### Frame Skip Rate

Modify processing frequency in `Main.py` (line ~42):
```python
if count % 3 != 0:  # Process every 3rd frame
    continue
```

#### Monitor Refresh Rate

Adjust in `speedlimitreader.cpp` (line ~10):
```cpp
m_timer.setInterval(500);  // Monitor file every 500ms
```

### Project Structure

```
AI-Speed-Limit-Detection-with-Python-Qt-Dashboard/
├── Main.py                      # Primary detection script
├── test.py                      # Advanced detection with threading
├── Main.cpp                     # Qt application entry point
├── speedlimitreader.h           # Speed limit reader class header
├── speedlimitreader.cpp         # Speed limit reader implementation
├── CMakeLists.txt               # CMake build configuration
├── qml/
│   └── Main.qml                 # Qt QML interface
├── assets/
│   └── signs/                   # SVG speed limit sign graphics
│       ├── 20.svg
│       ├── 30.svg
│       ├── 40.svg
│       ├── 50.svg
│       ├── 60.svg
│       ├── 80.svg
│       ├── 100.svg
│       └── 120.svg
├── build/                       # CMake build output (generated)
├── resources.qrc                # Qt resource configuration
├── SpeedClass.txt               # YOLO class definitions
├── vitesse_limite.json          # Current speed limit (IPC)
├── speed_limit_data.txt         # Historical detection log
├── Model.pt                     # YOLOv8 trained model
├── data.yaml                    # Dataset configuration
├── README.md                    # Main documentation
├── LICENSE                      # MIT License
├── COPYRIGHT                    # Copyright & IP rights
├── AUTHORS                      # Project creators & contributors
├── CODE_OF_CONDUCT.md           # Community guidelines
├── CONTRIBUTING.md              # Contribution guidelines
├── SECURITY.md                  # Security policy
├── CHANGELOG.md                 # Version history
├── .gitignore                   # Git ignore rules
└── requirements.txt             # Python dependencies
```

### File Descriptions

| File | Purpose |
|------|---------|
| `Main.py` | Primary Python script for speed limit detection using YOLO and Tesseract |
| `test.py` | Advanced version with threading, queue management, and GPU optimization |
| `Main.cpp` | Qt application initialization and QML engine setup |
| `speedlimitreader.h` | C++ class definition for monitoring speed limit changes |
| `speedlimitreader.cpp` | Implementation of JSON file monitoring and signal emission |
| `Main.qml` | Qt Quick interface with gauge visualization and controls |
| `Model.pt` | Pre-trained YOLOv8 model for sign detection |
| `vitesse_limite.json` | Inter-process communication file (JSON format) |
| `SpeedClass.txt` | YOLO class labels for object detection |

### Data Flow

```
1. Video Capture
   ↓
2. Frame Resizing (1020x500)
   ↓
3. YOLO Detection
   ↓
4. Sign Cropping & Preprocessing
   ↓
5. Tesseract OCR
   ↓
6. Validation (against known speeds)
   ↓
7. JSON Export
   ↓
8. C++ Monitoring & UI Update
   ↓
9. Gauge Rendering
```

### Advanced Features


#### Threading Implementation

`test.py` implements thread-safe queue processing:
```python
def traiter_frames(queue):
    while True:
        frame = queue.get()
        # Process frame
        queue.task_done()
```

#### Image Enhancement

Preprocessing pipeline for improved OCR accuracy:
```python
gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 10, 20, 20)  # Noise reduction
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
```

### Troubleshooting

#### Issue: "Tesseract not found"
**Solution**: Ensure Tesseract is installed and path is correct in Python script

#### Issue: YOLO model loading fails
**Solution**: Download `Model.pt` and place in project root directory

#### Issue: GUI doesn't update
**Solution**: Check if `vitesse_limite.json` exists and has correct permissions

#### Issue: Poor OCR accuracy
**Solution**: Increase bilateral filter kernel size or adjust frame resize dimensions


### API Reference

#### SpeedLimitReader (C++)

```cpp
class SpeedLimitReader : public QObject
{
    Q_OBJECT
    Q_PROPERTY(int speedLimit READ speedLimit NOTIFY speedLimitChanged)
    
public:
    explicit SpeedLimitReader(QObject *parent = nullptr);
    int speedLimit() const;
    QString speedLimitImage() const;
    
signals:
    void speedLimitChanged();
    
private slots:
    void readSpeedLimitFile();
};
```

#### JSON Format (vitesse_limite.json)

```json
{
    "vitesse_limite": 80,
    "timestamp": "2026-02-16 14:30:45"
}
```

### Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

### Known Limitations

- Single camera input only
- Supports French speed limit signs (customizable)
- OCR accuracy depends on sign quality and lighting
- Real-time performance varies by hardware
- Qt6 dependency (cross-platform but requires separate installation)

### Future Enhancements

- [ ] Multi-camera support
- [ ] Real-time speed limit enforcement
- [ ] Mobile app integration
- [ ] Advanced filtering (Kalman filter)
- [ ] Network communication capability
- [ ] Custom model training pipeline
- [ ] Docker containerization
- [ ] REST API interface

### License

This project is licensed under the MIT License - see LICENSE file for details.

### Author & Contact

**Project Developer**: [BITTA Anas](https://www.linkedin.com/in/bitta-anas/)

**GitHub**: [@BITTA-Anas](https://github.com/BITTA-Anas)

**LinkedIn**: [BITTA Anas](https://www.linkedin.com/in/bitta-anas/)

### Acknowledgments

- YOLOv8 by Ultralytics
- Tesseract OCR by Google
- Qt Framework by Qt Company
- OpenCV Community

### Support & Contact

For issues, questions, or suggestions:
- Open an Issue on [GitHub](https://github.com/BITTA-Anas/AI-Speed-Limit-Detection-with-Python-Qt-Dashboard/issues)
- Email: anas.bitta@usmba.ac.ma
- LinkedIn: https://www.linkedin.com/in/bitta-anas/
- Repository: https://github.com/BITTA-Anas/AI-Speed-Limit-Detection-with-Python-Qt-Dashboard

### Citation

If you use this project in academic research, please cite:

```bibtex
@software{ai_speed_limit_detection_2026,
  title = {AI Speed Limit Detection with Python Qt Dashboard: Real-time Traffic Sign Detection System},
  author = {BITTA-Anas},
  year = {2026},
  url = {https://github.com/BITTA-Anas/AI-Speed-Limit-Detection-with-Python-Qt-Dashboard}
}
```

---

## Français

### Aperçu

**AI Speed Limit Detection with Python Qt Dashboard** est une application complète de détection de panneaux de limitation de vitesse en temps réel combinant la vision par ordinateur avancée à une interface graphique élégante. Le système détecte les panneaux de limitation de vitesse à partir d'une entrée vidéo, extrait les valeurs numériques en utilisant l'OCR et les affiche dynamiquement sur une jauge personnalisable.

### Caractéristiques principales

- **🎯 Détection en temps réel** : Utilise YOLOv8 pour une détection précise des panneaux
- **🔤 Intégration OCR** : Tesseract OCR pour l'extraction robuste de chiffres
- **⚡ Accélération GPU** : Support optionnel de CUDA pour améliorer les performances
- **🎨 Interface dynamique** : Interface Qt6/QML avec mise à jour en temps réel
- **📊 Journalisation des données** : Stockage persistant des limites détectées
- **🔄 Communication IPC** : Communication inter-processus basée sur JSON
- **🛣️ Conformité aux normes** : Reconnaît les limites de vitesse françaises standard

### Structure du projet

```
AI-Speed-Limit-Detection-with-Python-Qt-Dashboard/
├── Main.py                      # Script de détection principal
├── test.py                      # Détection avancée avec threading
├── Main.cpp                     # Point d'entrée de l'application Qt
├── speedlimitreader.h           # En-tête de la classe lecteur
├── speedlimitreader.cpp         # Implémentation du lecteur
├── CMakeLists.txt               # Configuration CMake
├── qml/
│   └── Main.qml                 # Interface Qt QML
├── assets/
│   └── signs/                   # Graphiques de panneaux en SVG
├── build/                       # Sortie CMake (généré)
├── resources.qrc                # Configuration des ressources Qt
├── SpeedClass.txt               # Définitions des classes YOLO
├── vitesse_limite.json          # Limite de vitesse actuelle (IPC)
├── speed_limit_data.txt         # Journal des détections
├── Model.pt                     # Modèle YOLOv8 entraîné
└── README.md                    # Ce fichier
```

### Installation (Français)

#### Étape 1 : Cloner le référentiel
```bash
git clone https://github.com/BITTA-Anas/AI-Speed-Limit-Detection-with-Python-Qt-Dashboard.git
cd AI-Speed-Limit-Detection-with-Python-Qt-Dashboard
```

#### Étape 2 : Installation des dépendances Python
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### Étape 3 : Installer Tesseract OCR
- Télécharger depuis : https://sourceforge.net/projects/tesseract-ocr.mirror/
- Installer en chemin par défaut
- Ajouter au PATH

#### Étape 4 : Compiler l'application C++
```bash
mkdir build
cd build
cmake ..
cmake --build . --config Release
```

### Utilisation (Français)

```bash
# Terminal 1: Démarrer la détection Python
python Main.py

# Terminal 2: Lancer l'interface Qt
./build/JaugeDynamique
```

### Dépannage (Français)

| Problème | Solution |
|----------|----------|
| Tesseract non trouvé | Vérifier l'installation et le chemin |
| Modèle YOLO ne charge pas | Télécharger Model.pt |
| Interface ne se met pas à jour | Vérifier vitesse_limite.json |
| OCR imprécis | Augmenter la qualité de l'image |
| GPU non utilisé | Installer CUDA et vérifier torch.cuda |

---

**Last Updated**: February 2026
**Version**: 1.0.0
=======
# 🚦 AI Speed Limit Detection with Python & Qt Dashboard  

## 📌 Description  
This project combines **Computer Vision**, **Artificial Intelligence**, and **Qt/QML** to build an application capable of:  

- 🛑 Automatically detecting speed limit signs using a **YOLOv8 trained model**.  
- 🔎 Extracting the numeric speed value using **OCR (Tesseract)**.  
- 💾 Storing the detected value in **JSON** (`vitesse_limite.json`).  
- 📊 Displaying the detected speed on a **real-time dynamic gauge** built with **Qt/QML**.  

It demonstrates how to integrate **Python (AI & computer vision)** with **C++/Qt (UI)**.  

---

## 🛠️ Technologies  
- **Python** → YOLOv8, OpenCV, PyTesseract, NumPy  
- **C++/Qt (QML)** → dynamic gauge and UI  
- **JSON** → real-time data exchange  
- **CMake** → compilation and build system  

---

## 📂 Structure du projet

- 📁 **AI-Speed-Limit-Detection-with-Python-Qt-Dashboard/**
  - ⚙️ `.vscode/` → Configuration VS Code  
  - 🖼️ `assets/signs/` → Images de panneaux de vitesse  
  - 🏗️ `build/` → Résultats de compilation (CMake)  
  - 🎨 `qml/` → Interface QML (jauge dynamique)  
  - 📄 `CMakeLists.txt` → Configuration CMake  
  - 💻 `Main.cpp` → Point d'entrée C++ (Qt app)  
  - 🐍 `Main.py` → Script Python (YOLO + OCR)  
  - 🤖 `Model.pt` → Modèle YOLOv8 entraîné  
  - 📑 `SpeedClass.txt` → Classes de vitesses (30, 50, 80, etc.)  
  - 🗂️ `data.yaml` → Configuration dataset YOLO  
  - 📦 `resources.qrc` → Ressources Qt  
  - 📊 `speed_limit_data.txt` → Données de vitesse (texte)  
  - 🔍 `speedlimitreader.cpp` → Lecteur JSON en C++  
  - 📘 `speedlimitreader.h` → Header du lecteur JSON  
  - 📌 `vitesse_limite.json` → Vitesse détectée en temps réel  

---

## ▶️ Usage  

### 1️⃣ Run the Python detection + OCR script  
`bash`
python Main.py
### 2️⃣ Run the Qt app to display the dynamic gauge  
`bash`
./build/JaugeDynamique.exe

---

## 📊 Exemple de workflow

1. YOLOv8 détecte un panneau **80 km/h**.  
2. L’OCR extrait la valeur **80**.  
3. La valeur est écrite dans `vitesse_limite.json`.  
4. La jauge Qt se met à jour en temps réel et affiche **80 km/h**.  

---

## 📌 Améliorations futures

- 🚗 Détection multiple de panneaux.  
- 📉 Comparaison entre les vitesses limites détectées et la vitesse réelle du véhicule.  
- 📱 Déploiement sur cartes embarquées (**Raspberry Pi / Jetson Nano**).  

---

## 👨‍💻 Auteur
Développé par **BITTA Anas**  
🎓 Étudiant en Systèmes Embarqués – Université Privée de Fès  



>>>>>>> 69b43612840d0e379e0c4349b1252d29fed43746
