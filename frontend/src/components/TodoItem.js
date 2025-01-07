import React from 'react';

const TodoItem = ({ todo }) => {
    return (
        <div>
            <h2>{todo.title}</h2>
            <p>{todo.description}</p>
            <p>Completed: {todo.completed ? 'Yes' : 'No'}</p>
        </div>
    );
};

export default TodoItem;
