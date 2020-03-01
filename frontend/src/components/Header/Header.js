import React, {Component} from 'react';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';

import './Header.css';

/** The header containing all necessary links */
class Header extends Component {
  /**
   * renders the Header on site
   * @return {[HTMLDivElement]} HTML to be displayed
   */
  render() {
    return (
      <Navbar role="navigation">
        <Navbar.Brand href="/">Semesterplaner</Navbar.Brand>
        <Nav className="mr-auto">
          <Nav.Link href="/">Home</Nav.Link>
          <Nav.Link href="/myplans">Meine Pläne</Nav.Link>
          <Nav.Link href="/planner">Planer</Nav.Link>
        </Nav>
      </Navbar>
    );
  }
}
export default Header;
