import React from "react";

export function Index() {
  return (
    <div className="grid gap-4 grid-cols-4 mx-2 mt-2">
      <div>
        <a href="https://vitejs.dev" target="_blank">
          Vite Logo
        </a>
        <a href="https://reactjs.org" target="_blank">
          React Logo
        </a>
      </div>
      <h1>Vite + React</h1>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </div>
  );
}
