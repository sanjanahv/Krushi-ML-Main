# Role 1: Data Cleaning & Exploratory Data Analysis (EDA)

## **Role Overview**
**Title**: Data Engineer / Analyst  
**Objective**: Prepare the raw `PlantVillage` dataset to ensure the Machine Learning model receives clean, balanced, and high-quality input data. Your work is the foundation of the entire project.

---

## **Tech Stack & Tools**
*   **Language**: Python 3.8+
*   **Libraries**:
    *   `pandas`, `numpy` (Data Manipulation)
    *   `matplotlib`, `seaborn` (Visualization)
    *   `opencv-python` (cv2), `pillow` (Image Processing)
    *   `scikit-learn` (Splitting data)
*   **Environment**: Jupyter Notebook or Python Scripts

---

## **Step-by-Step Instructions**

### **1. Directory Structure Fix**
Currently, the dataset might have nested folders (e.g., `PlantVillage/PlantVillage/Tomato_Healthy`).
*   **Task**: Write a script to consolidate folders so the structure looks like this:
    ```
    dataset/
      ├── raw/
      │    ├── Tomato_Early_blight/
      │    ├── Tomato_Healthy/
      │    ├── Potato_Early_blight/
      │    └── ...
    ```

### **2. Data Cleaning & Inspection**
*   **Check for Corruption**: Write a script to iterate through every image. Try opening it with `cv2.imread()`. If it fails or if the file size is 0, delete it.
*   **Class Distribution**: Count the number of images in each class.
    *   *Deliverable*: A bar chart showing image counts.
    *   *Action*: If a class has < 500 images while others have 2000, flag it. We will need augmentation.

### **3. Preprocessing**
*   **Resizing**: The ML team needs fixed input sizes. Resize all images to **224x224** pixels.
*   **Normalization**: Scale pixel values from `0-255` to `0.0-1.0` (or leave this for the model's preprocessing layer, but clarify this decision).
*   **Format**: Ensure all images are converted to JPG or PNG to avoid compatibility issues.

### **4. Data Augmentation (For Imbalanced Classes)**
If any class is small, generate new samples to balance the dataset.
*   **Techniques**:
    *   Random Rotation (±20 degrees)
    *   Horizontal Flip
    *   Zoom (±10%)
    *   Brightness adjustment
*   **Tool**: Use `Albumentations` or `Keras ImageDataGenerator`.

### **5. Data Splitting**
Split the cleaned data into three sets to ensure honest model evaluation.
*   **Train Set**: 70% (Used to teach the model)
*   **Validation Set**: 15% (Used to tune hyperparameters during training)
*   **Test Set**: 15% (Held out completely for final evaluation)
*   **Output**: Save these into separate folders: `dataset/train`, `dataset/val`, `dataset/test`.

---

## **Deliverables**
1.  **`clean_data.py`**: Script to clean and restructure folders.
2.  **`eda_report.ipynb`**: Notebook with bar charts of class distributions and sample images.
3.  **Final Dataset Folder**: `dataset/` containing `train/`, `val/`, and `test/` subdirectories.
