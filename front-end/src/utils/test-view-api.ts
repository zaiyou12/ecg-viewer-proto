import api from './api'
import { deserializeTest, deserializeToGroups } from './deserializer'
import { resultTransacted } from './group-api-helper'

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

  async postSingleGroupToggle(
    type: Resp.GroupType,
    gid: number,
    toggle: boolean,
    dbId: EcgTest.Id,
    page?: number
  ): Promise<boolean> {
    const route = `${this.groupRoute}/${type}/change`
    const act = toggle ? 'add' : 'del'
    try {
      const works: EcgTest.Id[] | [EcgTest.Id, number][] =
        type === 't' ? [dbId] : [[dbId, page!]]
      const body = { works, id: gid, act }
      const res = (await api.post(route, body)) as Resp.GroupChange
      return resultTransacted(res.result[0], type, toggle, works![0])
    } catch {
      return false
    }
  }
}
