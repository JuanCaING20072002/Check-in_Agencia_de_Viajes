import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import { viajeService } from "@/api/client";

export default function TravelDetail() {
  const { id } = useParams();
  const [viaje, setViaje] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (id) {
      viajeService
        .getById(parseInt(id))
        .then((res) => setViaje(res.data))
        .catch((err) => console.error("Error fetching viaje:", err))
        .finally(() => setLoading(false));
    }
  }, [id]);

  if (loading) {
    return <div className="container-section text-center"><p>Cargando...</p></div>;
  }

  if (!viaje) {
    return <div className="container-section text-center"><p>Viaje no encontrado</p></div>;
  }

  return (
    <div className="container-section">
      <h1 className="heading-1 mb-8">{viaje.nombre}</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div className="text-6xl">{viaje.imagen || "📸"}</div>
        <div>
          <p className="text-lg text-gray-700 mb-4">{viaje.descripcion}</p>
          <p className="text-2xl font-bold text-secondary mb-4">${viaje.precio}</p>
          <p className="text-gray-600 mb-6">Fecha: {viaje.fecha}</p>
          <button className="btn-primary px-8 py-3 text-lg">Reservar Ahora</button>
        </div>
      </div>
    </div>
  );
}
