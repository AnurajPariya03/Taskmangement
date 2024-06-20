// import React from 'react';
import { Link } from 'react-router-dom';

const TaskList = ({ tasks, onDelete, onView }) => {
  return (
    <div className="min-h-screen p-4 bg-gray-100">
      <h1 className="text-2xl font-bold mb-4">Tasks</h1>
      {tasks.length === 0 ? (
        <p>No tasks available</p>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
          {tasks.map(task => (
            <div key={task.id} className="bg-white p-6 rounded-lg shadow-md">
              <h2 className="text-xl font-semibold mb-2">{task.title}</h2>
              <p className="text-gray-700 mb-2">{task.description}</p>
              <div className="flex space-x-2 mt-2">
                <Link 
                  to={`/tasks/${task.id}`} 
                  className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-700 transition duration-300" 
                  onClick={() => onView(task.id)}
                >
                  View
                </Link>
                <Link 
                  to={`/update-task/${task.id}`} 
                  className="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-700 transition duration-300"
                >
                  Update
                </Link>
                <button
                  onClick={() => onDelete(task.id)}
                  className="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-700 transition duration-300"
                >
                  Delete
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default TaskList;
