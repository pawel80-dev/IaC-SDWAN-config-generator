variable "azure_rg_name" {
  description = "Resource Group name"
  type = string
  default = ""
}

variable "azure_region" {
  description = "Region where all resources will be created"
  type = string
  default = ""
}

variable "azure_service_plan" {
  description = "Service Plan name"
  type = string
  default = ""
}

variable "azure_storage_account" {
  description = "Storage Account name"
  type = string
  default = ""
}

variable "azure_storage_container" {
  description = "Storage Container name"
  type = string
  default = ""
}

variable "azure_mi" {
  description = "Managed Identity name"
  type = string
  default = ""
}

variable "azure_kv" {
  description = "Key Vault name"
  type = string
  default = ""
}

variable "azure_log_analytic_workspace" {
  description = "Log Analytic Workspace name"
  type = string
  default = ""
}

variable "azure_app_insights" {
  description = "Application Insights name"
  type = string
  default = ""
}

variable "azure_func_app" {
  description = "Function App name"
  type = string
  default = ""
}

variable "azure_py_version" {
  description = "Function App Python version"
  type = string
  default = ""
}