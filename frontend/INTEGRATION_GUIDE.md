# Modernización del Frontend - Guía de Integración

## 📁 Estructura del Proyecto

```
Check-in_Agencia_de_Viajes/
├── backend/                     # Backend Flask (existente)
│   ├── app/
│   │   ├── models/             # Modelos SQLAlchemy
│   │   ├── routes/             # Blueprints con rutas
│   │   ├── services/           # Capa de servicios
│   │   ├── config/             # Configuración
│   │   ├── extensions.py       # Extensiones (db, migrate)
│   │   └── __init__.py         # Factory function
│   ├── tests/                  # Tests del backend
│   ├── main.py                 # Punto de entrada
│   └── requirements.txt        # Dependencias Python
│
└── frontend/                    # Frontend React + Tailwind (NUEVO)
    ├── src/
    │   ├── components/         # Componentes reutilizables
    │   ├── pages/             # Páginas principales
    │   ├── api/               # Cliente HTTP (Axios)
    │   ├── hooks/             # Custom React hooks
    │   ├── utils/             # Utilidades
    │   ├── styles/            # Estilos globales
    │   ├── App.tsx            # Componente raíz
    │   └── main.tsx           # Punto de entrada
    ├── index.html             # HTML principal
    ├── package.json           # Dependencias Node
    ├── vite.config.ts         # Configuración de Vite
    ├── tailwind.config.js     # Configuración de Tailwind
    ├── tsconfig.json          # Configuración TypeScript
    └── README.md              # Documentación del frontend
```

## 🚀 Cómo Ejecutar el Proyecto

### Backend (Flask)

```bash
# Instalar dependencias
pip install -r requirements.txt

# Crear archivo .env (opcional)
cp .env.example .env

# Ejecutar
python main.py
# O con gunicorn (production)
gunicorn -w 4 -b 0.0.0.0:5000 main:app
```

El backend estará disponible en: `http://localhost:5000`

### Frontend (React)

```bash
# Navegar a la carpeta del frontend
cd frontend

# Instalar dependencias
npm install

# Desarrollo (con HMR)
npm run dev

# Para producción
npm run build
```

El frontend estará disponible en: `http://localhost:5173` (desarrollo) o `http://localhost:5000/static/dist` (producción)

## 🔗 Integración Backend ↔ Frontend

### Comunicación HTTP

- **Backend**: API REST en `http://localhost:5000`
- **Frontend**: Cliente Axios en `src/api/client.ts`
- **CORS**: Debe estar habilitado en Flask

### Endpoints Disponibles

#### Autenticación
```
POST /login              - Iniciar sesión
POST /register           - Registrarse
POST /logout             - Cerrar sesión
```

#### Viajes
```
GET /viajes              - Obtener todos los viajes
GET /viaje/<id>          - Obtener detalle de viaje
GET /viajes/search?q=... - Buscar viajes
```

#### Reservas
```
GET /reservas            - Obtener todas las reservas
POST /reservas/nueva/<viaje_id> - Crear nueva reserva
GET /reservas/viaje/<id> - Obtener reservas de un viaje
DELETE /reservas/<id>    - Cancelar reserva
```

### Almacenamiento de Token

El token de autenticación se guarda en `localStorage` bajo la clave `auth_token`:

```javascript
// Almacenar token
localStorage.setItem("auth_token", token);

// Recuperar token
const token = localStorage.getItem("auth_token");

// Eliminar token
localStorage.removeItem("auth_token");
```

## 🎨 Estilos y Componentes

### Sistema de Colores

- **Principal**: `#003366` (azul oscuro)
- **Secundario**: `#FF9500` (naranja)
- **Accent**: `#00CC99` (verde agua)

### Componentes Disponibles

- `Navbar` - Navegación principal
- `Footer` - Pie de página
- `Button` (Primary, Secondary, Outline)
- `Card` - Contenedor genérico

### Utilidades Tailwind

```css
.btn-primary     /* Botón principal */
.btn-secondary   /* Botón secundario */
.btn-outline     /* Botón con borde */
.card            /* Contenedor con sombra */
.container-section /* Contenedor con max-width */
```

## 📦 Dependencias Principales

### Frontend
- React 18
- React Router 6
- Axios
- TypeScript
- Tailwind CSS
- Vite

### Backend
- Flask 3.0
- SQLAlchemy 3.0
- PostgreSQL 16 (Alpine)
- pytest (testing)

## 🔐 Seguridad

### Frontend
- CORS habilitado para localhost
- Token JWT en localStorage (desarrollo)
- HTTPS en producción (recomendado)

### Backend
- CORS configurado en `app/__init__.py`
- Password hashing con werkzeug
- Validación de datos en servicios
- Error handling robusto

## 🧪 Testing

```bash
# Backend
cd ..
python -m pytest tests/ -v

# Frontend (próximamente)
cd frontend
npm run test
```

## 📊 Coverage

- **Backend**: 62% (21+ tests)
- **Frontend**: Próximamente

## 🚀 Deployment

### Producción

1. **Build Frontend**
   ```bash
   cd frontend
   npm run build
   ```

2. **Backend con Gunicorn**
   ```bash
   gunicorn -w 4 -b 0.0.0.0:5000 main:app
   ```

3. **Nginx Reverse Proxy** (opcional)
   - Servir `/static` desde Frontend
   - Proxy de API a puerto 5000

## 📝 Próximos Pasos

1. ✅ Estructura React + Tailwind
2. ✅ Componentes básicos
3. ⏳ Integración completa de API
4. ⏳ Testing del frontend
5. ⏳ Autenticación persistent
6. ⏳ Estado global (Zustand)
7. ⏳ Error handling mejorado
8. ⏳ Tema oscuro/claro
9. ⏳ PWA (Progressive Web App)
10. ⏳ Analytics

## 🤝 Contribuir

Ver [CONTRIBUTING.md](../CONTRIBUTING.md) para detalles.

## 📄 Licencia

MIT
