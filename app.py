from flask import Flask, request, render_template
import gspread
from google.oauth2.service_account import Credentials

app = Flask(__name__)

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file('credentials.json', scopes=scope)
client = gspread.authorize(creds)

sheet_api = client.open('Баллы фест').sheet1

@app.route('/', methods=['GET', 'POST'])
def leaderboard():
    query = request.args.get('query', '')
    data = sheet_api.get_all_records()
    sorted_data = sorted(data, key=lambda x: x['сумма баллов'], reverse=True)
    total_points = sum(item['сумма баллов'] for item in sorted_data)

    if query:
        # Фильтрация данных для нахождения информации о человеке с соответствующим ФИО
        filtered_data = [(index + 1, item) for index, item in enumerate(sorted_data) if query.lower() in item['ФИО'].lower()]
        return render_template('leaderboard.html', total_points=total_points, top_ten=sorted_data[:10], filtered_data=filtered_data, query=query)
    else:
        return render_template('leaderboard.html', total_points=total_points, top_ten=sorted_data[:10], filtered_data=None, query='')


if __name__ == '__main__':
    app.run(debug=True)
