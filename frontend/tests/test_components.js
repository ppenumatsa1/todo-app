import React from 'react';
import { render, screen, act } from '@testing-library/react';
import TodoItem from '../src/components/TodoItem';
import TodoList from '../src/components/TodoList';

describe('TodoItem', () => {
    test('renders TodoItem correctly', () => {
        const todo = { title: 'Test Todo', description: 'Test Description', completed: false };
        render(<TodoItem todo={todo} />);
        expect(screen.getByText('Test Todo')).toBeInTheDocument();
        expect(screen.getByText('Test Description')).toBeInTheDocument();
        expect(screen.getByText('Completed: No')).toBeInTheDocument();
    });
});

describe('TodoList', () => {
    test('renders TodoList correctly', async () => {
        await act(async () => {
            render(<TodoList />);
        });
        expect(screen.getByText('Todo List')).toBeInTheDocument();
    });

    test('displays loading state initially', async () => {
        await act(async () => {
            render(<TodoList />);
        });
        expect(screen.getByText('Loading...')).toBeInTheDocument();
    });

    // Add more tests as needed for your component's functionality
});