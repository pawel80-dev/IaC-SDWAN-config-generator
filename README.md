# IAC-SDWAN-config-generator

> [!NOTE]
> For most of my projects, the leading branch is the **dev** one. That means that *_dev.yaml file is the most frequently used workflow/pipeline.  

Initial config is needed when ISP doesn't provide you DHCP based IP address.  
In our case there are two options to generate the config:  
- API call towards Manager to generate full bootstrap config based on existing device configuration  
- create a minimalistic boostrap config based on the data from SD-WAN deploy repository (TODO)  

Bootstrap file will be send to designated email address.  

The whole process could be extended with a few extra steps like Manager - PNP portal sync or attach a template to a new device.  

![alt text](drawings/cfg_gen_v09.png)  
*Config generator: Possible deployment options*  

Config generator, possible deployments (description):  
1. Create the config running python code on your laptop
2. Create the config running Github workflow
3. Create the config running Github workflow: Azure Function
4. Create the config running Github workflow: Google Cloud Run Function
5. Create the config running Github workflow: Azure Conteiner Apps

![alt text](drawings/workflow_opt_v01.png)  
*Config generator: Github workflow options*  
