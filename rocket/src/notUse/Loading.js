import React from "react";
import "../../css/Loading/Loading.css";

const Loading = () => {
  // return (
  //   <div class="pl">
  //     <div class="pl__dot"></div>
  //     <div class="pl__dot"></div>
  //     <div class="pl__dot"></div>
  //     <div class="pl__dot"></div>
  //     <div class="pl__dot"></div>
  //     <div class="pl__dot"></div>
  //     <div class="pl__dot"></div>
  //     <div class="pl__dot"></div>
  //     <div class="pl__dot"></div>
  //     <div class="pl__dot"></div>
  //     <div class="pl__dot"></div>
  //     <div class="pl__dot"></div>
  //     <div class="pl__text">Loading…</div>
  //   </div>
  // );

  return (
    <div class="container">
      <div class="loader3">
        <div class="circle1"></div>
        <div class="circle1"></div>
        <div class="circle1"></div>
        <div class="circle1"></div>
        <div class="circle1"></div>
      </div>
    </div>
  );
};

export default Loading;
