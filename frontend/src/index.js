import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import { setupLogging } from './utils/loggingService'; // Import setupLogging

setupLogging(); // Initialize logging

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

// Ensure your development server is running with hot reloading enabled
if (module.hot) {
  module.hot.accept('./App', () => {
    const NextApp = require('./App').default;
    ReactDOM.render(
      <React.StrictMode>
        <NextApp />
      </React.StrictMode>,
      document.getElementById('root')
    );
  });
}
