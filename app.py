from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', groom="Тимур", bride="Анастасия")

# Обработчик формы
@app.route('/confirm_attendance', methods=['POST'])
def confirm_attendance():
    name = request.form['name']
    guests = request.form['guests']
    phone = request.form['phone']

    # Здесь можно сохранить данные в файл или базу данных
    with open('guests.txt', 'a', encoding='utf-8') as f:
        f.write(f"{name}, {guests} гостей, Телефон: {phone}\n")

    return "Спасибо за подтверждение! Мы вас ждем!"

if __name__ == '__main__':
    app.run(debug=True)
