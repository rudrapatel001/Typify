# Typing Test Web Application

A simple Django web application to test typing speed and accuracy. It displays a random word, and users can type it out to see how fast and accurately they can type.

## Features

- **Random Word Display**: Shows words to type.
- **Typing Speed Calculation**: Calculates words per minute (WPM).
- **Typing Accuracy Calculation**: Displays typing accuracy percentage.

## Technologies Used

- **Django**: Web framework used for the backend.
- **HTML**: For the structure of the web page.
- **CSS**: For styling the web page.
- **JavaScript**: For interactive functionality.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/rudrapatel001/typing-test.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd typing-test
   ```

3. **Create a Virtual Environment:**

   ```bash
   python -m venv venv
   ```

4. **Activate the Virtual Environment:**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

6. **Apply Migrations:**

   ```bash
   python manage.py migrate
   ```

7. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

8. **Access the Application:**

   Open `http://127.0.0.1:8000/` in your web browser to view the application.

## File Structure

- `manage.py`: Command-line utility for managing the Django project.
- `typing_test/`: Directory containing the Django project settings and configurations.
- `typing_test/settings.py`: Django settings file.
- `typing_test/urls.py`: URL configuration for the Django project.
- `typing_test/views.py`: Contains the views for the application.
- `templates/`: Directory containing HTML templates.
  - `typing_test/index.html`: The main HTML template.
- `static/`: Directory for static files (CSS, JavaScript).

## Usage

1. **Open the Application:**

   Open `http://127.0.0.1:8000/` in your web browser to view the application.

2. **Start Typing:**

   A random word will be displayed. Start typing in the provided text area.

3. **View Metrics:**

   Typing speed (WPM) and accuracy will be updated in real-time.

## Troubleshooting

- Ensure you have Python and Django installed.
- If the server is not running, check for any errors in the terminal.
- Ensure the database is set up correctly by running migrations.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## Contact

For questions or feedback, please contact [rudra7042004@gmail.com](mailto:rudra7042004@gmail.com).

