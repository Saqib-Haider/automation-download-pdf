# Automation-download-pdf
This is a simple project which utilizes the Playwright framework for web automation in python language. Specifically, it automates navigating to a webpage in headless mode, locating the download PDF link, and initiating the download process. Once the PDF is downloaded, it then verifies whether the PDF file exists in the project directory or not.

1. Download and install Python 3.10:
https://www.python.org/downloads/release/python-3100/

2. Create a python virtual environment:
```
   python -m venv newenv 
```
3. Activate the virtual environment:
Depending on your operating system, the command to activate the virtual environment will differ
- For Windows:
```
.\newenv\Scripts\activate
```
- For Unix or MacOS
```
source newenv/bin/activate
```
4. Install dependencies from the requirements.txt file:
Once you're in your project directory and in a virtual environment, run the following command to install the dependencies listed in the requirements.txt file:
```
pip install -r requirements.txt
```
5. Verify installation:
After running the command, pip will download and install the packages listed in the requirements.txt file. You can verify that the packages have been installed correctly by running:
```
pip list
```
6. Run the code:
```
python task.py
```
