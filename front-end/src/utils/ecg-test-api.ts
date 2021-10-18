import api from './api'

export default class EcgTestApi {
  private baseRoute = import.meta.env.VITE_ECG_TEST_API_ROUTE as string

  constructor() {
    console.log('This is EcgTestApi constructor.')
    if (this.baseRoute == undefined) {
      throw new Error('No base route provided for EcgTestApi. Check .env.')
    }
  }

  async getEcgTests(): Promise<EcgTests> {
    try {
      const res = await api.get(this.baseRoute)
      // TODO: Do some transformation on the response to create EcgTest.Meta[]
      const ecgTests = res.data
      return Promise.resolve(ecgTests)
    } catch {
      return Promise.resolve([])
    }
  }
}
