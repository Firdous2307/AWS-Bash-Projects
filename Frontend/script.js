// Function to submit a POST request to add a task
function submitForm() {
    event.preventDefault();

    // Get form data
    const task = document.getElementById('task').value;
    const deadline = document.getElementById('deadline').value;
    const priority = document.getElementById('priority').value;

    // Create request object
    const xhr = new XMLHttpRequest();

    // Set up request
    xhr.open('POST', 'API_INVOKE_URL/addTask', true);
    xhr.setRequestHeader('Content-Type', 'application/json');

    // Set up response handler
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                alert('Task added successfully!');
                document.getElementById('task').value = '';
                document.getElementById('deadline').value = '';
                document.getElementById('priority').value = 'high'; // Reset priority to default
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

// Function to retrieve tasks via GET request
function getTasks() {
    // Create request object
    const xhr = new XMLHttpRequest();

    // Set up request
    xhr.open('GET', 'API_INVOKE_URL/getTasks', true);

    // Set up response handler
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                const tasks = JSON.parse(xhr.responseText);
                // Handle the retrieved tasks (e.g., display them on the page)
                console.log('Retrieved tasks:', tasks);
            } else {
                alert('Failed to retrieve tasks: ' + xhr.responseText);
            }
        }
    };

    // Send request
    xhr.send();
}

// Function to update a task via PATCH request
function updateTask() {
    // Get task data to update
    const taskToUpdate = 'task_name'; // Replace with the task name you want to update
    const newDeadline = 'new_deadline'; // Replace with the new deadline
    const newPriority = 'new_priority'; // Replace with the new priority

    // Create request object
    const xhr = new XMLHttpRequest();

    // Set up request
    xhr.open('PATCH', `API_INVOKE_URL/updateTask/${taskToUpdate}`, true);
    xhr.setRequestHeader('Content-Type', 'application/json');

    // Set up response handler
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                alert('Task updated successfully!');
            } else {
                alert('Failed to update task: ' + xhr.responseText);
            }
        }
    };

    // Send request
    xhr.send(JSON.stringify({
        deadline: newDeadline,
        priority: newPriority
    }));
}

// Function to delete a task via DELETE request
function deleteTask() {
    // Get task name to delete
    const taskToDelete = 'task_name'; 
    // Create request object
    const xhr = new XMLHttpRequest();

    // Set up request
    xhr.open('DELETE', `API_INVOKE_URL/deleteTask/${taskToDelete}`, true);

    // Set up response handler
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                alert('Task deleted successfully!');
            } else {
                alert('Failed to delete task: ' + xhr.responseText);
            }
        }
    };

    // Send request
    xhr.send();
}
