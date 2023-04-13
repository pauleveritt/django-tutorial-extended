import { Navbar } from "./Navbar.jsx";
import { Footer } from "./Footer.jsx";
import { Index } from "./Index.jsx";

function App() {
  return (
    <>
      <Navbar />
      <div className="flex-grow">
        <Index />
      </div>
      <Footer />
    </>
  );
}

export default App;
