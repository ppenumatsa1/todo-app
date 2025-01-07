import React from 'react';
import './App.css';
import Header from './components/Header';
import TodoList from './components/TodoList';

const App = () => {
  return (
    <div className="container">
      <Header />
      <TodoList />
    </div>
  );
};

export default App;

// Ensure your development server is running with hot reloading enabled
if (module.hot) {
  module.hot.accept();
}
