import api from './api'
import { deserializeToGroups } from './deserializer'

export default class GroupApi {
  private baseRoute = import.meta.env.VITE_GROUP_API_ROUTE as string

  constructor() {
    if (this.baseRoute == undefined) {
      throw new Error('No base route provided for DataLakeApi. Check .env.')
    }
  }

  async getGroupList(type: Resp.GroupType) {
    try {
      const route = `${this.baseRoute}/${type}/list`
      const res = (await api.get(route)) as Resp.GroupList
      const obj = {
        numGroups: res.totalNum,
        groups: deserializeToGroups(res.type, res.groupList)
      }
      return obj
    } catch {
      return undefined
    }
  }
}
