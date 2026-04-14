# Check-in Agencia de Viajes - Frontend

Modern React + Tailwind CSS frontend para la aplicación Check-in Agencia de Viajes.

## Características

- ✨ **React 18** - Framework UI moderno
- 🎨 **Tailwind CSS** - Utilidades CSS para un diseño responsive
- 🛣️ **React Router v6** - Enrutamiento moderno
- 📦 **Vite** - Bundler ultra-rápido
- 🔄 **Axios** - Cliente HTTP para comunicación con backend
- 📝 **TypeScript** - Tipado estático para JavaScript
- 🧹 **ESLint + Prettier** - Linting y formateo de código
- ♿ **Accesibilidad** - WCAG compliance

## Requisitos

- Node.js 16+ 
- npm o yarn

## Instalación

```bash
# Instalar dependencias
npm install

# Desarrollo
npm run dev

# Build para producción
npm run build

# Preview del build
npm run preview

# Linting
npm run lint

# Formateo de código
npm run format
```

## Estructura del Proyecto

```
frontend/
├── src/
│   ├── components/          # Componentes reutilizables (Navbar, Footer, etc)
│   ├── pages/              # Páginas principales
│   ├── api/                # Servicios de API
│   ├── hooks/              # Custom React hooks
│   ├── utils/              # Utilidades
│   ├── styles/             # Estilos globales
│   ├── App.tsx             # Componente principal
│   └── main.tsx            # Punto de entrada
├── index.html              # HTML principal
├── vite.config.ts          # Configuración de Vite
├── tailwind.config.js      # Configuración de Tailwind
├── postcss.config.js       # Configuración de PostCSS
├── tsconfig.json           # Configuración de TypeScript
└── package.json            # Dependencias y scripts
```

## Páginas Disponibles

- `/` - Inicio
- `/nosotros` - Sobre nosotros
- `/viajes` - Listado de viajes
- `/viaje/:id` - Detalle del viaje
- `/login` - Iniciar sesión
- `/register` - Registrarse
- `/dashboard` - Panel de usuario

## Integración con Backend

El frontend se comunica con el backend Flask mediante:

- **URL Base**: `http://localhost:5000` (desarrollo)
- **API Key**: Token en `localStorage` bajo la clave `auth_token`
- **CORS**: Habilitado en el servidor Flask

## Variables de Entorno

Crear archivo `.env.local`:

```env
VITE_API_URL=http://localhost:5000
VITE_app_NAME=Check-in Viajes
```

## Deployment

### Vite Build Output

El build se genera en `../static/dist` para integración con Flask. 

Para desplegar en producción:

```bash
npm run build
```

Esto genera archivos optimizados listos para production.

## Desarrollo

### Hot Module Replacement (HMR)

El desarrollo con Vite incluye HMR automático. Los cambios se reflejan instantáneamente.

### Proxy de API

En desarrollo, las requests a `/api/*` se redirigen automáticamente a `http://localhost:5000`.

## Performance

- 🚀 Code splitting automático
- 📦 Tree-shaking incluido
- 🗜️ Minificación automática
- 📱 Mobile-first responsive design

## Licencia

MIT
