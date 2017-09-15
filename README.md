This example code may be used in combination with Action-Oriented Log Forwarding on a Palo Alto Networks Firewall to automatically change the Network Security Group (NSG) in Azure when a threat is detected by the firewall. The HTTP Server Profile on the firewall is configured to include the relevant information in the POST request body. The code is imported as part of an HTTP-triggered Azure Function. When activated by a message from the firewall, it will extract the relevant information from the request body, request an API Access Token from Azure, and then make the relevant API call to Azure to update the specified NSG.

The code does not have any additional requirements/libraries other than those already provided by Azure.

Implementation of the code does require an Azure Service Principal with "Contributor"-level access.

Additional Information:

API Documentation: https://docs.microsoft.com/en-us/rest/api/
<br>Registering an Application: https://docs.microsoft.com/en-us/rest/api/#register-your-client-application-with-azure-ad
<br>NSG API Documentation: https://docs.microsoft.com/en-us/rest/api/virtualnetwork/networksecuritygroups

Support Policy

This template is released under an as-is, best effort, support policy. It should be seen as community supported and Palo Alto Networks will contribute our expertise as and when possible. We do not provide technical support or help in using or troubleshooting the components of the project through our normal support options such as Palo Alto Networks support teams, or ASC (Authorized Support Centers) partners and backline support options. The underlying product used (the VM-Series firewall) by the scripts or templates are still supported, but the support is only for the product functionality and not for help in deploying or using the template or script itself. Unless explicitly tagged, all projects or work posted in our GitHub repository (at https://github.com/PaloAltoNetworks) or sites other than our official Downloads page on https://support.paloaltonetworks.com are provided under the best effort policy.
