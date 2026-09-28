targetScope = 'resourceGroup'

param location string = resourceGroup().location
param workspaceName string = 'law-observability-lab'
param actionGroupName string = 'ag-observability-lab'

resource workspace 'Microsoft.OperationalInsights/workspaces@2025-07-01' = {
  name: workspaceName
  location: location
  properties: {
    retentionInDays: 30
    sku: {
      name: 'PerGB2018'
    }
    features: {
      enableLogAccessUsingOnlyResourcePermissions: true
    }
  }
}

resource actionGroup 'Microsoft.Insights/actionGroups@2023-01-01' = {
  name: actionGroupName
  location: 'global'
  properties: {
    groupShortName: 'ObsLab'
    enabled: true
    emailReceivers: []
    smsReceivers: []
    webhookReceivers: []
  }
}

output workspaceId string = workspace.id
output actionGroupId string = actionGroup.id
