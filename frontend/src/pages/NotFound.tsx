import { Link } from "react-router-dom";

export default function NotFound() {
  return (
    <div className="container-section text-center py-32">
      <h1 className="text-6xl font-bold text-primary mb-4">404</h1>
      <p className="text-2xl text-gray-600 mb-8">Página no encontrada</p>
      <p className="text-lg text-gray-500 mb-12">
        Lo sentimos, la página que buscas no existe.
      </p>
      <Link to="/" className="btn-primary px-8 py-3 text-lg inline-block">
        Volver al Inicio
      </Link>
    </div>
  );
}
