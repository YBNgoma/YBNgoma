# Image Compressor Web App

A modern, interactive web application built using Python Flask to compress images with a custom compression ratio. This tool was created to compress images efficiently for websites, ensuring faster loading times while maintaining high quality. 

---

## Features

- Interactive user interface with sleek modern design.
- Custom compression ratio selection.
- Supports multiple platforms: Windows, Linux, and macOS.
- Saves compressed images directly to your machine.
- Easy setup and installation.

---

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+**  
- **Pip (Python Package Manager)**  
- A modern web browser for interacting with the UI.

---

## Installation and Setup

Follow the steps below to set up and run the project on **Windows**, **Linux**, or **macOS**.

### 1. Clone the Repository

Clone this repository to your local machine using Git:

```bash
git clone https://github.com/your-username/image-compressor.git
cd image-compressor
```

### 2. Create a Virtual Environment

To isolate dependencies, create and activate a virtual environment:

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux/macOS
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Run the Application

Start the Flask development server:

```bash
python app.py
```

The app will be available at `http://127.0.0.1:5000` in your web browser.

---

## Usage

1. Open the app in your browser.
2. Upload an image using the file input.
3. Adjust the compression ratio as needed.
4. Click **Compress**, and the compressed image will be downloaded immediately.

---

## Cross-Platform Setup Notes

### Windows
- Ensure Python is added to your system's PATH during installation.
- Use `venv\Scripts\activate` to activate the virtual environment.

### Linux/macOS
- Use `source venv/bin/activate` to activate the virtual environment.
- Run `python3` instead of `python` if `python` points to Python 2.x on your system.

---

## Customization

### Changing Compression Ratio
- Edit the compression logic in `app.py` to customize default ratios.

### UI Enhancements
- Update the CSS in `templates/index.html` to adjust the design further.

---

## Technologies Used

- **Python Flask**: Backend framework for handling requests.
- **HTML/CSS**: Frontend for a modern user interface.
- **Pillow**: Image processing library for compression.

---

## Screenshots

### Main Interface
![Main UI](link-to-screenshot)

---

## Contributing

Feel free to fork this repository and make contributions. Submit a pull request for any changes or improvements you make.

---

## License

This project is licensed under the MIT License.

---

### Author

**Created by YassinB**  
This script was designed to compress my images for use on websites, enhancing speed and performance. If you have suggestions or feature requests, feel free to open an issue.

--- 
