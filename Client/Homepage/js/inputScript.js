// Get the value of the input form
const question = document.getElementById('question').value;

// Send a POST request to the server with the question data
fetch('/newmessage/' + question, {
  method: 'GET'
})
.then(response => {
  if (!response.ok) {
    throw new Error('Network response was not ok');
  }
  // Do something with the response
    return response.json();

})
.catch(error => {
  console.error('There was a problem with the fetch operation:', error);
  
});

