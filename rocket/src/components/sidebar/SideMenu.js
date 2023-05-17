import airforce108 from "../../assets/logo/logoSideBar/airforce108.png";
import airforcelogo from "../../assets/logo/logoSideBar/airforce.png";
import React, { useState, useEffect, useContext } from "react";
import { FileNameContext } from "../../App";
import MenuItem from "./MenuItem";
import axios from "axios";

axios.defaults.withCredentials = true;
const SideMenu = () => {
  const Swal = require("sweetalert2");

  const { token, setToken, admin, setAdmin, setUserName } =
    useContext(FileNameContext);
  const [inactive, setInactive] = useState(false);

  let tokenStorage, adminStorage, userNameStorage;
  tokenStorage = localStorage.getItem("user");
  adminStorage = localStorage.getItem("admin");
  userNameStorage = localStorage.getItem("username");
  setToken(tokenStorage);
  setAdmin(adminStorage);

  const Toast = Swal.mixin({
    toast: true,
    position: "top-end",
    showConfirmButton: false,
    timer: 2500,
    timerProgressBar: true,

    didOpen: (toast) => {
      toast.addEventListener("mouseenter", Swal.stopTimer);
      toast.addEventListener("mouseleave", Swal.resumeTimer);
    },
  });

  const handleLogout = () => {
    let success = 0;
    setToken(null);
    setUserName("");
    setAdmin(false);
    if (adminStorage) {
      localStorage.removeItem("admin");
      success += 1;
    }
    if (tokenStorage) {
      localStorage.removeItem("usename");
      success += 1;
    }
    if (userNameStorage) {
      localStorage.removeItem("user");
      success += 1;
    }
    if (success == 3) {
      Toast.fire({
        icon: "success",
        title: "Log out successfully",
      });
    }
    if (success != 3) {
      Toast.fire({
        icon: "error",
        title: "Log out failed",
      });
    }
    success = 0;
  };

  useEffect(() => {
    if (inactive) {
      document.querySelectorAll(".sub-menu").forEach((el) => {
        el.classList.remove("active");
      });
    }
  }, [inactive]);

  const showDataUser = () => {
    if (token) {
      if (admin && admin !== "false") {
        return true;
      }
    }
    return false;
  };

  return (
    <div className={`side-menu ${inactive ? "inactive" : ""}`}>
      <div className="top-section">
        <div className="logo">
          <img src={airforcelogo} alt="logo" />
        </div>
        <div onClick={() => setInactive(!inactive)} className="toggle-menu-btn">
          {inactive ? (
            <i class="bi bi-arrow-left-square-fill"></i>
          ) : (
            <i class="bi bi-arrow-right-square-fill"></i>
          )}
        </div>
      </div>

      <div className="search-controller">
        <button className="search-btn">
          <i class=""></i>
        </button>
        <input type="text" placeholder="" />
      </div>

      <div className="divider"></div>

      <div className="main-menu">
        <ul>
          {token ? (
            <>
              <MenuItem
                name="Log out"
                to="/"
                iconClassName="bi bi-box-arrow-in-right"
                onClick={handleLogout}
              />
              <MenuItem
                name="Live Stream"
                to="/live"
                iconClassName="bi bi-camera-video"
              />
              <MenuItem
                name="Investigation Screen"
                to="/investigation"
                iconClassName="bi bi-display"
              />
              {showDataUser() ? (
                <>
                  <MenuItem
                    name="Settings"
                    to="/settings"
                    iconClassName="bi bi-gear"
                  />
                  <MenuItem
                    name="Add Users"
                    to="/adduser"
                    iconClassName="bi bi-person-plus"
                  />
                </>
              ) : null}
            </>
          ) : (
            <>
              <MenuItem
                name="Verify"
                to="/"
                iconClassName="bi bi-shield-lock"
              />
            </>
          )}
        </ul>
      </div>
      <div className="side-menu-footer">
        <div className="avatar">
          <img src={airforce108} alt="user" />
        </div>
        <div className="user-info">
          <h6>{token ? userNameStorage : "Identify for using"}</h6>
          <h6>{token ? "" : "the system"}</h6>
          {token ? (
            <h6>
              {showDataUser() ? "System administrator" : "System operator"}
            </h6>
          ) : (
            ""
          )}
        </div>
      </div>
    </div>
  );
};

export default SideMenu;
