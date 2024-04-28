import React from "react";
import { toast } from "react-toastify";
import { NavLink } from "react-router-dom";

import Navbar from "react-bootstrap/Navbar";
import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";

import logo from "../assets/logo.png";
import styles from "../styles/NavBar.module.css";
import { useCurrentUser, useSetCurrentUser } from "../contexts/CurrentUserContext";
import Avatar from "./Avatar";
import UseClickOutsideToggle from "../hooks/UseClickOutsideToggle";
import { removeTokenTimestamp } from "../utils/utils";

import { axiosReq } from "../api/axiosDefaults";

const NavBar = () => {
    const currentUser = useCurrentUser();
    const setCurrentUser = useSetCurrentUser();
    const isAdminUser = currentUser && currentUser.is_staff_user;

    const { expanded, setExpanded, ref } = UseClickOutsideToggle();

    // Handle log out functionality
    const handleSignOut = async () => {
        try {
            await axiosReq.post("dj-rest-auth/logout/");
            setCurrentUser(null);
            removeTokenTimestamp();
            toast.success("Signed out successfully!", { position: "top-center" });
        } catch (err) {
            // console.log(err);
        }
    };

    // Provides icons to staff members when logged in
    const isAdminIcons = (
        <>
            <NavLink
                className={styles.NavLink}
                activeClassName={styles.Active}
                to="/adverts/create"
            >
                <i className="fa-regular fa-square-plus"></i>Create Advert
            </NavLink>
            <NavLink
                exact
                className={styles.NavLink}
                activeClassName={styles.Active}
                to="/adoptions"
            >
                <i className="fa-solid fa-clipboard-list"></i>Adoptions
            </NavLink>
        </>
    )

    // Provides icons to logged in users
    const loggedInIcons = <>
        <NavLink
            className={styles.NavLink}
            activeClassName={styles.Active}
            to="/liked"
        >
            <i className="fa-solid fa-thumbs-up"></i>Liked
        </NavLink>
        <NavLink
            className={styles.NavLink}
            activeClassName={styles.Active}
            to="/adoptions/create"
        >
            <i className="fa-solid fa-list"></i>Adopt a Cat
        </NavLink>

        <NavLink
            className={styles.NavLink}
            activeClassName={styles.Active}
            to="/about"
        >
            <i className="fa-solid fa-address-card"></i>About
        </NavLink>
        <NavLink
            className={styles.NavLink}
            to="/"
            onClick={handleSignOut}
        >
            <i className="fa-solid fa-right-from-bracket"></i>Sign Out
        </NavLink>
        <NavLink
            className={styles.NavLink}
            to={`/profiles/${currentUser?.profile_id}`}
        >
            <Avatar src={currentUser?.profile_image} text="Profile" height={40} />
        </NavLink>
    </>
    
    // Provides icons for all users not logged in
    const loggedOutIcons = (
        <>
            <NavLink
                className={styles.NavLink}
                activeClassName={styles.Active}
                to="/about"
            >
                <i className="fa-solid fa-address-card"></i>About
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
        </>
    )
    return (
        <Navbar
            expanded={expanded}
            className={styles.NavBar}
            expand="xl"
            fixed="top"
        >
            <Container>
                <NavLink to="/">
                    <Navbar.Brand>
                        <img src={logo} alt="logo" height="45" />
                    </Navbar.Brand>
                </NavLink>
                <Navbar.Toggle
                    ref={ref}
                    onClick={() => setExpanded(!expanded)}
                    aria-controls="basic-navbar-nav"
                />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="ml-auto text-left">
                        {isAdminUser ? isAdminIcons : null}
                        <NavLink
                            exact
                            className={styles.NavLink}
                            activeClassName={styles.Active}
                            to="/"
                        >
                            <i className="fa-solid fa-cat"></i>Cats
                        </NavLink>
                        {currentUser ? loggedInIcons : loggedOutIcons}
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
};

export default NavBar;