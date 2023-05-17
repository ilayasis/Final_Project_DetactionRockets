import css from "../../css/Authentication/Authentication.module.css";
import { useNavigate } from "react-router-dom";
import React, { useState } from "react";
import axios from "axios";
import "../../css/Authentication/AddUser.css";
const AddUser = () => {
  const Swal = require("sweetalert2");

  const history = useNavigate();

  const [inputs, setInputs] = useState({
    name: "",
    identification: "",
    password: "",
    isAdmin: false,
  });

  const Toast = Swal.mixin({
    toast: true,
    position: "top-end",
    showConfirmButton: false,
    timer: 3300,
    timerProgressBar: true,
    didOpen: (toast) => {
      toast.addEventListener("mouseenter", Swal.stopTimer);
      toast.addEventListener("mouseleave", Swal.resumeTimer);
    },
  });

  const handelChangeInputs = (e) => {
    setInputs((prev) => ({
      ...prev,
      [e.target.name]: e.target.value,
    }));
    console.log(e.target.name, "value : ", e.target.value);
  };

  let errorAddUser = false;
  const sendRequestToAddUser = async () => {
    const res = await axios
      .post("http://localhost:3005/api/adduser", {
        name: inputs.name,
        identification: inputs.identification,
        password: inputs.password,
        isAdmin: inputs.isAdmin,
      })
      .then((res) => {
        if (res.data.message === "Add User Successfully") {
          Toast.fire({
            icon: "success",
            title: inputs.isAdmin
              ? "Admin user added successfully"
              : "Operator user added successfully",
          });
          setInputs({
            name: "",
            identification: "",
            password: "",
            isAdmin: false,
          });
        }
      })
      .catch((err) => {
        errorAddUser = false;
        console.log(err);
        Toast.fire({
          icon: "error",
          title: `Request failed: ${err.response.data.message}`,
        });
      });
    const data = res ? await res.data : null;
    return data;
  };

  const handleSubmitButtonAddUser = (e) => {
    e.preventDefault();
    sendRequestToAddUser()
      .then(() => {
        if (errorAddUser) {
          history("/");
        }
      })
      .catch((err) => {
        errorAddUser = false;
        Toast.fire({
          icon: "error",
          title: `Request failed: Server Error`,
        });
      });
  };
  return (
    <div className="login-boxx">
      <p>Add User</p>
      <form>
        <div className="user-box">
          <input
            onChange={handelChangeInputs}
            value={inputs.name}
            required
            autoComplete="off"
            type="text"
            name="name"
          />
          <label>Name</label>
        </div>
        <div className="user-box">
          <input
            onChange={handelChangeInputs}
            value={inputs.identification}
            required
            name="identification"
          />
          <label>Id</label>
        </div>
        <div className="user-box">
          <input
            onChange={handelChangeInputs}
            value={inputs.password}
            required
            name="password"
            type="password"
          />
          <label>Password</label>
        </div>
        <div className={css.field}>
          <label htmlFor="isAdmin">Is Admin : </label>
          <select
            name="isAdmin"
            onChange={handelChangeInputs}
            value={inputs.isAdmin}
            className={css.selectField}
          >
            <option value={false}>No</option>
            <option value={true}>Yes</option>
          </select>
        </div>
        <a href="#" onClick={handleSubmitButtonAddUser}>
          <span></span>
          <span></span>
          <span></span>
          <span></span>
          Submit
        </a>
      </form>
    </div>
  );
};

export default AddUser;

