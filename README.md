This is image detection project using Google Cloud vision API
<br>
# Google Cloud Vision API Image Label Detection

## Overview
This project utilizes the **Google Cloud Vision API** to perform **image label detection**. Given an image, the API returns labels (descriptions) and their confidence scores.

## Prerequisites
Ensure you have the following before running the project:
- Python **3.x** installed
- A valid **Google Cloud Platform (GCP) account**
- A **service account JSON key** (`gcp_key.json`) for authentication
- The required Python dependencies installed

## Installation

### 1. Install Required Dependencies
Run the following command to install the necessary libraries:
```sh
pip install google-cloud-vision
```

### 2. Set Up Google Cloud Authentication
Ensure your **service account key file (`gcp_key.json`)** is available in the project directory.

Alternatively, set the environment variable:
```sh
export GOOGLE_APPLICATION_CREDENTIALS="path/to/gcp_key.json"
```
For Windows (PowerShell):
```sh
$env:GOOGLE_APPLICATION_CREDENTIALS="path/to/gcp_key.json"
```

## Usage
### Running the Script
```sh
python script.py
```

### Sample Code (`script.py`)
```python
from google.cloud import vision
import io

# Initialize the Vision API client
client = vision.ImageAnnotatorClient.from_service_account_file('gcp_key.json')

# Load image
image_path = "car2.png"
with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

# Create an image object for Vision API
image = vision.Image(content=content)

# Perform label detection
response = client.label_detection(image=image)
labels = response.label_annotations

# Print detected labels and confidence scores
for label in labels:
    print(f"{label.description}: {label.score:.2f}")
```

## Expected Output
For an image of a car (`car2.png`), the output might look like:
```
Car: 0.98
Vehicle: 0.95
Automobile: 0.93
```

## Troubleshooting
### **ModuleNotFoundError: No module named 'google'**
Run:
```sh
pip install google-cloud-vision
```

### **Invalid Service Account Key Error**
Ensure `gcp_key.json` is correctly configured and accessible.

## License
This project is licensed under the **MIT License**.

## Author
Kowshik ch


