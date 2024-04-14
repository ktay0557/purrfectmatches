import React from "react";
import Navbar from "react-bootstrap/Navbar";
import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import logo from "../assets/logo.png";
import styles from "../styles/NavBar.module.css";
import { NavLink } from "react-router-dom";

const NavBar = () => {
  return (
    <Navbar className={styles.NavBar} bg="dark" expand="md" fixed="top">
      <Container>
        <NavLink to="/">
          <Navbar.Brand>
            <img src={logo} alt="logo" height="45" />
          </Navbar.Brand>
        </NavLink>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="ml-auto text-left">
              <NavLink 
                exact 
                className={styles.NavLink} 
                activeClassName={styles.Active} 
                to="/"
              >
                <i className="fa-solid fa-house-chimney"></i>Home
              </NavLink>
              <NavLink 
                className={styles.NavLink} 
                activeClassName={styles.Active} 
                to="/signin"
              >
                <i className="fa-solid fa-right-to-bracket"></i>Sign In
              </NavLink>
              <NavLink 
                className={styles.NavLink} 
                activeClassName={styles.Active} 
                to="/signup"
              >
                <i className="fa-solid fa-user-plus"></i>Sign Up
              </NavLink>
            </Nav>
          </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default NavBar;