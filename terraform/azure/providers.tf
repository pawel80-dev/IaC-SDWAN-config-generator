terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
    }
  }
 # Hashicorp recommends using the cloud block instead of the backend block (legacy)
  cloud {
    organization = "tf-pawel-org"
    workspaces {
      name = "tf-azure"
    }
  }
}

provider "azurerm" {
  features {}
}
