import api from './api'
import { deserializeAllTestsInGroup } from './deserializer'

export default class GroupApi {
  private baseRoute = import.meta.env.VITE_GROUP_API_ROUTE as string

  constructor() {
    if (this.baseRoute == undefined) {
      throw new Error('No base route provided for GroupApi. Check .env.')
    }
  }

  /**
   *
   * @param type 't' | 's'
   * @param id Group ID
   */
  async getTestsInGroup(type: Resp.GroupType, id: number) {
    const route = `${this.baseRoute}/${type}/${id}`
    try {
      const res = (await api.get(route)) as Resp.TestsInGroup
      return deserializeAllTestsInGroup(type, res.tests)
    } catch {
      return undefined
    }
  }

  async postAddGroup(
    type: Resp.GroupType,
    groupName: string,
    groupStatus?: GroupStatus,
    path?: string
  ) {
    const route = `${this.baseRoute}/${type}/add`
    try {
      let body
      if (type === 'p') {
        body = { groupName, path }
      } else {
        body = { groupName, groupStatus }
      }
      const res = (await api.post(route, body)) as Resp.GroupAddDel
      if (res.message === 'Added') return true
      return false
    } catch {
      return false
    }
  }

  async postDelGroup(type: Resp.GroupType, id: number) {
    const route = `${this.baseRoute}/${type}/del`
    try {
      const res = (await api.post(route, { id })) as Resp.GroupAddDel
      if (res.message === 'Deleted') return true
      return false
    } catch {
      return false
    }
  }
}
