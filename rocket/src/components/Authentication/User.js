import React, { useContext, useState, useEffect } from "react";
import { FileNameContext } from "../../App";
import { Navigate } from "react-router";
import axios from "axios";
// import avatar from "./avatar.png";
import { useNavigate } from "react-router-dom";

const User = () => {
  const { setToken, admin, setUserName } = useContext(FileNameContext);
  const [data, setData] = useState(null);
  const tokenStorage = localStorage.getItem("user");
  const adminStorage = localStorage.getItem("admin");
  const navigate = useNavigate();
  useEffect(() => {
    axios
      .get("http://localhost:3005/api/userdata", {
        headers: {
          "x-token": tokenStorage,
        },
      })
      .then((res) => {
        setData(res.data);
        console.log("admin", admin);
        console.log("name", res.data.existingUser.name);
        setUserName(res.data.existingUser.name);
        setToken(tokenStorage);
      })
      .catch((err) => console.log(err));
  }, []);

  if (!tokenStorage) {
    navigate("/");
  }
  return (
    <div>
      {data && (
        <center>
          <br />
          <div
            class="card"
            style={{ width: "18rem", height: "6rem", marginLeft: "40rem" }}
          >
            <div class="card-body" style={{ backgroundColor: "white" }}>
              <h5 class="card-title">Welcome : {data.name}</h5>
              <h5>Id :{data.identification}</h5>
              <h5>isAdmin : {adminStorage}</h5>

              <h1></h1>
            </div>
          </div>
        </center>
      )}
    </div>
  );
};

export default User;
