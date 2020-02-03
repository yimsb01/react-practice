import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

import { createStore } from 'redux';
import rootReducer from './store/modules';
import { Provider } from 'react-redux';

import App from './App';
import * as serviceWorker from './serviceWorker';

const store = createStore(rootReducer);
console.log(store.getState());

ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('root'));
serviceWorker.unregister();
