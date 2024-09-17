<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="refresh" content="10">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
    <title>Leaderboard</title>
<style>
    body {
        font-size: 55px;
        font-family: 'Montserrat', sans-serif;
        background-image: url('https://firebasestorage.googleapis.com/v0/b/digital-portfolio-f8705.appspot.com/o/background.jpg.png?alt=media&token=d8b6f379-bc70-402b-850b-a2cb9e95cd8d');
        background-size: cover;
        background-position: center;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
    }
    ul {
        list-style-type: none;
        padding: 0;
        margin: 0;
        text-align: center;
    }
    li::before {
        content: "";
    }
    .leaderboard {
        text-align: center;
        width: 100%;
    }
    .search-form {
        text-align: center; /* Центрирование формы */
    }
    .search-input {
        width: 50%; /* Увеличение ширины поля ввода */
        font-size: 30px; /* Увеличение размера шрифта в поле ввода */
        padding: 10px; /* Добавление отступов внутри поля ввода */
        margin-top: 20px; /* Отступ сверху */
    }
    .search-button {
        font-size: 30px; /* Увеличение размера шрифта кнопки */
        padding: 10px 20px; /* Увеличение отступов кнопки */
    }
</style>

</head>
<body>
<div class="leaderboard">
    <h1>Общее количество баллов: {{ total_points }}</h1>
    <div class="search-form">
        <form action="/" method="get">
            <input type="text" name="query" class="search-input" placeholder="Введите ФИО" value="{{ query }}">
            <button type="submit" class="search-button">Поиск</button>
        </form>
    </div>

    <ul>
        {% for item in top_ten %}
        <li>{{ loop.index }}) {{ item['ФИО'] }} - {{ item['сумма баллов'] }}</li>
        {% endfor %}
    </ul>

    {% if filtered_data %}
    <h2>Результаты поиска:</h2>
    <ul>
        {% for index, item in filtered_data %}
        <li>{{ index }} {{ item['ФИО'] }} - {{ item['сумма баллов'] }}</li>
        {% endfor %}
    </ul>
    {% endif %}
</div>
</body>
</html>
