import axios from 'axios';
import { API_BASE_URL } from './constants';

const instance = axios.create({
  baseURL: API_BASE_URL,
});

instance.defaults.headers.common['Authorization'] =
  `Bearer ${localStorage.getItem('access_token')}`;
// Allow django to see that we are a library
instance.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
instance.defaults.headers.common['Content-Type'] = 'application/json';
instance.defaults.withCredentials = true;
instance.defaults.xsrfCookieName = 'csrftoken';
instance.defaults.xsrfHeaderName = 'x-csrftoken';

instance.interceptors.response.use((response) => response,
    (error) => {
      const response = error.response;
      // if backend answers with refresh_url token is invalid so refresh it
      if (response.status === 403 &&
        response.data.hasOwnProperty('refresh_url')) {
        localStorage.removeItem('access_token');
        document.location.href = response.data['refresh_url'];
      }
      return Promise.reject(error);
    });

export default instance;
