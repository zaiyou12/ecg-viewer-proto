declare namespace DataLake {
  type Region = 'AU' | 'UK' | 'KR' | 'N/A'

  interface Meta {
    fsRootPath: string
    numEcgTests: number
  }
}
