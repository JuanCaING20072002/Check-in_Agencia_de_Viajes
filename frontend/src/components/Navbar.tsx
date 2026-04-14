import { Link } from "react-router-dom";
import { useState } from "react";

export default function Navbar() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <nav className="sticky top-0 z-50 bg-primary text-white shadow-lg">
      <div className="max-w-6xl mx-auto px-4">
        <div className="flex justify-between items-center h-16">
          {/* Logo */}
          <Link to="/" className="flex items-center space-x-2">
            <div className="w-8 h-8 bg-secondary rounded-lg flex items-center justify-center font-bold">
              ✈️
            </div>
            <span className="font-bold text-lg hidden sm:inline">
              Check-in Viajes
            </span>
          </Link>

          {/* Desktop Menu */}
          <div className="hidden md:flex space-x-6">
            <Link to="/" className="hover:text-secondary transition">
              Inicio
            </Link>
            <Link to="/nosotros" className="hover:text-secondary transition">
              Nosotros
            </Link>
            <Link to="/viajes" className="hover:text-secondary transition">
              Viajes
            </Link>
            <Link to="/login" className="hover:text-secondary transition">
              Acceder
            </Link>
            <Link
              to="/register"
              className="bg-secondary text-primary px-4 py-2 rounded-lg hover:bg-orange-600 transition font-medium"
            >
              Registrarse
            </Link>
          </div>

          {/* Mobile Menu Button */}
          <button
            className="md:hidden"
            onClick={() => setIsOpen(!isOpen)}
            aria-label="Toggle menu"
          >
            <svg
              className="w-6 h-6"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M4 6h16M4 12h16M4 18h16"
              />
            </svg>
          </button>
        </div>

        {/* Mobile Menu */}
        {isOpen && (
          <div className="md:hidden pb-4 space-y-2">
            <Link
              to="/"
              className="block hover:text-secondary transition py-2"
              onClick={() => setIsOpen(false)}
            >
              Inicio
            </Link>
            <Link
              to="/nosotros"
              className="block hover:text-secondary transition py-2"
              onClick={() => setIsOpen(false)}
            >
              Nosotros
            </Link>
            <Link
              to="/viajes"
              className="block hover:text-secondary transition py-2"
              onClick={() => setIsOpen(false)}
            >
              Viajes
            </Link>
            <Link
              to="/login"
              className="block hover:text-secondary transition py-2"
              onClick={() => setIsOpen(false)}
            >
              Acceder
            </Link>
            <Link
              to="/register"
              className="block bg-secondary text-primary px-4 py-2 rounded-lg hover:bg-orange-600 transition font-medium"
              onClick={() => setIsOpen(false)}
            >
              Registrarse
            </Link>
          </div>
        )}
      </div>
    </nav>
  );
}
