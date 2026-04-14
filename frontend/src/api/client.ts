import axios, { AxiosError, AxiosInstance } from "axios";

const api: AxiosInstance = axios.create({
  baseURL: process.env.REACT_APP_API_URL || "http://localhost:5000",
  headers: {
    "Content-Type": "application/json",
  },
});

// Add token to requests if available
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("auth_token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Handle response errors
api.interceptors.response.use(
  (response) => response,
  (error: AxiosError) => {
    if (error.response?.status === 401) {
      localStorage.removeItem("auth_token");
      window.location.href = "/login";
    }
    return Promise.reject(error);
  }
);

// Services
export const authService = {
  login: (username: string, password: string) =>
    api.post("/login", { username, password }),
  register: (username: string, password: string) =>
    api.post("/register", { username, password }),
  logout: () => api.post("/logout"),
};

export const viajeService = {
  getAll: () => api.get("/viajes"),
  getById: (id: number) => api.get(`/viaje/${id}`),
  search: (query: string) => api.get(`/viajes/search?q=${query}`),
};

export const reservaService = {
  getAll: () => api.get("/reservas"),
  create: (viaje_id: number, data: Record<string, any>) =>
    api.post(`/reservas/nueva/${viaje_id}`, data),
  getByViaje: (viaje_id: number) => api.get(`/reservas/viaje/${viaje_id}`),
  cancel: (id: number) => api.delete(`/reservas/${id}`),
};

export default api;
