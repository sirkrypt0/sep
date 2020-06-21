import React from 'react';
import { Link } from 'react-router-dom';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';

import './Header.css';

export const Header = () => {
  return (
    <Navbar role="navigation">
      <Navbar.Brand as={Link} to="/">Semesterplaner</Navbar.Brand>
      <Nav className="mr-auto">
        <Nav.Link as={Link} to="/">Home</Nav.Link>
        <Nav.Link as={Link} to="/myplans">Meine Pläne</Nav.Link>
        <Nav.Link as={Link} to="/planner">Planer</Nav.Link>
      </Nav>
    </Navbar>
  );
};
