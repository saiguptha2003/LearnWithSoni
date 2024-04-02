# LearnWithSoni

LearnWithSoni is a Flask-based web application designed to provide educational resources and tools for students and teachers. The application allows users to register, log in, access study materials, take exams, and receive feedback on their performance.

## Features

- User Authentication: Users can register and log in to access the application's features.
- Exam Module: Provides the ability for users to take exams with randomized questions and receive instant feedback on their performance.
- Admin Portal: Allows administrators to view user details, exam scores, and feedback.
- Email Verification: Sends verification emails to users upon registration to ensure account security.
- Firebase Integration: Utilizes Firebase for user authentication, database storage, and email services.

## Setup

To set up the LearnWithSoni application locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/saiguptha2003/LearnWithSoni.git
    ```

2. Navigate to the project directory:

    ```bash
    cd LearnWithSoni
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:

    ```bash
    python app.py
    ```

5. Open your web browser and navigate to `http://localhost:5000` to access the application.

## Usage

1. Register for an account using a valid email address.
2. Log in to access the application's features.
3. Explore study materials, take exams, and view feedback on your performance.
4. Administrators can access the admin portal to view user details, exam scores, and feedback.

## Technology Stack

- Flask: Web application framework
- Firebase: Authentication, database, and email services
- Pandas: Data manipulation and analysis
- Pyrebase: Python wrapper for Firebase
- Flask-Mail: Email sending capabilities for Flask applications

## Contributing

Contributions to the LearnWithSoni project are welcome! If you encounter any issues, have suggestions for improvements, or would like to contribute new features, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
