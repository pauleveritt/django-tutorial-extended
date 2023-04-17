import { Footer } from "./Footer.jsx";
import { Index } from "./Index.jsx";
import { Navbar } from "./Navbar.jsx";

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
