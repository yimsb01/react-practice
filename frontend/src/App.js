import React from 'react';
import CounterContainer from './containers/CounterContainer';
import Buttons from './components/Buttons';
import Router from './routes/Router';

function App() {
  return (
    <div className="App">
      <h1>test!</h1>
      <CounterContainer />
      <br />
      <Router />
      <br />
      <Buttons />
    </div>
  );
}

export default App;