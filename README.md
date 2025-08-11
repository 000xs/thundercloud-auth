# Thundercloud Authentication™

This is a Flask-based web application that provides a unique and fun authentication system based on emoji sequences.

## 🚀 Features

- **Emoji-based Passwords**: Users sign up and log in using a sequence of weather-related emojis.
- **Creative UI**: The application features a high-contrast, dark-mode theme with a variety of animations to create a dynamic and engaging user experience.
- **Floating Emoji Background**: A floating emoji animation is present on all pages, adding a playful touch to the UI.
- **Responsive Design**: The UI is fully responsive and works on all screen sizes, from mobile phones to desktops.
- **Funny Animations**: The application includes a variety of fun and creative animations, such as a "face-palm" animation on the error page and a "confetti" animation on the success page.

## Project Structure

```
.
├── app.py
├── database.py
├── static
│   └── style.css
├── templates
│   ├── account.html
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   └── auth
│       ├── error.html
│       └── success.html
└── utils.py
```

- **`app.py`**: The main Flask application file.
- **`database.py`**: Handles all database interactions.
- **`static/style.css`**: The main stylesheet for the application.
- **`templates/`**: Contains all the HTML templates for the application.
- **`utils.py`**: Contains utility functions.

## 🏃‍♀️ Running the Application

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the Application**:
   ```bash
   flask run
   ```
3. **Open in Browser**:
   Open your browser and navigate to `http://127.0.0.1:5000`.

## 🎨 Customization

The UI can be easily customized by modifying the `static/style.css` file. The animations can be customized by modifying the keyframe animations in the stylesheet and the JavaScript in the HTML templates.
