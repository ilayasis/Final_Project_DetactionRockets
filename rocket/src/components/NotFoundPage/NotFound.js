import React from "react";
import NotFoundPhoto from "../../assets/notFoundUrl/error.png";
import css from "../../css/NotFound/Not.module.css";
const NotFound = () => {
  return (
    <div>
      <div classNmae={css.containerNot} style={{ marginLeft: "455px" }}>
        <img
          style={{ width: "950px", marginTop: "120px", marginLeft: "-120px" }}
          src={NotFoundPhoto}
          alt="logo"
        />
      </div>
    </div>
  );
};

export default NotFound;
