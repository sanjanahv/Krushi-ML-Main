# Role 3: Backend Development

## **Role Overview**
**Title**: Backend Developer  
**Objective**: Create a robust API that serves the ML model to the world. You are the bridge between the heavy "Brain" (ML Model) and the "Face" (Frontend).

---

## **Tech Stack & Tools**
*   **Language**: Python 3.9+
*   **Framework**: **FastAPI** (Recommended for speed) or Flask.
*   **Server**: `Uvicorn`
*   **Libraries**: `tensorflow-cpu` (to load model), `pillow` (image processing).

---

## **Step-by-Step Instructions**

### **1. Environment Setup**
*   Initialize a virtual environment.
*   Install dependencies: `fastapi`, `uvicorn`, `python-multipart`, `tensorflow`, `numpy`, `pillow`.

### **2. API Structure**
Create a `main.py` file.
*   **Load Model**: Load `model.h5` and `reasoning_dict.json` **globally** at startup (so you don't reload it for every request).

### **3. The `/predict` Endpoint**
Create a POST route that accepts an image file.
*   **Input**: `file: UploadFile`
*   **Processing**:
    1.  Read the file bytes.
    2.  Open with Pillow (`Image.open(io.BytesIO(data))`).
    3.  Resize to `224x224` (Must match ML team's size exactly!).
    4.  Convert to NumPy array and normalize (scale 1./255).
    5.  Expand dimensions to match batch size `(1, 224, 224, 3)`.
*   **Inference**:
    1.  Run `prediction = model.predict(img)`.
    2.  Get the max confidence score and the class index (`np.argmax`).
*   **Response Construction**:
    1.  Get the class name using `class_indices.json`.
    2.  Fetch the "Reasoning", "Cause", and "Cure" from `reasoning_dict.json`.
    3.  Return JSON:
        ```json
        {
          "class": "Tomato_Early_blight",
          "confidence": 0.95,
          "reasoning": "Identified by dark spots...",
          "cure": "Use fungicides..."
        }
        ```

### **4. Feedback & Logging**
*   Create a `/feedback` endpoint where users can click "Correct" or "Incorrect" on the frontend.
*   Log these interactions to a simple CSV or SQLite DB to help the Analytics team later.

### **5. Security & CORS**
*   Enable **CORS** (`CORSMiddleware`) to allow requests from `localhost:3000` (Frontend).
*   Validate file types (ensure user uploads image, not .exe).

---

## **Deliverables**
1.  **`main.py`**: The FastAPI application.
2.  **`requirements.txt`**: List of all python dependencies.
3.  **Running API**: Accessible at `http://localhost:8000/docs`.
