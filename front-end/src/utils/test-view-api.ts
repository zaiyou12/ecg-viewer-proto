import api from './api'
import { deserializeTest, deserializeToGroups } from './deserializer'

export default class TestViewApi {
  private ecgRoute = import.meta.env.VITE_ECG_TEST_API_ROUTE as string
  private groupRoute = import.meta.env.VITE_GROUP_API_ROUTE as string

  constructor() {
    if (this.ecgRoute == undefined || this.groupRoute == undefined) {
      throw new Error('No base route provided for TestViewApi. Check .env.')
    }
  }

  async fetchTestView(id: EcgTest.Id) {
    const route = `${this.ecgRoute}/${id}`
    try {
      const res = (await api.get(route)) as Resp.TestView
      const { details, testGroup, totalPage, ...test } = res
      const obj = {
        selectedTest: deserializeTest(test),
        details,
        testGroup: deserializeToGroups('t', testGroup) as TestGroups,
        totalPage
      }
      return obj
    } catch {
      return undefined
    }
  }

  async fetchStrips(id: EcgTest.Id, page: number, pid?: number) {
    const route = `${this.ecgRoute}/${id}/${page}`
    try {
      const res = (await api.get(route, { params: { pid } })) as Resp.Strips
      const obj = {
        stripUrl: res.imagePath,
        sampleGroup: deserializeToGroups('s', res.sampleGroup) as SampleGroups
      }
      return obj
    } catch {
      return undefined
    }
  }

  /**
   * @description Single toggle
   */
  async postTestGroupToggle(
    dbId: EcgTest.Id,
    gid: number,
    toggle: boolean
  ): Promise<boolean> {
    const route = `${this.groupRoute}/t/change`
    const act = toggle ? 'add' : 'del'
    try {
      const body = { works: [dbId], id: gid, act }
      const res = (await api.post(route, body)) as Resp.GroupChange
      if (
        (toggle && res.result[0].message === 'Added') ||
        (!toggle && res.result[0].message === 'Deleted')
      ) {
        return true
      }
      return false
    } catch {
      return false
    }
  }

  /**
   * @description Single toggle
   */
  async postSampleGroupToggle(
    dbId: EcgTest.Id,
    page: number,
    gid: number,
    toggle: boolean
  ): Promise<boolean> {
    const route = `${this.groupRoute}/s/change`
    const act = toggle ? 'add' : 'del'
    try {
      const body = { works: [[dbId, page]], id: gid, act }
      const res = (await api.post(route, body)) as Resp.GroupChange
      if (
        (toggle && res.result[0].message === 'Added') ||
        (!toggle && res.result[0].message === 'Deleted')
      ) {
        return true
      }
      return false
    } catch {
      return false
    }
  }
}
