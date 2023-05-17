import React from "react";
import cssSwitch from "../../css/switch/Switch.module.css";

const Switch = ({ isToggled, onToggle }) => {
  return (
    <label className={cssSwitch.switch}>
      <input type="checkbox" checked={isToggled} onChange={onToggle} />
      <span className={cssSwitch.slider} />
    </label>
  );
};

export default Switch;
