from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
appointments = []

@app.route('/')
def index():
    return render_template('index.html', appointments=appointments)


# fazendo get e post das informações
@app.route('/schedule', methods=['GET', 'POST'])
def schedule():
    if request.method == 'POST':
        name = request.form['name']
        service = request.form['service']
        date = request.form['date']
        appointments.append({'name': name, 'service': service, 'date': date})
        return redirect(url_for('index'))
    return render_template('schedule.html')

#página adm
@app.route('/admin')
def admin():
    return render_template('admin.html', appointments=appointments)



if __name__ == '__main__':
    app.run(debug=True)
