import 'react-app-polyfill/ie11'
import React from 'react';
import ReactDOM from 'react-dom';
import App from './components/App'


// Take the react component and show it on the screen
ReactDOM.render(
    < App />,
    document.querySelector('#root')
);
