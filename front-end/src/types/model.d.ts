declare interface AiModel {
  readonly id: number
  displayName: string
  description?: string
}

declare interface AiModelStatus {
  modelId: AiModel["id"]
  status: 'normal' | 'abnormal'
  anomaly?: AnomalyGroupId[]
}
