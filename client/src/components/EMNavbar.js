// @flow

import React, { Component } from 'react';
import {
  Collapse,
  Navbar,
  NavbarToggler,
  NavbarBrand,
  Nav,
  NavLink,
  NavItem,
  UncontrolledDropdown,
  DropdownToggle,
  DropdownMenu,
  DropdownItem,
} from 'reactstrap';
import { userLogout } from '../actions';
import type { BaseReduxPropTypes } from '../types/base-props-types';
import User from '../types/multi-types';

type Props = {
  userData: User,
};

type State = {
  isOpen: boolean,
};

export class EMNavbar extends Component<Props, State> {
  state = {
    isOpen: false,
  };

  logout = () => {
    const { dispatch } = this.props.userData;
    dispatch(userLogout());
  };

  toggle = () => {
    this.setState({
      isOpen: !this.state.isOpen,
    });
  };

  render() {
    const { userState } = this.props.userData;
    const { username, id } = userState.currentUser;
    return (
      <Navbar color="dark" dark expand="md">
        <NavbarToggler onClick={this.toggle} className="mr-2" />
        <NavbarBrand href="/">community-manager</NavbarBrand>
        <Collapse isOpen={this.state.isOpen} navbar>
          <Nav className="ml-auto" navbar>
            <NavItem>
              <NavLink href="/">Home</NavLink>
            </NavItem>
            <NavItem>
              <NavLink href="/about">About</NavLink>
            </NavItem>
            {userState && userState.token ? (
              <UncontrolledDropdown nav inNavbar>
                <DropdownToggle>
                  <span className="fa fa-user-circle fa-lg" />
                </DropdownToggle>
                <DropdownMenu right>
                  <DropdownItem>
                    <strong>{username}</strong>
                  </DropdownItem>
                  <DropdownItem href={`/users/${id}`}>My Profile</DropdownItem>
                  <DropdownItem divider />
                  <DropdownItem onClick={this.logout}>Logout</DropdownItem>
                </DropdownMenu>
              </UncontrolledDropdown>
            ) : (
              <NavItem>
                <NavLink href="/login">Login</NavLink>
              </NavItem>
            )}
          </Nav>
        </Collapse>
      </Navbar>
    );
  }
}
