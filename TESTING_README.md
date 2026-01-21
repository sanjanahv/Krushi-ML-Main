# Role 5: Quality Assurance (QA) & Testing

## **Role Overview**
**Title**: QA Engineer  
**Objective**: Break things before the user does. Your job is to verify that the ML model is accurate, the Backend is stable, and the Frontend is usable.

---

## **Tech Stack & Tools**
*   **Backend Testing**: `pytest`, `requests`
*   **API Testing**: Postman or Thunder Client
*   **Frontend Testing**: Cypress or Jest
*   **Stress Testing**: Locust (optional)

---

## **Step-by-Step Instructions**

### **1. Model Evaluation (The "exam")**
*   Take the `test_set` (images the model has NEVER seen).
*   Run the model on these images.
*   **Deliverable**:
    *   **Accuracy Score**: (e.g., 92%).
    *   **False Positives**: Did it call a healthy leaf "diseased"? (This is bad, farmers might waste money on medicine).
    *   **False Negatives**: Did it call a diseased leaf "healthy"? (This is worse, the crop might die).

### **2. API Testing**
*   **Functional Test**:
    *   Send a valid JPG image -> Expect `200 OK` and JSON response.
    *   Send a text file -> Expect `400 Bad Request`.
*   **Performance**:
    *   Send a 5MB high-res image. Does the server crash? Does it timeout?

### **3. Frontend / User Experience (UX)**
*   **Responsiveness**: Open `localhost:3000` on your phone (or Chrome DevTools Mobile View). Can you still click the "Upload" button?
*   **Flow**:
    *   Upload Image -> Wait -> See Result.
    *   Does the "Cure" section text cut off?
    *   Is the font readable?

### **4. Integration Testing**
*   Verify the full loop:
    1.  Frontend sends Image -> Backend receives -> Model predicts -> Backend responds -> Frontend displays.
    2.  Check if the "Reasoning" text on the UI matches what is in the Backend's JSON file.

---

## **Deliverables**
1.  **`test_suite/`**: Folder containing `test_api.py` and `test_ui.spec.js`.
2.  **Bug Report**: A simple document listing any issues found (e.g., "Upload button broken on iPhone").
3.  **Final Quality Sign-off**: A "Green Light" that the project is ready to show.
