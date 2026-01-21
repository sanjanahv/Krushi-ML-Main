# Role 2: Machine Learning Model & Reasoning

## **Role Overview**
**Title**: AI / ML Engineer  
**Objective**: Build, train, and export a Deep Learning model that can accurately classify plant diseases. Crucially, you must also create the "Intelligence" layer that maps these predictions to human-understandable reasoning and cures.

---

## **Tech Stack & Tools**
*   **Language**: Python 3.8+
*   **Frameworks**: TensorFlow/Keras (Recommended) OR PyTorch
*   **Environment**: Jupyter Notebook / Google Colab (for GPU training)
*   **Model Format**: `.h5` (Keras) or `.pt` (PyTorch)

---

## **Step-by-Step Instructions**

### **1. Model Selection (Transfer Learning)**
Do not build a CNN from scratch. Use a pre-trained model for better accuracy and faster training.
*   **Option A (Speed)**: `MobileNetV2` - Good for web/mobile, lightweight.
*   **Option B (Accuracy)**: `ResNet50` or `EfficientNetB0` - Heavier but often more accurate.
*   **Task**: Load the pre-trained model with `include_top=False` and freeze the base layers. Add your own final Dense layers (GlobalAveragePooling -> Dense(128, ReLU) -> Dropout -> Dense(Num_Classes, Softmax)).

### **2. Training**
*   **Input**: Use the `dataset/train` and `dataset/val` folders prepared by the Data Team.
*   **Hyperparameters**:
    *   Optimizer: `Adam` (lr=0.0001 or 0.001)
    *   Loss Function: `CategoricalCrossentropy`
    *   Metrics: `Accuracy`
    *   Epochs: 20-50 (use Early Stopping with patience=5)
*   **Callbacks**: Save the best model only (`ModelCheckpoint`).

### **3. Evaluation**
*   Run the model on `dataset/test`.
*   Generate a **Confusion Matrix** to see which diseases are confused with others.
*   A target accuracy of **>90%** is expected.

### **4. Constructing the Reasoning System (CRITICAL)**
 The model only outputs a class ID (e.g., `0` or `Tomato__Early_blight`). You must build the translation layer.
*   **Task**: Create a `class_desc.json` file.
*   **Structure**:
    ```json
    {
      "Tomato__Early_blight": {
        "name": "Early Blight",
        "symptoms": "Dark, concentric rings on older leaves.",
        "cause": "Fungus Alternaria solani.",
        "cure": "Apply copper-based fungicides. Prune infected leaves."
      },
      "Tomato__Healthy": {
        "name": "Healthy",
        "symptoms": "None. The plant looks vigorous.",
        "cause": "N/A",
        "cure": "Continue regular watering and monitoring."
      }
    }
    ```
*   *(Advanced Extension)*: Write a script to query a customized LLM prompts if the User requests more "Detailed Analysis".

### **5. Export**
*   Save the final model as `model.h5`.
*   Save the class indices mapping (e.g., `Class 0 = Pepper_bell`, `Class 1 = Potato...`).

---

## **Deliverables**
1.  **`train_model.ipynb`**: The training notebook.
2.  **`model.h5`**: The saved model file ready for deployment.
3.  **`class_indices.json`**: Mapping of model output ID to Class Name.
4.  **`reasoning_dict.json`**: The dictionary of symptoms/cures.
