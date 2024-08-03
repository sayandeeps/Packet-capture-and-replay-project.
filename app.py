from flask import Flask, render_template, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-traffic', methods=['POST'])
def generate_traffic():
    result = subprocess.run(['python3', 'gentraffic.py'], capture_output=True, text=True)
    print(result.stdout)  # Print the output to the console for debugging
    return redirect(url_for('index'))

@app.route('/replay', methods=['POST'])
def replay():
    result = subprocess.run(['python3', 'replay.py'], capture_output=True, text=True)
    print(result.stdout)  
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
