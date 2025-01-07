import React, { useEffect, useState } from 'react';
import { getTodos, deleteTodo, createTodo, updateTodo } from '../services/TodoService';
import { setupLogging, logInfo, logError } from '../utils/loggingService'; // Import logging functions

setupLogging(); // Initialize logging

const TodoList = () => {
    const [todos, setTodos] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [newTodo, setNewTodo] = useState({ title: '', description: '', completed: false });
    const [editingTodo, setEditingTodo] = useState(null);

    const fetchTodos = async () => {
        try {
            logInfo('Fetching todos'); // Log action
            const data = await getTodos();
            setTodos(data);
        } catch (error) {
            logError('Error fetching todos:', error); // Log error
            setError('Failed to fetch todos. Please try again later.');
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchTodos();
    }, []);

    const handleDelete = async (todoId) => {
        try {
            logInfo(`Deleting todo with id: ${todoId}`); // Log action
            await deleteTodo(todoId);
            setTodos(todos.filter(todo => todo.id !== todoId));
        } catch (error) {
            logError('Error deleting todo:', error); // Log error
        }
    };

    const handleCreate = async () => {
        try {
            logInfo('Creating new todo'); // Log action
            const createdTodo = await createTodo(newTodo);
            setTodos([...todos, createdTodo]);
            setNewTodo({ title: '', description: '', completed: false });
        } catch (error) {
            logError('Error creating todo:', error); // Log error
        }
    };

    const handleUpdate = async () => {
        try {
            logInfo(`Updating todo with id: ${editingTodo.id}`); // Log action
            const updatedTodo = await updateTodo(editingTodo.id, editingTodo);
            setTodos(todos.map(todo => (todo.id === updatedTodo.id ? updatedTodo : todo)));
            setEditingTodo(null);
        } catch (error) {
            logError('Error updating todo:', error); // Log error
        }
    };

    const handleReload = () => {
        logInfo('Reloading todos'); // Log action
        setLoading(true);
        fetchTodos();
    };

    if (loading) {
        return <div>Loading...</div>;
    }

    return (
        <div className="todo-list">
            <h1>Todo List</h1>
            {error && <div className="error-message">{error}</div>}
            <button className="reload-button" onClick={handleReload}>Reload</button>
            <div className="todo-form">
                <h2>{editingTodo ? 'Edit Todo' : 'Create Todo'}</h2>
                <input
                    type="text"
                    placeholder="Title"
                    value={editingTodo ? editingTodo.title : newTodo.title}
                    onChange={(e) =>
                        editingTodo
                            ? setEditingTodo({ ...editingTodo, title: e.target.value })
                            : setNewTodo({ ...newTodo, title: e.target.value })
                    }
                />
                <input
                    type="text"
                    placeholder="Description"
                    value={editingTodo ? editingTodo.description : newTodo.description}
                    onChange={(e) =>
                        editingTodo
                            ? setEditingTodo({ ...editingTodo, description: e.target.value })
                            : setNewTodo({ ...newTodo, description: e.target.value })
                    }
                />
                <label>
                    Completed:
                    <input
                        type="checkbox"
                        checked={editingTodo ? editingTodo.completed : newTodo.completed}
                        onChange={(e) =>
                            editingTodo
                                ? setEditingTodo({ ...editingTodo, completed: e.target.checked })
                                : setNewTodo({ ...newTodo, completed: e.target.checked })
                        }
                    />
                </label>
                <button className="submit-button" onClick={editingTodo ? handleUpdate : handleCreate}>
                    {editingTodo ? 'Update' : 'Create'}
                </button>
                {editingTodo && <button className="cancel-button" onClick={() => setEditingTodo(null)}>Cancel</button>}
            </div>
            <table className="todo-table">
                <thead>
                    <tr>
                        <th>Title</th>
                        <th>Description</th>
                        <th>Completed</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {todos.map(todo => (
                        <tr key={todo.id}>
                            <td>{todo.title}</td>
                            <td>{todo.description}</td>
                            <td>{todo.completed ? 'Yes' : 'No'}</td>
                            <td>
                                <button className="delete-button" onClick={() => handleDelete(todo.id)}>Delete</button>
                                <button className="edit-button" onClick={() => setEditingTodo(todo)}>Edit</button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default TodoList;
