import axios, { AxiosInstance, AxiosRequestConfig, AxiosResponse } from 'axios'
import qs from 'qs'
import { camelizeKeys, decamelizeKeys } from 'humps'

const cancelSource = axios.CancelToken.source()

const apiConfig: AxiosRequestConfig = {
  baseURL: import.meta.env.VITE_API_BASE_URL as string,
  timeout: 5000,
  headers: { 'Content-Type': 'application/json' },
  withCredentials: false,
  // TODO: encode: false
  paramsSerializer: (params) => qs.stringify(params, { arrayFormat: 'repeat' })
}

const api: AxiosInstance = axios.create(apiConfig)

const requestInterceptor = api.interceptors.request.use(
  (config: AxiosRequestConfig) => {
    console.log(
      `Sending request of ${config.method!.toUpperCase()}${config.url}`
    )
    config.data = decamelizeKeys(config.data)
    console.log(config)
    return config
  },
  (error: any) => {
    console.log('Sending request failed with')
    console.log(error)
    return Promise.reject(error)
  }
)

const responseInterceptor = api.interceptors.response.use(
  (response: AxiosResponse) => {
    console.log(
      `The server responded normally with \
${response.config.method!.toUpperCase()} \
${response.config.url}`
    )
    console.log(response)
    return Promise.resolve(camelizeKeys(response.data))
  },
  (error: any) => {
    console.log('Request did not return status 200...')
    console.log(error)
    return Promise.reject(error)
  }
)

// TODO: Maybe add method for eject
// api.interceptors.request.eject(requestInterceptor);
// api.interceptors.response.eject(responseInterceptor);

export default api
