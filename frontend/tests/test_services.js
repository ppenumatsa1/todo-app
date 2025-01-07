import axios from 'axios';
import MockAdapter from 'axios-mock-adapter';
import { getTodos, createTodo, updateTodo, deleteTodo } from '../src/services/TodoService'; // Ensure this path is correct

const mock = new MockAdapter(axios);

describe('Todo Services', () => {
    beforeEach(() => {
        mock.reset();
    });

    test('getTodos should return a list of todos', async () => {
        const todos = [{ id: 1, title: 'Test Todo', completed: false }];
        mock.onGet('http://localhost:8000/api/v1/todos/').reply(200, todos);

        const result = await getTodos();
        expect(result).toEqual(todos);
    });

    test('createTodo should add a new todo', async () => {
        const newTodo = { title: 'Test Todo', completed: false };
        const createdTodo = { id: 1, ...newTodo };
        mock.onPost('http://localhost:8000/api/v1/todos/').reply(201, createdTodo);

        const result = await createTodo(newTodo);
        expect(result).toEqual(createdTodo);
    });

    test('updateTodo should modify an existing todo', async () => {
        const updatedData = { title: 'Updated Todo', completed: true };
        const updatedTodo = { id: 1, ...updatedData };
        mock.onPut('http://localhost:8000/api/v1/todos/1').reply(200, updatedTodo);

        const result = await updateTodo(1, updatedData);
        expect(result).toEqual(updatedTodo);
    });

    test('deleteTodo should remove a todo', async () => {
        mock.onDelete('http://localhost:8000/api/v1/todos/1').reply(204);

        await deleteTodo(1);
        expect(mock.history.delete.length).toBe(1);
    });
});