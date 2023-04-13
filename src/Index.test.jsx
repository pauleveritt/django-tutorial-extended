import React from "react";

import { expect, test } from "vitest";
import { render, screen } from "@testing-library/react";
import { Index } from "./Index.jsx";

global.fetch = vi.fn();

test("load the polls on home page", async () => {
  render(<Index />);

  // Ensure this renders by finding the h1
  expect(screen.getByText("Questions")).to.exist;

  // Find the questions
  const first = screen.getAllByRole("link", { name: "Question" });
  expect(first.href).to.equal(9);
});
