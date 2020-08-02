export const API_BASE_URL = process.env.API_BASE_URL ?
  process.env.API_BASE_URL :
  'http://127.0.0.1:8000';

export const LOGIN_REDIRECT = '/';
export const LOGIN_ERROR_REDIRECT = '/?error';
