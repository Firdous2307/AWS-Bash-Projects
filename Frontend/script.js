// Function to submit a POST request to add a task
function submitForm(event) {
    event.preventDefault();

    // Get form data
    const task = document.getElementById('task').value;
    const deadline = document.getElementById('deadline').value;
    const priority = document.getElementById('priority').value;

    // Create request object
    const xhr = new XMLHttpRequest();

    // Set up request
    xhr.open('POST', 'https://fczp9ttbpb.execute-api.us-east-2.amazonaws.com/prod/addTask', true);
    xhr.setRequestHeader('Content-Type', 'application/json');

    // Set up response handler
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                alert('Task added successfully!');
                document.getElementById('task').value = '';
                document.getElementById('deadline').value = '';
                document.getElementById('priority').value = ''; 
            } else {
                alert('Task addition failed: ' + xhr.responseText);
            }
        }
    };

    // Send request
    xhr.send(JSON.stringify({
        task: task,
        deadline: deadline,
        priority: priority
    }));
}
