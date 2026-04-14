export default function About() {
  return (
    <div className="container-section">
      <h1 className="heading-1">Sobre Nosotros</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div>
          <p className="text-lg text-gray-700 mb-4">
            Somos una agencia de viajes con más de 20 años de experiencia, dedicados a crear experiencias inolvidables para nuestros clientes.
          </p>
          <p className="text-lg text-gray-700">
            Nos especializamos en viajes personalizados a los destinos más hermosos de Colombia y el mundo.
          </p>
        </div>
        <div className="text-6xl text-center">✈️</div>
      </div>
    </div>
  );
}
