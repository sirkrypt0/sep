import React, { Component } from 'react';
import CSRFToken from './csrftoken';
import axios from 'axios';
import Cookies from 'js-cookie';

export default class Login extends Component {
  constructor(props) {
    super(props);
    this.state = {
      username : '',
      password: '',
      csrfmiddlewaretoken: Cookies.get('csrftoken'),
    };
  };

  handleInputChange = (event) => {
    const { value, name } = event.target;
    this.setState({
      [name]: value
    });
  };

  onSubmit = (event) => {
    event.preventDefault();
    console.log(this.state);

    const config = {
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": this.state.csrfmiddlewaretoken,
        "Cookie": "csrftoken="+this.state.csrfmiddlewaretoken,
      },
      withCredentials: true,
		  crossdomain: true,
    };

    const body = JSON.stringify(this.state);

    axios.post("http://localhost:8000/users/login/", body, config)
    .then(function (response) {
      if (response.status === 200) {
        console.log(response);
        alert("Success");
      } else {
        const error = new Error(response.error);
        throw error;
      }
    })
    .catch(function (error) {
      console.log("ERROR");
      console.error(error);
      alert('Error logging in please try again');
    });
  } ;

  render() {
    return (
      <form onSubmit={this.onSubmit}>
        <h1>Login Below!</h1>
        <CSRFToken />
        <input
          type="username"
          name="username"
          placeholder="Enter username"
          value={this.state.username}
          onChange={this.handleInputChange}
          required
        />
        <input
          type="password"
          name="password"
          placeholder="Enter password"
          value={this.state.password}
          onChange={this.handleInputChange}
          required
        />
       <input type="submit" value="Submit"/>
       <a href="http://127.0.0.1:8000/oidc/authenticate">OpenID</a>
      </form>
    );
  }
}