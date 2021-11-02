import { defineStore } from 'pinia'
import GroupApi from '../utils/group-api'
import useDataLakeStore from '../stores/data-lake'

const api = new GroupApi()

type GroupPageState = {
  type?: Resp.GroupType
  selectedGroupId?: number
  selectedGroupName?: string
  tests?: EcgTests
  samples?: [EcgTest.Meta, number[]][]
  loading: boolean
}

const useGroupPageStore = defineStore('groupPage', {
  state: () => {
    return {
      type: undefined,
      selectedGroupId: undefined,
      selectedGroupName: undefined,
      tests: [],
      samples: [],
      loading: false
    } as GroupPageState
  },
  actions: {
    resetGroupPage() {
      this.type = undefined
      this.selectedGroupId = undefined
      this.selectedGroupName = undefined
      this.tests = []
      this.samples = []
      this.loading = false
    },

    async fetchTestList(gid: number) {
      this.loading = true
      const res = await api.getTestsInGroup(this.type!, gid)
      if (res === undefined) return
      const lakeStore = useDataLakeStore()
      this.selectedGroupId = gid
      if (this.type! === 't') {
        this.tests = res as EcgTests
        this.selectedGroupName = lakeStore.testGroups[gid].groupName
      } else {
        this.samples = res as [EcgTest.Meta, number[]][]
        this.selectedGroupName = lakeStore.sampleGroups[gid].groupName
      }
      this.loading = false
    },

    async addGroup(groupName: string, groupStatus?: GroupStatus, path = './') {
      this.loading = true
      const res = await api.postAddGroup(
        this.type!,
        groupName,
        groupStatus,
        path
      )
      if (res) {
        const lakeStore = useDataLakeStore()
        await lakeStore.fetchGroupList(this.type!)
      }
      this.loading = false
    },

    async delGroup(gid: number) {
      this.loading = true
      const res = await api.postDelGroup(this.type!, gid)
      if (res) {
        const lakeStore = useDataLakeStore()
        await lakeStore.fetchGroupList(this.type!)
      }
      this.loading = false
    }
  }
})

export default useGroupPageStore
