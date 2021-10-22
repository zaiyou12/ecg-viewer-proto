import api from './api'

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
        numGroups: res.total_num,
        groups: this.deserializeAllGroup(res.group_list)
      }
      return obj
    } catch {
      return undefined
    }
  }

  private deserializeGroup(group: Resp.GroupList): TestGroup {
    return {
      id: group.id,
      displayName: group.group_name
    }
  }

  private deserializeAllGroup(groups: Resp.GroupList[]) {
    const gi: { [id: number]: TestGroup | SampleGroup | PreprocessGroup } = {}
    groups.forEach((g) => {
      const d = this.deserializeGroup(g)
      gi[d.id] = d
    })
    return gi
    // return groups.map((g) => this.deserializeGroup(g))
  }
}
