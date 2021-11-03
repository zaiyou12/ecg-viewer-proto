declare type GroupCols = {
  label: string
  class: 'id' | 'name' | 'desc' | 'num' | 'pid'
  prop?: keyof TestGroup | keyof SampleGroup
}
