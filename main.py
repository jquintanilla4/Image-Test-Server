from flask import Flask, request
import os
import argparse
# import platform

# Parse command line arguments
parser = argparse.ArgumentParser(description="Start the test image server with the given IP and port.")
parser.add_argument('--ip', type=str, default='0.0.0.0', help='Local IP address for the test server (default:0.0.0.0)')
parser.add_argument('--port', type=int, default=5000, help='Local port number for the test server (default:5000)')
args = parser.parse_args()

# Determine the platform
# platform = platform.system()  # Windows, Linux, Darwin (MacOS)

# Set the path for the uploads folder
uploads_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'testServer_uploads') # Works on MacOS, Windows, and Linux
# Double checking the path
print(uploads_path)
# Create the folder if it doesn't exist
os.makedirs(uploads_path, exist_ok=True)

app = Flask(__name__)

# Decorator tells the function to run the upload function
# when it receives a POST request to the /upload endpoint
# Function handles the upload functionality
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file found in the request.', 400
# it checkes if the POST request contains a file. Returns error if it doesn't.

    # checks if the file was selected
    file = request.files['file']
    if file.filename == '':
        return 'No file selected', 400

    # Save the file to the uploads folder
    save_path = os.path.join(uploads_path, file.filename)
    file.save(save_path)
    return 'File successfully uploaded', 200


# Run the app when script is run directly, not when it's imported
if __name__ == '__main__':
    # arguments change IP and port for testing
    app.run(host=args.ip, port=args.port)
