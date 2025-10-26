from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my Flask API!"

@app.route('/student')
def get_student():
    # Example data - you can change the values
    grade = int(request.args.get('grade', 80))
    remarks = "Pass" if grade >= 75 else "Fail"

    return jsonify({
        "name": "Your Name",
        "grade": grade,
        "section": "Zechariah",
        "remarks": remarks
    })

if __name__ == '__main__':
    app.run(debug=True)
