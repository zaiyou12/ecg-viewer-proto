import api from './api'
import { deserializeToGroups } from './deserializer'

export default class GroupApi {
  private baseRoute = import.meta.env.VITE_GROUP_API_ROUTE as string

  constructor() {
    if (this.baseRoute == undefined) {
      throw new Error('No base route provided for GroupApi. Check .env.')
    }
  }

  async getGroupList(type: 't' | 's' | 'p') {
    try {
      const res = (await api.get(this.baseRoute, {
        params: { type }
      })) as Resp.GroupListResp
      const obj = {
        numGroups: res.totalNum,
        groups: deserializeToGroups(res.groupList)
      }
      return obj
    } catch {
      return undefined
    }
  }
}
