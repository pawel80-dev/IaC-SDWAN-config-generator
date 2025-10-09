# IAC-SDWAN-config-generator

> [!NOTE]
> For most of my projects, the leading branch is the **dev** one. That means that *_dev.yaml file is the most frequently used workflow/pipeline.  

Initial config is needed when ISP doesn't provide you DHCP based IP address.  
In our case there are two options to generate the config:  
- API call towards Manager to generate full bootstrap config based on existing device configuration  
- create a minimalistic boostrap config based on the data from SD-WAN deploy repository  
To access the repo data, I will use Github fine-grained personal access token.  
Data will be read from a repository: https://github.com/pawel80-dev/IaC-SDWAN-deployment  
File: /tf_sdwan/providers_devices.tf  
Alternative would be to create a separate source file (csv, excel, etc...) for a device variables.  

Bootstrap file will be send to designated email address.  

The whole process could be extended with a few extra steps like Manager - PNP portal sync or attach a template to a new device.  

![alt text](drawings/cfg_gen_v05.png)  
*Config generator: Possible deployment options*

Describie the flows:  
1.
2.
3.
