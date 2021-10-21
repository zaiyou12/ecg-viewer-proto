import api from './api'

export default class GroupApi {
  private baseRoute = import.meta.env.VITE_GROUP_API_ROUTE as string

  constructor() {
    console.log('This is the GroupApi constructor.')
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
        numGroups: res.total_num,
        groups: this.deserializeAllGroup(res.group_list)
      }
      return obj
    } catch {
      return undefined
    }
  }

  private deserializeGroup(group: { id: number; name: string }): TestGroup {
    return {
      id: group.id,
      displayName: group.name
    }
  }

  private deserializeAllGroup(groups: { id: number; name: string }[]) {
    return groups.map((g) => this.deserializeGroup(g))
  }
}
