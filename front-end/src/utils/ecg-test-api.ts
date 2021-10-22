import api from './api'
import { deserializeAllTest } from './deserializer'

export default class EcgTestApi {
  private baseRoute = import.meta.env.VITE_ECG_TEST_API_ROUTE as string

  constructor() {
    if (this.baseRoute == undefined) {
      throw new Error('No base route provided for EcgTestApi. Check .env.')
    }
  }

  async fetchTestList(params: Req.EcgTestQuery) {
    try {
      const res = (await api.get(this.baseRoute, {
        params
      })) as Resp.EcgTestResp
      const { tests, page, totalPage, testGroup } = res
      const obj = {
        tests: deserializeAllTest(tests),
        page,
        totalPage: totalPage === undefined || totalPage < 1 ? 1 : totalPage
        // TODO: testGroup
      }
      return obj
    } catch {
      return undefined
    }
  }
}
