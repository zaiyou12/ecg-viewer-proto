import api from './api'
import { deserializeTest, deserializeToGroups } from './deserializer'
import { hasTypedProperty } from '../utils/helper'

export default class TestViewApi {
  private baseRoute = import.meta.env.VITE_TEST_VIEW_API_ROUTE as string

  constructor() {
    if (this.baseRoute == undefined) {
      throw new Error('No base route provided for TestViewApi. Check .env.')
    }
  }

  async fetchTestView(region: EcgTest.Region, testId: EcgTest.TestId) {
    const route = `${this.baseRoute}/${region}/${testId}`
    try {
      const res = (await api.get(route)) as Resp.TestViewResp
      const { details, testGroup, totalPage, ...test } = res
      const obj = {
        selectedTest: deserializeTest(test),
        details,
        testGroup: deserializeToGroups(testGroup) as TestGroups,
        totalPage
      }
      return obj
    } catch {
      return undefined
    }
  }

  async postTestGroupToggle(
    region: EcgTest.Region,
    testId: EcgTest.TestId,
    id: number,
    status: boolean
  ): Promise<boolean> {
    const route = `${this.baseRoute}/${region}/${testId}`
    try {
      const body = { testGroupId: id, status }
      const res = await api.post(route, body)
      if (hasTypedProperty(res, 'message')) {
        if (
          (status && res.message === 'Added') ||
          (!status && res.message === 'Deleted')
        ) {
          return true
        }
      }
      return false
    } catch {
      return false
    }
  }

  async fetchStrips(
    region: EcgTest.Region,
    testId: EcgTest.TestId,
    page: number,
    pid?: number
  ) {
    const route = `${this.baseRoute}/${region}/${testId}/${page}`
    try {
      const res = (await api.get(route, { params: { pid } })) as Resp.StripsResp
      const obj = {
        stripUrl: res.imagePath,
        sampleGroup: deserializeToGroups(res.sampleGroup) as SampleGroups
      }
      return obj
    } catch {
      return undefined
    }
  }

  async postSampleGroupToggle(
    region: EcgTest.Region,
    testId: EcgTest.TestId,
    page: number,
    id: number,
    status: boolean
  ) {
    const route = `${this.baseRoute}/${region}/${testId}/${page}`
    try {
      const body = {
        sample_group_id: id,
        status
      }
      const res = await api.post(route, body)
      if (hasTypedProperty(res, 'message')) {
        if (
          (status && res.message === 'Added') ||
          (!status && res.message === 'Deleted')
        ) {
          return true
        }
      }
      return false
    } catch {
      return false
    }
  }
}
