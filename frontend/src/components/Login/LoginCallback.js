import React, {useEffect} from 'react';
import axios from 'axios';
import {API_BASE_URL, LOGIN_ERROR_REDIRECT, LOGIN_REDIRECT}
  from '../../constants';
import Cookies from 'js-cookie';

const LoginCallback = () => {
  useEffect(() => {
    const urlParams = new URLSearchParams(window.location.search);
    const qParams = [
      `code=${urlParams.get('code')}`,
      `scope=openid profile email`,
      `state=${urlParams.get('state')}`,
    ].join('&');
    // request access token from backend
    axios.get(`${API_BASE_URL}/oidc/callback/?${qParams}`,
        {withCredentials: true})
        .then((res) => {
          window.localStorage.setItem('access_token', res.data['access_token']);
          Cookies.remove('sessionid');
          window.location.assign(LOGIN_REDIRECT);
        })
        .catch(() => {
          window.location.assign(LOGIN_ERROR_REDIRECT);
        });
  }, []);

  return <p>Logging you in ...</p>;
};

export default LoginCallback;
