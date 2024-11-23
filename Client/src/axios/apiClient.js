import axios from 'axios';

const apiClient = axios.create({
    baseURL: import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000/api/',
});

let accessToken = null;

export const setAccessToken = token => {
    accessToken = token;
};

apiClient.interceptors.request.use(config => {
    if (accessToken) {
        config.headers.Authorization = `Bearer ${accessToken}`;
    }
    return config;
});

export default apiClient;