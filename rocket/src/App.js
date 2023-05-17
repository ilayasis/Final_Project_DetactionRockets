import "./App.css";
import React, { createContext, useState } from "react";
import SideMenu from "./components/sidebar/SideMenu";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Videos from "./components/LaunchSections/Videos";
import Investigation from "./components/InvestigationScreen/Investigation";
import Login from "./components/Authentication/Login";
import AddUser from "./components/Authentication/AddUser";
import User from "./components/Authentication/User";
import SettingsApp from "./components/Settings/SettingsApp";
import PrivateRoutes from "./components/privateRoutes/PrivateRoutes";
import LiveStream from "./components/LiveStream/LiveStream";
import NotFoundPage from "./components/NotFoundPage/NotFound";
export const FileNameContext = React.createContext({});
export const store = createContext();
// import VideoSream from "./components/LiveStream/VideoStream";

function App() {
  const [token, setToken] = useState(null);
  const [admin, setAdmin] = useState(false);
  const [videoData, setVideoData] = useState("");
  const [username, setUserName] = useState("");
  const [isActive, setIsActive] = useState(false);

  return (
    <FileNameContext.Provider
      value={{
        username,
        setUserName,
        admin,
        setAdmin,
        token,
        setToken,
        videoData,
        setVideoData,
        isActive,
        setIsActive,
      }}
    >
      <BrowserRouter>
        <SideMenu />
        <Routes>
          <Route path="*" element={<NotFoundPage />} />
          <Route path="/" element={<Login />} />
          <Route element={<PrivateRoutes />}>
            <Route element={<SettingsApp />} path="/settings" exact />
            <Route element={<LiveStream />} path="/live" exact />
            <Route element={<Videos />} path="/investigation" />
            <Route element={<Investigation />} path="/InvestigationVideo" />
            <Route element={<AddUser />} path="/adduser" />
            <Route element={<User />} path="/user" />
          </Route>
        </Routes>
      </BrowserRouter>
    </FileNameContext.Provider>
  );
}
export default App;

{
  /* <Route element={<VideoSream />} path="/live" exact /> */
}
