import React, { Component } from 'react';
import '../App.css';
import Header from './Header/Header';
import { List } from './ListGroup/ListGroup';

/** The App that gets loaded on site */
class App extends Component {
    render() {
        return (
            <div className="App">
                <Header/>
                <List />
            </div>
        );
    }
}

export default App;
