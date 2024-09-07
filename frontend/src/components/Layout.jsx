import { Link, Outlet } from "react-router-dom";
import Navbar from "./Navbar";

export default function Layout() {
    return(
        <div className="flex flex-col min-h-screen mb-10 font-[Ubuntu] text-white">
            <header className="flex justify-between gap-10 mb-10">
                <Navbar />
            </header>

            <Outlet />
            
            {/* <footer className="self-center sticky bot-0">by Mevrora 2024</footer> */}
        </div>
    )
}