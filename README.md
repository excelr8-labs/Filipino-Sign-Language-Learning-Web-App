# Filipino Sign Language Learning Web App

This is a web application designed to help users learn Filipino Sign Language (FSL). The app provides an interactive experience with features such as a searchable dictionary, categorized learning sections, user account management, and quiz/flashcards to test knowledge.

## Features

1. **Dictionary**

    - Search for words to see their corresponding Filipino Sign Language signs.
    - Video or GIF demonstrations of the signs.

2. **Learning Categories**

    - Browse signs organized into categories like "Love" "Conversation," etc.
    - Each category contains a list of related signs.

3. **User Accounts**

    - Sign up, log in, and manage your account.
    - Track progress and performance in quizzes.

4. **Quiz and Flashcards**
    - Test your knowledge with interactive quizzes.
    - Use flashcards to practice and reinforce learning.

## Apps and Their Purposes

### 1. **dictionary**

-   **Purpose**:
    -   Serves as the searchable dictionary for the application.
    -   Allows users to input a word and view its corresponding Filipino Sign Language (FSL) sign, displayed as an image, video, or GIF.
-   **Features**:
    -   Search functionality for FSL words.
    -   Management of FSL sign entries (CRUD operations for administrators).

---

### 2. **learning**

-   **Purpose**:
    -   Provides categorized learning resources for users to explore and learn FSL signs based on different themes or topics.
-   **Features**:
    -   Displays categories such as "Love," "Conversation," etc.
    -   Each category contains related FSL signs.
    -   Easy navigation and user-friendly design to facilitate learning.

---

### 3. **accounts**

-   **Purpose**:
    -   Manages user authentication and account-related functionalities.
-   **Features**:
    -   User registration and login/logout.
    -   Profile management.
    -   Tracks user progress in quizzes and learning modules.

---

### 4. **quizzes**

-   **Purpose**:
    -   Tests users' knowledge of FSL through interactive quizzes and flashcards.
    -   Helps reinforce learning and identify areas for improvement.
-   **Features**:
    -   Multiple-choice quizzes based on signs from the dictionary and learning modules.
    -   Flashcards for practice.
    -   Scoring and progress tracking.

---

## Installation

1. Clone the repository:

```bash
   git clone https://github.com/yourusername/filipino-sign-language.git
   cd filipino-sign-language
```

2. Set up a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run migrations:

```bash
python manage.py migrate
```

5. Start the development server:

```bash
python manage.py runserver
```

6. Open your browser and visit:

```bash
http://127.0.0.1:8000/
```
