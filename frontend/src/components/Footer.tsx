import { Link } from "react-router-dom";

export default function Footer() {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="bg-gray-900 text-white mt-16">
      <div className="container-section">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
          {/* About */}
          <div>
            <h3 className="font-bold text-lg mb-4">Check-in Viajes</h3>
            <p className="text-gray-400 text-sm">
              Tu agencia de viajes confiable para explorar el mundo. Ofertas especiales en paquetes vacacionales.
            </p>
          </div>

          {/* Quick Links */}
          <div>
            <h4 className="font-bold mb-4">Enlaces Rápidos</h4>
            <ul className="space-y-2 text-gray-400 text-sm">
              <li>
                <Link to="/" className="hover:text-secondary transition">
                  Inicio
                </Link>
              </li>
              <li>
                <Link to="/viajes" className="hover:text-secondary transition">
                  Viajes
                </Link>
              </li>
              <li>
                <Link to="/nosotros" className="hover:text-secondary transition">
                  Nosotros
                </Link>
              </li>
            </ul>
          </div>

          {/* Services */}
          <div>
            <h4 className="font-bold mb-4">Servicios</h4>
            <ul className="space-y-2 text-gray-400 text-sm">
              <li>
                <a href="#" className="hover:text-secondary transition">
                  Reservaciones
                </a>
              </li>
              <li>
                <a href="#" className="hover:text-secondary transition">
                  Asesoría
                </a>
              </li>
              <li>
                <a href="#" className="hover:text-secondary transition">
                  Seguros
                </a>
              </li>
            </ul>
          </div>

          {/* Contact */}
          <div>
            <h4 className="font-bold mb-4">Contacto</h4>
            <ul className="space-y-2 text-gray-400 text-sm">
              <li>
                <a
                  href="mailto:info@checkin.com"
                  className="hover:text-secondary transition"
                >
                  info@checkin.com
                </a>
              </li>
              <li>
                <a
                  href="tel:+15551234567"
                  className="hover:text-secondary transition"
                >
                  +1 (555) 123-4567
                </a>
              </li>
              <li className="text-gray-500">Medellín, Colombia</li>
            </ul>
          </div>
        </div>

        {/* Divider */}
        <div className="border-t border-gray-800 pt-8">
          <div className="flex flex-col md:flex-row justify-between items-center text-gray-400 text-sm">
            <p>
              &copy; {currentYear} Check-in Agencia de Viajes. Todos los derechos
              reservados.
            </p>
            <div className="flex space-x-6 mt-4 md:mt-0">
              <a href="#" className="hover:text-secondary transition">
                Privacidad
              </a>
              <a href="#" className="hover:text-secondary transition">
                Términos
              </a>
              <a href="#" className="hover:text-secondary transition">
                Cookies
              </a>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
}
