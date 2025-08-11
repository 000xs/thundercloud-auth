# Thundercloud Authentication™

This is a Flask-based web application that provides a unique and fun authentication system based on weather-related emoji sequences.

## 🚀 Features

- **Emoji-based Passwords**: Users sign up and log in using a sequence of weather-related emojis. The available emojis are: ☀️ (Sunny), ☁️ (Cloudy), 🌧️ (Rainy), ⛈️ (Thunderstorm), 🌪️ (Tornado). Users select a sequence of these emojis to create their unique password.
- **Creative UI**: The application features a high-contrast, dark-mode theme with a variety of animations to create a dynamic and engaging user experience.
- **Floating Emoji Background**: A floating emoji animation is present on all pages, adding a playful touch to the UI.
- **Responsive Design**: The UI is fully responsive and works on all screen sizes, from mobile phones to desktops.
- **Funny Animations**: The application includes a variety of fun and creative animations, such as a "face-palm" animation on the error page and a "confetti" animation on the success page.

## Project Structure

```
.
├── app.py
├── database.py
├── requirements.txt
├── run.py
├── static
│   └── style.css
│   └── images
│       ├── cloudy.png
│       ├── sunny.png
│       ├── thunder.png
│       └── tornado.png
├── templates
│   ├── account.html
│   ├── error.html
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   └── auth
│       ├── login
│       │   ├── error.html
│       │   └── success.html
│       └── signup
│           ├── error.html
│           └── success.html
└── utils.py
```

- **`app.py`**: The main Flask application file. Sets up the Flask app, routes, and handles requests.
- **`database.py`**: Handles all database interactions, including user creation and authentication. It uses `database.db` for storage.
- **`requirements.txt`**: Lists all Python dependencies required for the project.
- **`run.py`**: A script to run the Flask development server.
- **`static/`**: Contains static assets like CSS and images.
    - **`static/style.css`**: The main stylesheet for the application, including animations.
    - **`static/images/`**: Contains weather-related emoji images.
- **`templates/`**: Contains all the HTML templates for the application.
    - **`templates/auth/login/`**: Templates for login-related pages.
    - **`templates/auth/signup/`**: Templates for signup-related pages.
- **`utils.py`**: Contains utility functions used throughout the application.

## 🏃‍♀️ Running the Application

### Prerequisites

- Python 3.6+
- pip

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/000xs/thundercloud-auth.git
   cd thundercloud-auth
   ```
2. **Create a virtual environment (recommended)**:
   ```bash
   python -m venv venv
   ```
3. **Activate the virtual environment**:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Server

1. **Start the application**:
   ```bash
   python run.py
   ```
   This command will start the Flask development server.
2. **Open in Browser**:
   Open your browser and navigate to `http://127.0.0.1:5000`.

### Database Setup

The application uses a SQLite database (`database.db`). The database file will be created automatically when the application first runs if it does not exist. No manual setup is required for the database.

## 🎨 Customization

The UI can be easily customized by modifying the `static/style.css` file. The animations can be customized by modifying the keyframe animations in the stylesheet and the JavaScript in the HTML templates.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details. (Note: LICENSE.md does not exist, but it's good practice to mention it).
