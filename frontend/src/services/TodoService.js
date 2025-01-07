import axios from 'axios';
import { logInfo, logError } from '../utils/loggingService'; // Import logging functions

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api/v1';

export const createTodo = async (todo) => {
    try {
        logInfo('Creating todo'); // Log action
        const response = await axios.post(`${API_URL}/todos/`, todo);
        return response.data;
    } catch (error) {
        logError('Error creating todo:', error); // Log error
        throw error;
    }
};

export const getTodos = async (skip = 0, limit = 10) => {
    try {
        logInfo('Retrieving todos'); // Log action
        const response = await axios.get(`${API_URL}/todos/`, {
            params: { skip, limit },
        });
        return response.data;
    } catch (error) {
        logError('Error retrieving todos:', error); // Log error
        throw error;
    }
};

export const getTodo = async (todoId) => {
    try {
        logInfo(`Retrieving todo with id: ${todoId}`); // Log action
        const response = await axios.get(`${API_URL}/todos/${todoId}`);
        return response.data;
    } catch (error) {
        logError('Error retrieving todo:', error); // Log error
        throw error;
    }
};

export const updateTodo = async (todoId, todo) => {
    try {
        logInfo(`Updating todo with id: ${todoId}`); // Log action
        const response = await axios.put(`${API_URL}/todos/${todoId}`, todo);
        return response.data;
    } catch (error) {
        logError('Error updating todo:', error); // Log error
        throw error;
    }
};

export const deleteTodo = async (todoId) => {
    try {
        logInfo(`Deleting todo with id: ${todoId}`); // Log action
        await axios.delete(`${API_URL}/todos/${todoId}`);
    } catch (error) {
        logError('Error deleting todo:', error); // Log error
        throw error;
    }
};
