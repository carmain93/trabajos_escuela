import React, { useState } from 'react';

function TodoApp() {
  const [tasks, setTasks] = useState([]);
  const [taskInput, setTaskInput] = useState('');

  const addTask = () => {
    if (taskInput.trim() !== '') {
      setTasks([...tasks, { id: tasks.length + 1, content: taskInput }]);
      setTaskInput('');
    }
  };

  const deleteTask = (id) => {
    setTasks(tasks.filter(task => task.id !== id));
  };

  const updateTask = (id, newContent) => {
    setTasks(tasks.map(task => {
      if (task.id === id) {
        return { ...task, content: newContent };
      }
      return task;
    }));
  };

  return (
    <div>
      <h1>Todo List</h1>
      <input 
        type="text" 
        placeholder="Add task..." 
        value={taskInput} 
        onChange={(e) => setTaskInput(e.target.value)} 
      />
      <button onClick={addTask}>Add Task</button>
      <ul>
        {tasks.map(task => (
          <li key={task.id}>
            <input 
              type="text" 
              value={task.content} 
              onChange={(e) => updateTask(task.id, e.target.value)} 
            />
            <button onClick={() => deleteTask(task.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TodoApp;
