import React from "react";
import ReactDOM from "react-dom";

import "./styles.css";

function App() {
  return (
    <div className="App">
      <div>
        <h1>Adam Skye Jones</h1>
        <p>
          Feet on the ground...
          <br />
          Head in the cloud.
        </p>
      </div>
    </div>
  );
}

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
