import React, { useEffect, useState } from "react";

export function Index() {
  const URL = "http://localhost:8000/v1/question/";
  let [questions, setQuestions] = useState(null);

  useEffect(() => {
    fetch(URL)
      .then((response) => response.json())
      .then((data) => {
        setQuestions(data.message);
      });
  }, []);

  return (
    <div className="grid gap-4 grid-cols-4 mx-2 mt-2">
      <h1>Questions</h1>
      <p>
        {questions &&
          questions.map((question) => (
            <ul>
              <a key={question.id} href={`${URL}/${question.id}`}>
                <li>{question.question_text}</li>
              </a>
            </ul>
          ))}
      </p>
    </div>
  );
}
