import React, { useEffect, useState } from "react";

export function Index() {
  const URL = "http://localhost:8000/v1/question/";
  let [questions, setQuestions] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch(URL)
        .then((response) => response.json())
        .then((data) => {
          setQuestions(data);
        });
    };
    // noinspection JSIgnoredPromiseFromCall
    fetchData();
  }, []);
  return (
    <div className="grid gap-4 grid-cols-4 mx-2 mt-2">
      <h1>Questions</h1>
      <ul>
        {questions &&
          questions.map((question) => (
            <li key={question.id}>
              <a href={`${URL}/${question.id}`} aria-label="Question">
                {question.question_text}
              </a>
            </li>
          ))}
      </ul>
    </div>
  );
}
