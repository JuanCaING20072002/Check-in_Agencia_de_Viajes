import { Link } from "react-router-dom";

export default function Home() {
  return (
    <>
      {/* Hero Section */}
      <section className="bg-gradient-to-br from-primary to-blue-900 text-white py-32">
        <div className="container-section text-center">
          <h1 className="text-5xl md:text-6xl font-bold mb-6">
            Explora el Mundo con Nosotros
          </h1>
          <p className="text-xl md:text-2xl mb-8 text-blue-100">
            Descubre increíbles destinos y crea recuerdos inolvidables
          </p>
          <div className="flex flex-col md:flex-row gap-4 justify-center">
            <Link
              to="/viajes"
              className="btn-primary px-8 py-4 text-lg inline-block"
            >
              Ver Viajes
            </Link>
            <Link
              to="/nosotros"
              className="btn-outline px-8 py-4 text-lg inline-block"
            >
              Conócenos
            </Link>
          </div>
        </div>
      </section>

      {/* Featured Destinations */}
      <section className="container-section">
        <h2 className="heading-2 text-center mb-12">Destinos Destacados</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {[
            {
              name: "Cartagena",
              description: "Hermosa ciudad colonial en el Caribe",
              image: "🏝️",
            },
            {
              name: "Bogotá",
              description: "Capital cosmopolita a 2600 metros de altura",
              image: "🏙️",
            },
            {
              name: "Santa Marta",
              description: "Puerta de entrada a la Sierra Nevada",
              image: "⛰️",
            },
          ].map((destination) => (
            <div key={destination.name} className="card p-6">
              <div className="text-6xl mb-4">{destination.image}</div>
              <h3 className="heading-3">{destination.name}</h3>
              <p className="text-gray-600 mb-4">{destination.description}</p>
              <Link
                to="/viajes"
                className="text-secondary font-medium hover:text-orange-600 transition inline-flex items-center"
              >
                Explorar →
              </Link>
            </div>
          ))}
        </div>
      </section>

      {/* Why Choose Us */}
      <section className="bg-gray-50 container-section">
        <h2 className="heading-2 text-center mb-12">¿Por qué elegirnos?</h2>
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          {[
            { icon: "✓", title: "Precios Competitivos", desc: "Las mejores ofertas del mercado" },
            { icon: "★", title: "Experiencias VIP", desc: "Servicios premium y personalizados" },
            { icon: "🛡️", title: "Garantía Total", desc: "Cobertura completa de tus viajes" },
            { icon: "24/7", title: "Soporte 24/7", desc: "Atención al cliente siempre disponible" },
          ].map((feature) => (
            <div key={feature.title} className="text-center">
              <div className="text-4xl mb-4">{feature.icon}</div>
              <h3 className="font-bold text-lg mb-2">{feature.title}</h3>
              <p className="text-gray-600">{feature.desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* Call to Action */}
      <section className="bg-secondary text-white container-section text-center">
        <h2 className="heading-2 text-white mb-4">¿Listo para tu próxima aventura?</h2>
        <p className="text-lg mb-8">Regístrate ahora y obtén 10% de descuento</p>
        <Link
          to="/register"
          className="bg-primary hover:bg-blue-800 px-8 py-3 rounded-lg font-bold inline-block transition"
        >
          Registrarse Ahora
        </Link>
      </section>
    </>
  );
}
