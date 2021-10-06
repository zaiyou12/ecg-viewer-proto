declare namespace EcgTest {
  interface Meta {
    testSeq: number | string
    duration: number | string
    region: DataLake.Region
    sampled?: boolean
    normal?: boolean
    readonly path?: string
  }
}
