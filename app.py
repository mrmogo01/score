from flask import Flask, request, render_template
import gspread
from google.oauth2.gdch_credentials import ServiceAccountCredentials
from google.oauth2.service_account import Credentials

app = Flask(__name__)

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file('credentials.json', scopes=scope)
client = gspread.authorize(creds)

# Откройте таблицу по URL
sheet_api = client.open('Баллы фест').sheet1


@app.route('/')
def leaderboard():
    # Получаем все данные из таблицы
    data = sheet_api.get_all_records()
    # Сортируем данные по сумме баллов в убывающем порядке
    sorted_data = sorted(data, key=lambda x: x['сумма баллов'], reverse=True)
    # Вычисляем общее количество баллов
    total_points = sum(item['сумма баллов'] for item in sorted_data)
    # Отображаем только первые 10 записей
    top_ten = sorted_data[:10]
    return render_template('leaderboard.html', total_points=total_points, top_ten=top_ten)

if __name__ == '__main__':
    app.run(debug=True)

