// Get the form element and add an event listener for the submit event
const form = document.querySelector('.QuestionInputForm');

form.addEventListener('submit', (event) => {
    // Prevent the default form submission behavior
    event.preventDefault();
    
    // Get the value of the text input
    const questionInput = document.querySelector('.QuestionInput');
    const question = questionInput.value;
    // Send the value of the text input to a Python script
    const xhr = new XMLHttpRequest();
    xhr.open('POST', 'clientInput.py', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.send('question=' + encodeURIComponent(question));
});