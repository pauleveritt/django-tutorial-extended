import React, { useEffect, useState } from "react";

export function Index() {
  let [questions, setQuestions] = useState(null);

  useEffect(() => {
    fetch("https://dog.ceo/api/breeds/image/random/3")
      .then((response) => response.json())
      .then((data) => setQuestions(data.message));
  }, []);

  return (
    <div className="grid gap-4 grid-cols-4 mx-2 mt-2">
      <h1>Questions</h1>
      <p>
        {questions &&
          questions.map((dog) => (
            <div>
              <a href={dog} key={dog} aria-label="Question">
                <img alt="Dog" width={"200px"} height={"200px"} src={dog}></img>
              </a>
            </div>
          ))}
      </p>
    </div>
  );
}
