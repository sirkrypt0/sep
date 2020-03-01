import React, {Component} from 'react';
import {ListGroup, ListGroupItem } from 'react-bootstrap';

import './ListGroup.css'

class List extends Component{
  constructor(props) {
    super(props);
    this.state = {
        data: [],
        loaded: false,
        placeholder: "Loading"
    }
  }

  async componentDidMount() {
    try {
      const response = await fetch("http://localhost:8000/api/");
      const data = await response.json();
      this.setState({
        data
      });
    }
    catch(exception){
      console.log(exception);
    }
  }

  render() {
    return(
      <ListGroup>
        {this.state.data.map(lecture => {
          return (
              <ListGroupItem key={lecture.id}>
                {lecture.title}
              </ListGroupItem>
          );
        })}
      </ListGroup>
    );
  }
}

export default List;