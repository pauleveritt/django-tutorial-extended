// noinspection JSUnresolvedReference,JSCheckFunctionSignatures

import React from "react";

import { beforeEach, expect, test } from "vitest";
import { render, screen, waitFor } from "@testing-library/react";
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

function createFetchResponse(data) {
  return { json: () => new Promise((resolve) => resolve(data)) };
}

beforeEach(async () => {
  fetch.mockResolvedValue(createFetchResponse(questionListResponse));
  render(<Index />);
  await waitFor(() => screen.getByRole("link", { name: "Question" }));
});

test("load the polls on home page", async () => {
  // Find the questions
  const links = screen.getAllByRole("link");
  expect(links).to.have.length(3);
  expect(links[0].textContent).to.equal(questionListResponse[0].question_text);
});
