from flask import Flask, request, jsonify, render_template
import openpyxl
import os

app = Flask(__name__)

# If file doesn't exist, create it and add headers
excel_file = 'users.xlsx'
if not os.path.exists(excel_file):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Username", "Email", "Password"])
    wb.save(excel_file)

@app.route('/')
def index():
    return render_template('index.html')  # Serve your HTML file

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()

    # Open existing workbook
    wb = openpyxl.load_workbook(excel_file)
    ws = wb.active

    # Append user data
    ws.append([data['username'], data['email'], data['password']])
    wb.save(excel_file)

    return jsonify({"message": "Data saved successfully!"}), 200

if __name__ == '__main__':
    app.run(debug=True)


