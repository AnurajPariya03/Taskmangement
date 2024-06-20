import React from 'react';
import { useNavigate } from 'react-router-dom';

const TaskDetail = ({ task, onClose }) => {
  const navigate = useNavigate();

  const handleClose = () => {
    if (onClose) {
      onClose();
    }
    navigate('/');
  };

  return (
    <div className="p-4">
      <div className="max-w-md mx-auto bg-white shadow-md rounded-lg overflow-hidden">
        <div className="p-4">
          <h1 className="text-2xl font-bold mb-4">{task.title}</h1>
          <p className="text-sm text-gray-500">{task.description}</p>
          <p className="text-sm text-gray-500">Due Date: {task.due_date}</p>
        </div>
        <div className="px-4 py-3 bg-gray-50 text-right sm:px-6">
          <button
            onClick={handleClose}
            className="bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded"
          >
            Close
          </button>
        </div>
      </div>
    </div>
  );
};

export default TaskDetail;
