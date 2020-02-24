import React, {Component} from 'react';
import '../App.css';
import Header from './Header/Header';

/** The App that gets loaded on site */
class App extends Component {
  /**
   * renders the App on site
   * @return {[HTMLDivElement]} HTML to be displayed
   */
  render() {
    return (
      <div className="App">
        <Header/>
      </div>
    );
  }
}

export default App;
