from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='template')

def get_last_log_entries(num_entries=5):
    try:
        with open('system_health_log.txt', 'r') as file:
            lines = file.readlines()
            return "<br>".join(lines[-num_entries:])  # Get the last 5 entries
    except FileNotFoundError:
        return "Log file not found."

@app.route('/')
def index():
    log_data = get_last_log_entries()
    return render_template('index.html', log_data=log_data)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
