import React, { useState, useEffect, useContext } from "react";
import css from "../../css/Videos/Videos.module.css";
import { useNavigate } from "react-router-dom";
import { FileNameContext } from "../../App";
import RocketLoading from "./RocketLoading";
import LaunchData from "./launchData";
// export const FileNameContext = React.createContext("");

const Videos = () => {
  const [files, setFiles] = useState([]);
  const [page, setPage] = useState(1);
  const [isLoading, setIsLoading] = useState(false);
  const [activeFile, setActiveFile] = useState(null);

  // const [filenameVideo, setFilenameVideo] = useState("");
  // const [fileName, setFileName] = useState("");
  const { setVideoData, videoData } = useContext(FileNameContext);
  const pageSize = 3;
  const urlFiles = "http://localhost:3005/get_files";
  const navigate = useNavigate();
  const flag = false;
  //
  const handleFetchData = async () => {
    setIsLoading(true);

    try {
      const response = await fetch(urlFiles);

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      console.log(data);
      setFiles(data);
    } catch (error) {
      console.error(error);
    }

    setIsLoading(false);
  };
  useEffect(() => {
    handleFetchData();
  }, []);

  const handleFileEnter = async (filename) => {
    console.log("click", filename);
    try {
      const response = await fetch(
        `http://localhost:3005/load_video?filename=${filename}`
      );
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json();
      setActiveFile(data);
    } catch (error) {
      console.error(error);
      // handle error here
    }
  };

  useEffect(() => {
    if (videoData != "") {
      console.log("first");
      console.log("useEffect", videoData);
    }
  }, [videoData]);

  const handlePageClick = (newPage) => {
    setPage(newPage);
  };
  function getLaunchName(fullFileName) {
    const parts = fullFileName.split("_"); // split the filename at the underscore character
    console.log("parts", parts);
    const lastPart = parts[parts.length - 1]; // get the last part of the filename
    console.log("lastPart", lastPart);
    const launch = lastPart.replace(".mp4", "");
    const newName = launch
      .replace(/([a-z])([A-Z])/g, "$1 $2")
      .replace(/(\d+)/g, "$1 ");
    return newName;
  }
  const numPages = Math.ceil(files.length / pageSize);

  // const handleFileEnter = (filename) => {
  //   // Set active file state to the selected file
  //   setActiveFile(filename);
  // };

  const resetActiveFile = () => {
    // Reset active file state to null
    setActiveFile(null);
  };

  return (
    <div>
      {activeFile ? (
        <div>
          {/* <button onClick={resetActiveFile}>Back to all files</button> */}
          <LaunchData
            activeFile={activeFile}
            resetActiveFile={resetActiveFile}
          />
        </div>
      ) : (
        // Render the list of files here
        <button onClick={handleFetchData}>
          {isLoading ? (
            <RocketLoading />
          ) : (
            <div className={css.cardContainer}>
              <div className="h1Container">
                <h1 className="h1">Missile launch sections</h1>
              </div>

              <div className={css.files}>
                {files
                  .slice((page - 1) * pageSize, page * pageSize)
                  .map((file) => (
                    <div className={css.fileItem} key={file.filename}>
                      <img
                        src={`data:Image/jpeg;base64,${file.metadata.Image}`}
                        alt={file.filename}
                        className={css.card}
                      />
                      <p className={css.p}>{file.metadata.Date}</p>
                      <button
                        onClick={() => {
                          handleFileEnter(file.filename);
                        }}
                        className={css.name}
                      >
                        {getLaunchName(file.filename)}
                      </button>
                    </div>
                  ))}
              </div>

              {numPages >= 1 && (
                <div className={css.pagination}>
                  {Array.from({ length: numPages }, (_, i) => (
                    <button
                      key={i}
                      onClick={() => handlePageClick(i + 1)}
                      className={i + 1 === page ? "current" : ""}
                    >
                      {i + 1}
                    </button>
                  ))}
                </div>
              )}
            </div>
          )}
        </button>
      )}
    </div>
  );
};

export default Videos;

// import React, { useState, useEffect } from "react";
// import css from "../../css/Videos/Videos.module.css";

// const Videos = () => {
//   const [products, setProducts] = useState([]);

//   useEffect(() => {
//     async function fetchData() {
//       const response = await fetch("http://127.0.0.1:8000/get_files");
//       const data = await response.json();
//       setProducts(data);
//     }

//     fetchData();
//   }, []);
//   const handleClick = (filename) => {
//     // Add your code here to handle the click event
//   };
//   return (
//     <div className={css.products}>
//       {products.map((product) => (
//         <div className={css.productItem} key={product.filename}>
//           <img
//             src={`data:image/jpeg;base64,${product.metadata.image}`}
//             alt={product.filename}
//           />
//           <p>{product.filename}</p>
//           <button onClick={() => handleClick(product.filename)}>
//             Click me
//           </button>
//         </div>
//       ))}
//     </div>
//   );
// };

// export default Videos;

// import React, { useState, useEffect } from "react";
// import css from "../../css/Videos/Videos.module.css";

// const Videos = () => {
//   const [products, setProducts] = useState([]);
//   const [page, setPage] = useState(1);
//   const pageSize = 6;

//   useEffect(() => {
//     async function fetchData() {
//       const response = await fetch(
//         `http://127.0.0.1:8000/get_files?page=${page}&pageSize=${pageSize}`
//       );
//       const data = await response.json();
//       setProducts(data);
//     }

//     fetchData();
//   }, [page]);

//   const handleClick = (filename) => {
//     // Add your code here to handle the click event
//   };

//   const handlePageClick = (newPage) => {
//     setPage(newPage);
//   };

//   const numPages = Math.ceil(products.length / pageSize);

//   return (
//     <div>
//       <div className={css.products}>
//         {products
//           .slice((page - 1) * pageSize, page * pageSize)
//           .map((product) => (
//             <div className={css.productItem} key={product.filename}>
//               <img
//                 src={`data:image/jpeg;base64,${product.metadata.image}`}
//                 alt={product.filename}
//               />
//               <p>{product.filename}</p>
//               <button onClick={() => handleClick(product.filename)}>
//                 Click me
//               </button>
//             </div>
//           ))}
//       </div>
//       {numPages > 1 && (
//         <div className={css.pagination}>
//           {Array.from({ length: numPages }, (_, i) => (
//             <button
//               key={i}
//               onClick={() => handlePageClick(i + 1)}
//               className={i + 1 === page ? "current" : ""}
//             >
//               {i + 1}
//             </button>
//           ))}
//         </div>
//       )}
//     </div>
//   );
// };

// export default Videos;
