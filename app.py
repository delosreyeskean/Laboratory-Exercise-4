from flask import Flask, render_template, request

app = Flask(__name__)

exercise_descriptions = {
    'exercise1': 'This is the description of Laboratory Exercise 1.',
    'exercise2': 'This is the description of Laboratory Exercise 2.',
    'exercise3': 'This is the description of Laboratory Exercise 3.'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works', methods=['GET', 'POST'])
def works():
    return render_template('works.html', exercise_descriptions=exercise_descriptions)


@app.route('/contact')
def contact():
    return  render_template('contact.html')

@app.route('/touppercase', methods=['GET', 'POST'])
def touppercase():
    uppercased_text = ""
    if request.method == 'POST':
        input_text = request.form.get('input_text', '')
        uppercased_text = input_text.upper()
    return render_template('touppercase.html', uppercased_text=uppercased_text)

@app.route('/areaofcircle', methods=['POST', 'GET'])
def calculate_area():
    if request.method == 'POST':
        try:
            radius = float(request.form['radius'])
            area = 3.141592653589793238 * (radius ** 2)
            return render_template('areaofcircle.html', radius=radius, area=area)
        except ValueError:
            return "Please enter a valid number for the radius."
    return render_template('areaofcircle.html', radius=None, area=None)

@app.route('/areaoftriangle')
def triangle_calculator():
    return render_template('areaoftriangle.html')

@app.route('/calculate', methods=['POST'])
def calculate_areat():
    base = float(request.form['base'])
    height = float(request.form['height'])
    area = 0.5 * base * height
    return f'The area of the triangle is {area} square units.'




if __name__ == "__main__":
    app.run(debug=True)
