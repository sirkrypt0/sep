import React, { Component } from 'react';
import './ListGroup.css';

export class List extends Component {
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
      <div className="list"> Lectures
        <div className="listbox" id="rectangle">
          {this.state.data.map((lecture, id) => {
            return (
              <a href="#" className="list-group-item" list-group-item-action flex-column align-items-start key={id}>
                <div className="d-flex w-100 justify-content-between">
                  <h5 className="mb-1">{lecture.title}</h5>
                  <small>{lecture.lp} LP</small>
                </div>
                <div className="d-flex w-100 justify-content-between">
                  <h6 className="mb-1">{lecture.lecturer.name}</h6>
                  <small>{lecture.semester}. Semester</small>
                </div>
              </a>
            )
            })}
        </div>
      </div>
    );
  }
}
