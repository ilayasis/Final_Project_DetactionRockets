import React, { useContext } from "react";
import { FileNameContext } from "../../App";
import { Outlet, Navigate } from "react-router-dom";

const PrivateRoutes = () => {
  const { token } = useContext(FileNameContext);

  return token ? <Outlet /> : <Navigate to="/" />;
};

export default PrivateRoutes;
