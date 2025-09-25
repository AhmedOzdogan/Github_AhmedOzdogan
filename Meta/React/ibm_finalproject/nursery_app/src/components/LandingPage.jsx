import { Link } from "react-router-dom";

function LandingPage() {
  return (
    <div className="flex flex-col items-center justify-start min-h-screen bg-gray-100 backdrop-blur-sm">
      <h1 className=" background-img text-8xl font-bold text-black mb-8 w-screen text-center items-center justify-center flex">
        Nursery App
      </h1>
      <p className="text-lg text-black mb-8 text-center max-w-xl">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor
        sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt
        ut labore et dolore magna aliqua.
      </p>
      <Link
        to="/products"
        className="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600 inline-block"
      >
        Get Started
      </Link>
    </div>
  );
}
export default LandingPage;