// return (
//   <div>
//     <div className={css.container}>
//       <h1 className={css.text}>-------------</h1>
//     </div>
//     <form className={css.form} onSubmit={handleSubmit}>
//       <p className={css.heading} id="heading">
//         Add User
//       </p>
//       <div></div>
//       <div className={css.field}>
//         <svg
//           className={css.inputIcon}
//           xmlns="http://www.w3.org/2000/svg"
//           width="16"
//           height="16"
//           fill="currentColor"
//           viewBox="0 0 16 16"
//         >
//           <path d="M13.106 7.222c0-2.967-2.249-5.032-5.482-5.032-3.35 0-5.646 2.318-5.646 5.702 0 3.493 2.235 5.708 5.762 5.708.862 0 1.689-.123 2.304-.335v-.862c-.43.199-1.354.328-2.29.328-2.926 0-4.813-1.88-4.813-4.798 0-2.844 1.921-4.881 4.594-4.881 2.735 0 4.608 1.688 4.608 4.156 0 1.682-.554 2.769-1.416 2.769-.492 0-.772-.28-.772-.76V5.206H8.923v.834h-.11c-.266-.595-.881-.964-1.6-.964-1.4 0-2.378 1.162-2.378 2.823 0 1.737.957 2.906 2.379 2.906.8 0 1.415-.39 1.709-1.087h.11c.081.67.703 1.148 1.503 1.148 1.572 0 2.57-1.415 2.57-3.643zm-7.177.704c0-1.197.54-1.907 1.456-1.907.93 0 1.524.738 1.524 1.907S8.308 9.84 7.371 9.84c-.895 0-1.442-.725-1.442-1.914z"></path>
//         </svg>
//         <input
//           name="name"
//           onChange={handelChange}
//           value={inputs.name}
//           autoComplete="off"
//           placeholder="Name"
//           className={css.inputField}
//           type="text"
//         />
//       </div>
//       <div className={css.field}>
//         <svg
//           className={css.inputIcon}
//           xmlns="http://www.w3.org/2000/svg"
//           width="16"
//           height="16"
//           fill="currentColor"
//           viewBox="0 0 16 16"
//         >
//           <path d="M13.106 7.222c0-2.967-2.249-5.032-5.482-5.032-3.35 0-5.646 2.318-5.646 5.702 0 3.493 2.235 5.708 5.762 5.708.862 0 1.689-.123 2.304-.335v-.862c-.43.199-1.354.328-2.29.328-2.926 0-4.813-1.88-4.813-4.798 0-2.844 1.921-4.881 4.594-4.881 2.735 0 4.608 1.688 4.608 4.156 0 1.682-.554 2.769-1.416 2.769-.492 0-.772-.28-.772-.76V5.206H8.923v.834h-.11c-.266-.595-.881-.964-1.6-.964-1.4 0-2.378 1.162-2.378 2.823 0 1.737.957 2.906 2.379 2.906.8 0 1.415-.39 1.709-1.087h.11c.081.67.703 1.148 1.503 1.148 1.572 0 2.57-1.415 2.57-3.643zm-7.177.704c0-1.197.54-1.907 1.456-1.907.93 0 1.524.738 1.524 1.907S8.308 9.84 7.371 9.84c-.895 0-1.442-.725-1.442-1.914z"></path>
//         </svg>
//         <input
//           name="identification"
//           onChange={handelChange}
//           value={inputs.identification}
//           autoComplete="off"
//           placeholder="identification"
//           className={css.inputField}
//         />
//       </div>
//       <div className={css.field}>
//         <svg
//           className={css.inputIcon}
//           xmlns="http://www.w3.org/2000/svg"
//           width="16"
//           height="16"
//           fill="currentColor"
//           viewBox="0 0 16 16"
//         >
//           <path d="M8 1a2 2 0 0 1 2 2v4H6V3a2 2 0 0 1 2-2zm3 6V3a3 3 0 0 0-6 0v4a2 2 0 0 0-2 2v5a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2z"></path>
//         </svg>
//         <input
//           name="password"
//           onChange={handelChange}
//           value={inputs.password}
//           placeholder="Password"
//           className={css.inputField}
//           type="password"
//         />
//       </div>
//       <div className={css.field}>
//         <label htmlFor="isAdmin">Is Admin : </label>
//         <select
//           name="isAdmin"
//           onChange={handelChange}
//           value={inputs.isAdmin}
//           className={css.selectField}
//         >
//           <option value={false}>No</option>
//           <option value={true}>Yes</option>
//         </select>
//       </div>
//       <div className={css.btn}>
//         <button type="submit" className={css.button2}>
//           Add User
//         </button>
//       </div>
//     </form>
//   </div>
// );
