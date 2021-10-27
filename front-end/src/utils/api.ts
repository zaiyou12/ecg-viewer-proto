import axios, { AxiosInstance, AxiosRequestConfig, AxiosResponse } from 'axios'


const cancelSource = axios.CancelToken.source()

const apiConfig: AxiosRequestConfig = {
  baseURL: import.meta.env.VITE_API_BASE_URL as string,
  timeout: 5000,
  withCredentials: false
}

const api: AxiosInstance = axios.create(apiConfig)

const requestInterceptor = api.interceptors.request.use(
  (config: AxiosRequestConfig) => {
    // TODO: Add things that need to be done before request
    // config.headers['Content-Type'] = 'application/x-www-form-urlencoded';
    console.log(`Sending request of`);
    console.log(config);
    return config;
  }, (error: any) => {
    console.log('Sending request failed with');
    console.log(error);
    return Promise.reject(error);
  }
);

const responseInterceptor = api.interceptors.response.use(
  (response: AxiosResponse) => {
    console.log(`The server responded correctly with`);
    console.log(response);
    return response;
  }, (error: any) => {
    console.log('Request did not return status 200...');
    console.log(error);
    return Promise.reject(error);
  }
);

// TODO: Maybe add method for eject
// api.interceptors.request.eject(requestInterceptor);
// api.interceptors.response.eject(responseInterceptor);

export default api