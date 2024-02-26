// survey.js

// JavaScript code to fetch and display dynamic questions
function fetchQuestion() {
    // Assuming you have a URL endpoint to fetch the next question
    fetch('/get_next_question')
        .then(response => response.json())
        .then(data => {
            document.getElementById('questionText').innerText = data.question;
            document.getElementById('questionId').value = data.question_id;

            // Clear previous options
            document.getElementById('options').innerHTML = '';

            // Append new options
            data.options.forEach(option => {
                if (option.text) {
                    let radioInput = document.createElement('input');
                    radioInput.type = 'radio';
                    radioInput.id = 'option_' + option.id;
                    radioInput.name = 'option_id';
                    radioInput.value = option.id;

                    let label = document.createElement('label');
                    label.htmlFor = 'option_' + option.id;
                    label.innerText = option.text;

                    document.getElementById('options').appendChild(radioInput);
                    document.getElementById('options').appendChild(label);
                    document.getElementById('options').appendChild(document.createElement('br'));
                } else {
                    let label = document.createElement('label');
                    label.for = 'custom_answer';
                    label.innerText = 'Введите свой ответ:';

                    let input = document.createElement('input');
                    input.type = 'text';
                    input.id = 'custom_answer';
                    input.name = 'custom_answer';

                    document.getElementById('options').appendChild(label);
                    document.getElementById('options').appendChild(document.createElement('br'));
                    document.getElementById('options').appendChild(input);
                    document.getElementById('options').appendChild(document.createElement('br'));
                }
            });
        })
        .catch(error => console.error('Error fetching question:', error));
}

// Fetch question when the page loads
fetchQuestion();

// Optionally, you can also refresh the question at regular intervals
// setInterval(fetchQuestion, 5000); // Refresh every 5 seconds, for example
