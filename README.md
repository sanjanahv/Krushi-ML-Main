# 🌿 AI-Powered Plant Disease Prediction & Reasoning System

## **Project Overview**
This project aims to build a full-stack automated system to help farmers and agriculturalists identify plant diseases from leaf images. Unlike standard classifiers that only give a label (e.g., "Potato Blight"), this system allows for **AI-Reasoning**, providing the "Why" (Symptoms) and the "How to Fix" (Cure/Treatment).

### **Core Objectives**
1.  **High Accuracy**: Train a Deep Learning model (MobileNetV2/ResNet) on the `PlantVillage` dataset.
2.  **Explainability**: Provide detailed reasoning for *why* a disease was detected (e.g., specific leaf patterns).
3.  **Actionability**: Offer immediate cure recommendations or preventive measures.
4.  **Accessibility**: A modern, easy-to-use Web Interface for users to upload images and view results.

---

## **Project Structure**
The project is divided into 5 modular roles to ensure parallel development.

```text
/Project_Root
│
├── /dataset_eda          # [Role 1] Data Cleaning, Preprocessing & EDA
│   ├── clean_data.py     # Script to fix folder structure
│   ├── eda_report.ipynb  # Analysis of class balance
│   └── dataset/          # Final Split: train/, val/, test/
│
├── /ml_model             # [Role 2] Model Training & Intelligence
│   ├── train.ipynb       # Training Notebook (Transfer Learning)
│   ├── model.h5          # The trained model artifact
│   └── reasoning.json    # The 'Reasoning Dictionary' (Class -> Explanation)
│
├── /backend              # [Role 3] API Server
│   ├── main.py           # FastAPI Application
│   └── requirements.txt  # Python Dependencies
│
├── /frontend             # [Role 4] Web Client
│   ├── pages/            # Next.js Pages
│   ├── components/       # UI Components
│   └── public/           # Assets
│
└── /testing              # [Role 5] QA & Validation
    ├── test_api.py       # API Endpoint Tests
    └── test_model.py     # Accuracy & Confusion Matrix Reports
```

---

## **Workflow Diagram**
1.  **User** uploads an image on the **Frontend**.
2.  **Frontend** sends image to **Backend API**.
3.  **Backend** preprocesses image and feeds it to **ML Model**.
4.  **ML Model** returns a Class ID (e.g., `0`).
5.  **Backend** looks up Class ID in `reasoning.json` to find Name, Symptoms, and Cure.
6.  **Backend** responds with full details.
7.  **Frontend** displays the result card to the **User**.

---

## **Global Requirements**

### **System Prerequisites**
*   **OS**: Windows, Linux, or macOS.
*   **Python**: Version 3.8+
*   **Node.js**: Version 14+ (for Frontend).
*   **Hardware**: A GPU is recommended for training (Role 2), but CPU inference is fine for the Backend.

### **Key Libraries**
*   **Python**: `fastapi`, `tensorflow` or `torch`, `pandas`, `numpy`, `opencv-python`.
*   **JavaScript**: `next`, `react`, `tailwindcss`, `axios`.

---

## **Getting Started**
1.  **Clone/Download** this repository.
2.  **Navigate** to your specific role folder (check the dedicated READMEs):
    *   `DATA_EDA_README.md`
    *   `ML_MODEL_README.md`
    *   `BACKEND_README.md`
    *   `FRONTEND_README.md`
    *   `TESTING_README.md`
3.  **Install Dependencies** for your module.
4.  **Sync**: Weekly syncs to ensure Input/Output formats (Image Size `224x224`, JSON keys) match between teams.
