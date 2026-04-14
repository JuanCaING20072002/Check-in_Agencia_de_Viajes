export default function Dashboard() {
  return (
    <div className="container-section">
      <h1 className="heading-1 mb-8">Mi Panel de Control</h1>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-12">
        <div className="card p-6">
          <h3 className="heading-3">Mis Reservas</h3>
          <p className="text-2xl font-bold text-secondary">0</p>
          <p className="text-gray-600">viajes reservados</p>
        </div>

        <div className="card p-6">
          <h3 className="heading-3">Próximos Viajes</h3>
          <p className="text-2xl font-bold text-secondary">0</p>
          <p className="text-gray-600">viajes próximos</p>
        </div>

        <div className="card p-6">
          <h3 className="heading-3">Puntos de Fidelización</h3>
          <p className="text-2xl font-bold text-secondary">0</p>
          <p className="text-gray-600">puntos acumulados</p>
        </div>
      </div>

      <div className="card p-8">
        <h2 className="heading-2 mb-6">Mi Información</h2>
        <div className="space-y-4">
          <div>
            <label className="block text-sm font-medium mb-2">Email</label>
            <input
              type="email"
              disabled
              className="w-full px-4 py-2 bg-gray-50 border border-gray-300 rounded-lg"
            />
          </div>
          <div>
            <label className="block text-sm font-medium mb-2">Teléfono</label>
            <input
              type="tel"
              placeholder="Tu número de teléfono"
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent outline-none"
            />
          </div>
        </div>
      </div>
    </div>
  );
}
