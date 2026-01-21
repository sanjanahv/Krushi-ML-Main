# Role 4: Frontend Development

## **Role Overview**
**Title**: Frontend Developer  
**Objective**: Build a visually stunning, responsive, and easy-to-use web interface. Users (farmers) should be able to upload a photo and get results instantly. The "WOW factor" is important here.

---

## **Tech Stack & Tools**
*   **Framework**: **Next.js** (React)
*   **Styling**: **Tailwind CSS**
*   **Animations**: **Framer Motion**
*   **HTTP Client**: `axios` or `fetch`

---

## **Step-by-Step Instructions**

### **1. Project Initialization**
*   Create a new Next.js app: `npx create-next-app@latest ./frontend`.
*   Install Tailwind CSS and Framer Motion (`npm install framer-motion`).

### **2. Design & Layout**
*   **Color Palette**: Use nature-inspired colors (Forest Green, Earthy Brown) mixed with modern UI trends (Glassmorphism, clean whites/grays).
*   **Components**:
    *   **Hero Section**: Big bold text "AI for Healthy Crops". Check background patterns.
    *   **UploadCard**: A centered box supporting Drag & Drop. Show a preview of the image once selected.

### **3. Integrating with Backend**
*   On image selection/drop:
    1.  Show a "Scanning..." or "Analyzing..." loading state (use a spinner or scanning animation).
    2.  Send `POST` request to `http://localhost:8000/predict` with the image `FormData`.
    3.  Receive JSON response (`class`, `confidence`, `reasoning`, `cure`).

### **4. Displaying Results**
*   **The Verdict**: Display the Disease Name prominently.
    *   *Color Coding*: Green for "Healthy", Red/Orange for "Disease".
*   **The Details**:
    *   Create an "Accordion" or "Cards" layout to show:
        *   **Reasoning**: "Why did AI think this?"
        *   **Cure**: "What should I do?"
*   **(Bonus)**: Add a "Print Report" button.

### **5. Polish**
*   **Responsive**: Ensure it works perfectly on mobile phones (since farmers might use phones in the field).
*   **Error Handling**: If the API fails, show a friendly "Server is sleeping" message, not a code stack trace.

---

## **Deliverables**
1.  **Next.js Source Code**: Fully functional frontend folder.
2.  **Live Demo**: Ability to run `npm run dev` and use the app end-to-end.
