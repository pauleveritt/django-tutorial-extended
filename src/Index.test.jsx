import React from "react";

import { beforeEach, expect, test } from "vitest";
import { render, screen } from "@testing-library/react";
import { Index } from "./Index.jsx";

// Setup fake response JSON
const questionListResponse = [
  {
    id: 1,
    question_text: "Do you prefer light or dark theme?",
    pub_date: "2023-04-14T13:29:06Z",
  },
  {
    id: 2,
    question_text: "Your current version of Python",
    pub_date: "2023-04-14T13:29:19Z",
  },
  {
    id: 3,
    question_text: "Your current version of Django",
    pub_date: "2023-04-14T13:29:32Z",
  },
];

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
function createFetchResponse(data) {
  return { json: () => new Promise((resolve) => resolve(data)) };
}

beforeEach(async () => {
  // noinspection JSUnresolvedReference
  fetch.mockResolvedValue(createFetchResponse(questionListResponse));
  render(<Index />);
  await sleep(500);
});

test("load the polls on home page", async () => {
  // Find the questions
  const links = screen.getAllByRole("link");
  expect(links).to.have.length(99);
  const first = links[0];
  expect(first.question_text).to.equal(questionListResponse[0].question_text);
});
