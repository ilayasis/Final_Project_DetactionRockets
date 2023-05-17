import React from "react";

const FileData = ({ activeFile, resetActiveFile }) => {
  if (!activeFile) {
    return null;
  }

  // Render file data here

  return (
    <div>
      <button onClick={resetActiveFile}>Back to all files</button>
    </div>
  );
};

export default FileData;
