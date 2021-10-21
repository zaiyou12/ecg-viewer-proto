import api from './api'

export default class EcgTestApi {
  private baseRoute = import.meta.env.VITE_ECG_TEST_API_ROUTE as string

  constructor() {
    console.log('This is the EcgTestApi constructor.')
    if (this.baseRoute == undefined) {
      throw new Error('No base route provided for EcgTestApi. Check .env.')
    }
  }

  async getEcgTests(params: Req.EcgTestQuery) {
    try {
      const res = (await api.get(this.baseRoute, {
        params
      })) as Resp.EcgTestResp
      const obj = {
        tests: this.deserializeAllTest(res.tests),
        page: res.page,
        totalPages: res.total_page
        // TODO: testGroup: res.test_group
      }
      return obj
    } catch {
      return undefined
    }
  }

  // TODO: Remove some types
  private deserializeTest(resp: Resp.EcgTest): EcgTest.Meta {
    return {
      testId: resp.test_id,
      duration: resp.duration,
      region: resp.region,
      tGroup: [],
      condition: { final: resp.condition }
    }
  }

  private deserializeAllTest(resps: Resp.EcgTest[]): EcgTests {
    return resps.map((r) => this.deserializeTest(r))
  }
}
