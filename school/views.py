from django.shortcuts import render


def home(request):
    highlights = [
        {'title': 'Сучасні класи', 'text': 'Інтерактивні дошки та сучасне обладнання.'},
        {'title': 'Безпечне середовище', 'text': 'Підтримка психолога, наставництво та дружня шкільна спільнота.'},
    ]
    return render(request, 'school/home.html', {'highlights': highlights})


def teachers(request):
    teachers_list = [
        {'name': 'Інга Олексіївна', 'subject': 'Українська мова та література'},
        {'name': 'Віра Василівна', 'subject': 'Математика'},
        {'name': 'Світлана Геннадіївна', 'subject': 'Історія, громадянська освіта, правознавство'},
        {'name': 'Варвара Миколаївна', 'subject': 'Інформатика'},
        {'name': 'Галина Дмитрівна', 'subject': 'Англійська мова'},
        {'name': 'Олена Василівна', 'subject': 'Географія, біологія, природознавство, основи здоров\'я'},
        {'name': 'Леся Миколаївна', 'subject': 'Зарубіжна література'},
        {'name': 'Оксана  Михайлівна', 'subject': 'Фізика'},
        {'name': 'Жанна Олексіївна', 'subject': 'Українська мова'},
        {'name': 'Олександра Олександрівна', 'subject': 'Технології, образотворче мистецтво'},
        {'name': 'Валерій Анатолійович', 'subject': 'Фізична культура'},
        {'name': 'Анастасія Володимирівна', 'subject': 'Інформатика'},
        {'name': 'вакансія вакансія', 'subject': 'вакансія'},
    ]
    return render(request, 'school/teachers.html', {'teachers': teachers_list})


def events(request):
    upcoming_events = [
        {'date': '13 травня 2026', 'title': 'Благодійний ярмарок', 'description': 'Учнівські ініціативи, творчі майстеркласи та збір коштів для ЗСУ.'},
    ]
    return render(request, 'school/events.html', {'events': upcoming_events})
