from flask import Flask, request, render_template_string
import subprocess
import os
import zipfile

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template_string('''
        <form method="POST" action="/run" enctype="multipart/form-data">
            <input type="file" name="folder" accept=".zip">
            <input type="submit" value="Upload and Run">
        </form>
    ''')

@app.route('/run', methods=['POST'])
def run():
    if 'folder' not in request.files:
        return 'No file part'
    file = request.files['folder']
    if file.filename == '':
        return 'No selected file'
    if file and file.filename.endswith('.zip'):
        zip_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(zip_path)
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(UPLOAD_FOLDER)
        output = ''
        for root, dirs, files in os.walk(UPLOAD_FOLDER):
            for filename in files:
                if filename.endswith('.py'):
                    filepath = os.path.join(root, filename)
                    try:
                        result = subprocess.run(['python', filepath], capture_output=True, text=True)
                        output += f'<h3>{filename} Output:</h3><pre>{result.stdout + result.stderr}</pre>'
                    except Exception as e:
                        output += f'<h3>{filename} Error:</h3><pre>{str(e)}</pre>'
        return f'<h1>File Outputs:</h1>{output}'
    else:
        return 'Invalid file type. Please upload a .zip file containing Python files.'

if __name__ == '__main__':
    app.run()
