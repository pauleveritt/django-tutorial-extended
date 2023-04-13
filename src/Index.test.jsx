import React from "react";

import { expect, test } from "vitest";
import { render, screen } from "@testing-library/react";
import { Index } from "./Index.jsx";

test("load the polls on home page", async () => {
  render(<Index />);
  expect(screen.getByRole("link", { name: "Vite Logo" })).to.exist;
});
