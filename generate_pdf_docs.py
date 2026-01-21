from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, 'Disease Prediction & Reasoning Website', 0, 0, 'C')
        # Line break
        self.ln(20)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    def chapter_title(self, num, label):
        # Arial 12
        self.set_font('Arial', 'B', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, 'Role %d : %s' % (num, label), 0, 1, 'L', 1)
        # Line break
        self.ln(4)

    def chapter_body(self, body):
        # Read text file
        self.set_font('Times', '', 12)
        # Output justified text
        self.multi_cell(0, 5, body)
        # Line break
        self.ln()

pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font('Times', '', 12)

# Intro
pdf.set_font('Arial', 'B', 16)
pdf.cell(0, 10, 'Project Team Framework & Role Assignments', 0, 1, 'C')
pdf.ln(10)
pdf.set_font('Times', '', 12)
intro_text = (
    "Project Goal: Build a full-stack web application where farmers can upload plant leaf images "
    "to identify diseases. crucial feature: provide 'Reasoning', Symptoms, and Cure recommendations, "
    "not just the class prediction.\n\n"
    "Dataset: PlantVillage (Tomato, Potato, Pepper, etc.)\n"
    "Total Roles: 5\n"
)
pdf.multi_cell(0, 5, intro_text)
pdf.ln(10)

# Role 1: Data Cleaning & EDA
pdf.chapter_title(1, 'Data Cleaning, EDA & Preprocessing')
role1_text = (
    "Assignee: Data Engineer / Analyst\n\n"
    "Objective: Prepare the raw PlantVillage dataset to ensure high quality input for the ML model.\n\n"
    "Tech Stack:\n"
    "- Python\n- Pandas, NumPy\n- OpenCV (cv2)\n- Matplotlib / Seaborn\n\n"
    "Key Responsibilities:\n"
    "1. Structure Fix: Consolidate the nested 'PlantVillage' folders into a single 'dataset/train' directory.\n"
    "2. Quality Check: Remove corrupt images and check for class imbalance (e.g., if 'Tomato_Healthy' has 2000 images but 'Potato_Early_Blight' has only 200).\n"
    "3. Preprocessing:\n"
    "   - Resize all images to a fixed standard (e.g., 224x224).\n"
    "   - Normalize pixel values (0-255 -> 0-1).\n"
    "4. Augmentation: Generate synthetic data (rotation, flip, zoom) to balance smaller classes.\n"
    "5. Splitting: Create Train (70%), Validation (15%), and Test (15%) sets.\n\n"
    "Deliverable: A clean, split dataset ready for training."
)
pdf.chapter_body(role1_text)

# Role 2: ML Model
pdf.chapter_title(2, 'Machine Learning Model & Reasoning')
role2_text = (
    "Assignee: AI/ML Engineer\n\n"
    "Objective: Build a Deep Learning model to classify diseases and map them to explanations.\n\n"
    "Tech Stack:\n"
    "- Python\n- TensorFlow/Keras or PyTorch\n- Jupyter Notebook\n\n"
    "Key Responsibilities:\n"
    "1. Model Architecture: Use Transfer Learning (Recommended: MobileNetV2 for speed or ResNet50 for accuracy).\n"
    "   - Do NOT build from scratch unless necessary.\n"
    "2. Training: Train on the cleaned dataset. Use Categorical Crossentropy loss and Adam optimizer.\n"
    "3. Reasoning System (CRITICAL):\n"
    "   - Create a JSON/Dictionary mapping class names to human-readable explanations.\n"
    "   - Example: {'Tomato_Early_blight': {'cause': 'Fungal infection...', 'cure': 'Use copper fungicide...'}}\n"
    "   - OPTIONAL: Integrate a small LLM (Llama/Gemini) to generate dynamic reasoning.\n"
    "4. Export: Save the trained model (.h5/.pt) and the class_indices mapping.\n\n"
    "Deliverable: 'model.h5' and 'reasoning_map.json'."
)
pdf.chapter_body(role2_text)

# Role 3: Backend
pdf.chapter_title(3, 'Backend Development (API)')
role3_text = (
    "Assignee: Backend Developer\n\n"
    "Objective: Serve the ML model to the web and manage application logic.\n\n"
    "Tech Stack:\n"
    "- Python (FastAPI)\n- Uvicorn\n\n"
    "Key Responsibilities:\n"
    "1. API Setup: Initialize a FastAPI application.\n"
    "2. Prediction Endpoint (/predict):\n"
    "   - Accept POST request with image file.\n"
    "   - Preprocess image (same logic as ML team).\n"
    "   - Run model inference.\n"
    "   - Retrieval: Look up the predicted class in the 'Reasoning Mapping' to get Cause and Cure.\n"
    "   - Return JSON: {prediction, confidence, reasoning, cure}.\n"
    "3. Feedback Loop: Create an endpoint to save user feedback on prediction accuracy.\n"
    "4. CORS: Enable CORS to allow the Frontend to connect.\n\n"
    "Deliverable: A running API server."
)
pdf.chapter_body(role3_text)

# Role 4: Frontend
pdf.chapter_title(4, 'Frontend Development (UI/UX)')
role4_text = (
    "Assignee: Frontend Developer\n\n"
    "Objective: Create a modern, responsive, and visually stunning user interface.\n\n"
    "Tech Stack:\n"
    "- Next.js (React Framework)\n- Tailwind CSS (Styling)\n- Framer Motion (Animations)\n\n"
    "Key Responsibilities:\n"
    "1. Design:\n"
    "   - Theme: Nature/Agriculture (Greens, Earthy tones) but Modern (Glassmorphism).\n"
    "   - Hero Section: 'AI Doctor for your Crops'.\n"
    "2. Upload Feature: Drag & Drop zone with image preview.\n"
    "3. Results Display:\n"
    "   - Show the detected disease clearly.\n"
    "   - Display the 'Reasoning' and 'Cure' in distinct, easy-to-read cards.\n"
    "4. Loading State: Smooth animation while waiting for the model.\n\n"
    "Deliverable: A deployed web application."
)
pdf.chapter_body(role4_text)

# Role 5: Testing
pdf.chapter_title(5, 'Quality Assurance & Testing')
role5_text = (
    "Assignee: QA Engineer\n\n"
    "Objective: Ensure reliability, accuracy, and user experience.\n\n"
    "Tech Stack:\n"
    "- PyTest\n- Postman\n- Jest/Cypress\n\n"
    "Key Responsibilities:\n"
    "1. Model Testing: Evaluate model on the 'Test Set'. Check for False Positives.\n"
    "2. API Testing: Ensure the backend handles large images or invalid files gracefully.\n"
    "3. UI Testing: Check responsiveness on Mobile, Tablet, and Desktop.\n"
    "4. Integration: Verify that the frontend correctly displays data sent by the backend.\n\n"
    "Deliverable: Test report and Bug list."
)
pdf.chapter_body(role5_text)

output_path = "Project_Documentation.pdf"
pdf.output(output_path, 'F')
print(f"PDF generated successfully at: {output_path}")
