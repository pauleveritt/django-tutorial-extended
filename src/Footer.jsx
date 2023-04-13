export function Footer() {
  return (
    <footer className="footer mt-500 p-10 bg-neutral text-neutral-content">
      <div>
        <span className="footer-title">Products</span>
        <a className="link link-hover">IDEs</a>
        <a className="link link-hover">.NET & Visual Studio</a>
        <a className="link link-hover">Team Tools</a>
        <a className="link link-hover">Plugins</a>
      </div>
      <div>
        <span className="footer-title">Solutions</span>
        <a className="link link-hover">C++ Tools</a>
        <a className="link link-hover">Data Tools</a>
        <a className="link link-hover">DevOps</a>
        <a className="link link-hover">Education</a>
      </div>
      <div>
        <span className="footer-title">Initiatives</span>
        <a className="link link-hover">Kotlin</a>
        <a className="link link-hover">JetBrains Mono</a>
        <a className="link link-hover">JetBrains Research</a>
      </div>
    </footer>
  );
}
