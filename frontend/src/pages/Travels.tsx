import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { viajeService } from "@/api/client";

interface Viaje {
  id: number;
  nombre: string;
  descripcion: string;
  fecha: string;
  precio: number;
}

export default function Travels() {
  const [viajes, setViajes] = useState<Viaje[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    viajeService
      .getAll()
      .then((res) => setViajes(res.data))
      .catch((err) => console.error("Error fetching viajes:", err))
      .finally(() => setLoading(false));
  }, []);

  if (loading) {
    return (
      <div className="container-section text-center">
        <p className="text-xl">Cargando viajes...</p>
      </div>
    );
  }

  return (
    <div className="container-section">
      <h1 className="heading-1 mb-12">Nuestros Viajes</h1>

      {viajes.length === 0 ? (
        <p className="text-center text-gray-600 text-lg">
          No hay viajes disponibles en este momento.
        </p>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {viajes.map((viaje) => (
            <div key={viaje.id} className="card p-6">
              <h2 className="heading-3">{viaje.nombre}</h2>
              <p className="text-gray-600 mb-4">{viaje.descripcion}</p>
              <div className="flex justify-between items-center mb-4">
                <span className="text-secondary font-bold text-xl">
                  ${viaje.precio}
                </span>
                <span className="text-gray-500">{viaje.fecha}</span>
              </div>
              <Link
                to={`/viaje/${viaje.id}`}
                className="btn-secondary w-full text-center block"
              >
                Ver Detalles
              </Link>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
