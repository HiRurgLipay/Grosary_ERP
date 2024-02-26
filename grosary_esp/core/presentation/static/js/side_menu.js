// Обработчик события для кнопки "Добавить ответ"
document.getElementById('add-answer-btn').addEventListener('click', function() {
    var answerInputsContainer = document.getElementById('answer_inputs');
    var newAnswerInput = document.createElement('input');
    newAnswerInput.type = 'text';
    newAnswerInput.name = 'answer_text';
    newAnswerInput.placeholder = 'Введите ответ';
    var noTextCheckbox = document.createElement('input');
    noTextCheckbox.type = 'checkbox';
    noTextCheckbox.id = 'no_text_checkbox';
    noTextCheckbox.name = 'no_text';
    var noTextLabel = document.createElement('label');
    noTextLabel.htmlFor = 'no_text_checkbox';
    noTextLabel.textContent = 'Ответ без текста';
    var br = document.createElement('br');
    answerInputsContainer.appendChild(newAnswerInput);
    answerInputsContainer.appendChild(noTextCheckbox);
    answerInputsContainer.appendChild(noTextLabel);
    answerInputsContainer.appendChild(br);
});

// Обработчик события для выпадающего меню
document.querySelectorAll('.dropdown').forEach(function(dropdown) {
    dropdown.addEventListener('click', function() {
        this.classList.toggle('active');
        var dropdownContent = this.querySelector('.dropdown-content');
        if (dropdownContent.style.display === 'block') {
            dropdownContent.style.display = 'none';
        } else {
            dropdownContent.style.display = 'block';
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.getElementById('menu-toggle'); // Получаем кнопку меню
    const sideMenu = document.getElementById('side-menu'); // Получаем боковое меню

    // Функция для открытия/закрытия бокового меню
    function toggleSideMenu() {
        sideMenu.classList.toggle('open'); // Добавляем/удаляем класс 'open' для показа/скрытия меню
    }

    // Добавляем обработчик события клика на кнопку меню
    menuToggle.addEventListener('click', function() {
        if (sideMenu.classList.contains('open')) {
            sideMenu.classList.remove('open'); // Закрываем меню, если оно уже открыто
        } else {
            toggleSideMenu(); // Открываем меню, если оно закрыто
        }
    });
});

