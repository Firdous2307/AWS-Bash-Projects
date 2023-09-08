// Function to submit a POST request to add a task
function submitForm(event) {
    event.preventDefault();

    // Get form data
    const task_id = document.getElementById('task_id').value;
    const task = document.getElementById('task').value;
    const priority = document.getElementById('priority').value;

    // Create request object
    const xhr = new XMLHttpRequest();

    // Set up request
    xhr.open('POST', 'https://e2vjdjotya.execute-api.us-east-2.amazonaws.com/prod/addtask', true);
    xhr.setRequestHeader('Content-Type', 'application/json');

    // Set up response handler
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                alert('Task added successfully!');
                document.getElementById('task_id').value = '';
                document.getElementById('task').value = '';
                document.getElementById('priority').value = ''; 
            } else {
                alert('Task addition failed: ' + xhr.responseText);
            }
        }
    };

    // Send request
    xhr.send(JSON.stringify({
        task_id: task_id,
        task: task,
        priority: priority
    }));
}
