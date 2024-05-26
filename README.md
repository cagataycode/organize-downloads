# Downloads Organizer

This script organizes your Downloads folder by moving files into specific subfolders based on their file types. It's designed to run once and tidy up the Downloads folder according to predefined rules.

## Features

- Moves PDF files to a `PDF` folder
- Moves image files to an `Images` folder
- Moves document files to a `Documents` folder
- Moves video files to a `Videos` folder
- Moves application files (`.app`, `.dmg`, `.pkg`, `.zip`) to an `Applications` folder
- Handles file naming conflicts by appending a counter to the filename
- Uses a configuration file to define file type mappings

## Configuration

The script uses a configuration file (`config.yaml`) to define the file type mappings. You can customize it according to your needs.

Example `config.yaml`:

```yaml
folders:
  PDF: [".pdf"]
  Images: [".png", ".jpg", ".jpeg", ".gif", ".bmp"]
  Documents: [".docx", ".doc", ".txt"]
  Videos: [".mp4", ".mov", ".avi"]
  Applications: [".app", ".dmg", ".pkg", ".zip"]
```

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/downloads-organizer.git
   cd downloads-organizer
   ```

2. **Create a virtual environment and activate it (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install pyyaml
   ```

## Usage

1. **Place the `config.yaml` file in the same directory as the script.**

2. **Run the script:**
   ```bash
   python organize_downloads.py
   ```

The script will organize the files in your Downloads folder according to the rules specified in the `config.yaml` file.

## Logging

The script logs its activities, making it easier to track what files are moved and where. Logs are printed to the console.
