from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Definindo os serviços e preços no backend
services = [
    {"name": "Corte de Cabelo", "price": 30},
    {"name": "Manicure", "price": 20},
    {"name": "Massagem", "price": 50}
]

appointments = []

@app.route('/')
def index():
    return render_template('index.html', appointments=appointments)

@app.route('/schedule', methods=['GET', 'POST'])
def schedule():
    if request.method == 'POST':
        name = request.form['name']
        selected_services = request.form.getlist('service')  # Captura múltiplos valores de checkbox
        date = request.form['date']

        # Processa cada serviço selecionado para separar o nome e o preço
        processed_services = []
        for service in selected_services:
            service_name, service_price = service.split(' - ')  # Separa nome do serviço e preço
            processed_services.append({'name': service_name, 'price': service_price})

        # Adiciona o agendamento com nome, serviços processados e data
        appointments.append({'name': name, 'services': processed_services, 'date': date})
        return redirect(url_for('index'))
    return render_template('schedule.html', services=services)

@app.route('/admin')
def admin():
    return render_template('admin.html', appointments=appointments)

if __name__ == '__main__':
    app.run(debug=True)
