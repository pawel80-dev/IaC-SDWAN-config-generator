resource "azurerm_resource_group" "rg_func_v2" {
  name        = var.azure_rg_name
  location    = var.azure_region

  lifecycle {
    ignore_changes = [ tags ]
  }
}

resource "azurerm_service_plan" "sp_func_v2" {
  name                = var.azure_service_plan
  location            = azurerm_resource_group.rg_func_v2.location
  resource_group_name = azurerm_resource_group.rg_func_v2.name
  os_type             = "Linux"
  sku_name            = "FC1"
 
  lifecycle {
    ignore_changes = [ tags ]
  }
}

resource "azurerm_storage_account" "storage_func_v2" {
  name                     = var.azure_storage_account
  location                 = azurerm_resource_group.rg_func_v2.location
  resource_group_name      = azurerm_resource_group.rg_func_v2.name
  account_tier             = "Standard"
  account_replication_type = "LRS"
  min_tls_version          = "TLS1_2"

  lifecycle {
    ignore_changes = [ tags ]
  }
}

# Needed for Function App Flex Consumption
resource "azurerm_storage_container" "storage_container_func_v2" {
  name                  = var.azure_storage_container
  storage_account_id    = azurerm_storage_account.storage_func_v2.id
  container_access_type = "private"
}

resource "azurerm_log_analytics_workspace" "log_analytic_workspace_func_v2" {
  name                = var.azure_log_analytic_workspace
  location            = azurerm_resource_group.rg_func_v2.location
  resource_group_name = azurerm_resource_group.rg_func_v2.name
  sku                 = "PerGB2018"
  retention_in_days   = 30

  lifecycle {
    ignore_changes = [ tags ]
  }
}

resource "azurerm_application_insights" "app_insights_func_v2" {
  name                = var.azure_app_insights
  location            = azurerm_resource_group.rg_func_v2.location
  resource_group_name = azurerm_resource_group.rg_func_v2.name
  workspace_id        = azurerm_log_analytics_workspace.log_analytic_workspace_func_v2.id
  application_type    = "web"

  lifecycle {
    ignore_changes = [ tags ]
  }
}

resource "azurerm_user_assigned_identity" "mi_func_v2" {
  name                = var.azure_mi
  location            = azurerm_resource_group.rg_func_v2.location
  resource_group_name = azurerm_resource_group.rg_func_v2.name
}

data "azurerm_client_config" "current" {}

resource "azurerm_key_vault" "kv_func_v2" {
  name                        = var.azure_kv
  location                    = azurerm_resource_group.rg_func_v2.location
  resource_group_name         = azurerm_resource_group.rg_func_v2.name
  tenant_id                   = data.azurerm_client_config.current.tenant_id
  sku_name                    = "standard"
  purge_protection_enabled    = false
  soft_delete_retention_days  = 7

  lifecycle {
    ignore_changes = [ tags ]
  }
}

resource "azurerm_key_vault_access_policy" "kv_access_policy_func_v2" {
  key_vault_id = azurerm_key_vault.kv_func_v2.id
  tenant_id    = data.azurerm_client_config.current.tenant_id
  object_id    = azurerm_user_assigned_identity.mi_func_v2.principal_id

  key_permissions = [ 
    "Get", 
    "List" 
  ]

  secret_permissions = [
    "Get", 
    "List"
  ]
}

resource "azurerm_function_app_flex_consumption" "func_app_v2" {
  name                        = var.azure_func_app
  location                    = azurerm_resource_group.rg_func_v2.location
  resource_group_name         = azurerm_resource_group.rg_func_v2.name
  storage_container_type      = "blobContainer"
  storage_container_endpoint  = "${azurerm_storage_account.storage_func_v2.primary_blob_endpoint}${azurerm_storage_container.storage_container_func_v2.name}"
  storage_authentication_type = "StorageAccountConnectionString"
  storage_access_key          = azurerm_storage_account.storage_func_v2.primary_access_key
  runtime_name                = "python"
  runtime_version             = var.azure_py_version
#   storage_account_name       = azurerm_storage_account.storage_func_v2.name
#   storage_account_access_key = azurerm_storage_account.storage_func_v2.primary_access_key
  service_plan_id             = azurerm_service_plan.sp_func_v2.id

# Do not add the WEBSITE_RUN_FROM_PACKAGE on the Flex Consumption plan...
  # app_settings = {
  #   WEBSITE_RUN_FROM_PACKAGE  = 1
  # }

  site_config {
    application_insights_key               = azurerm_application_insights.app_insights_func_v2.instrumentation_key
    application_insights_connection_string = azurerm_application_insights.app_insights_func_v2.connection_string
  }

  lifecycle {
    ignore_changes = [ tags ]
  }
}