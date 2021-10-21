declare interface AiModel {
  readonly id: number
  displayName: string
  description?: string
}

declare interface AiModelCondition {
  modelId: AiModel['id']
  condition: 'normal' | 'abnormal'
  anomaly?: AnomalyGroupId[]
}
