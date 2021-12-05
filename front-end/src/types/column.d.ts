declare type GroupCol = {
  label: string
  class: 'id' | 'name' | 'desc' | 'num' | 'pid'
  prop?: keyof TestGroup | keyof SampleGroup
}

declare type TestCol = {
  label: string
  class:
    | 'db-id'
    | 'reg'
    | 'org-code'
    | 'site-name'
    | 'test-seq'
    | 'dur'
    | 'stat'
  prop?: keyof EcgTest.Meta
}
