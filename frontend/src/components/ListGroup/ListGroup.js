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

  componentDidMount() {
    fetch("http://localhost:8000/api/")
    .then(response => {
      if (response.status > 400) {
        return this.setState(() => {
          return { placeholder: "Something went wrong!" };
        });
      }
      return response.json();
    })
    .then(data => {
      this.setState(() => {
        return {
          data,
          loaded: true
        };
      });
    });
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