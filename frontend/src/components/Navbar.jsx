import React, { useState } from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleMenu = () => {
    setIsOpen(!isOpen);
  };

  const toggleMenu2 = () => {
    if (isOpen) {
        setIsOpen(!isOpen)
    }
  }

  return (
    <div className="flex w-full justify-between px-10 py-4 border-b z-10">
        <Link to="/" className="text-white text-xl" onClick={toggleMenu2}>Mevrora</Link>

        <div className="">
            <button onClick={toggleMenu} className="text-white focus:outline-none">
                <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        strokeWidth="2"
                        d="M4 6h16M4 12h16m-7 6h7"
                    />
                </svg>
            </button>
        </div>

        <div className={`${isOpen ? "block" : "hidden"} absolute right-4 top-12 py-2 px-4 bg-blue-500 rounded-md shadow-lg gap-6`}>
            <Link to="/stats" className="text-white hover:text-gray-200 block md:inline-block" onClick={toggleMenu}>My Stats</Link>
            <Link to="/tiers" className="text-white hover:text-gray-200 block md:inline-block" onClick={toggleMenu}>Tiers</Link>
        </div>
    </div>
  );
};

export default Navbar;