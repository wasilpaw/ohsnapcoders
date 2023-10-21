Include: Cloud storage, automation, FTP
Automated configuration (embedded script, scrip on a bucket)
Automated VM creation using Terraform

Goal of this project is to simulate GCSC exam setup between schools and a central examination server. We will prove that the set up is correct by transferring dummy exam result files from school VMs to the central server.

1. https://medium.com/google-cloud/automation-vm-instance-tasks-and-configurations-using-startup-scripts-in-gcp-ca66f7c9afc
2. The exam infrastructure project https://github.com/wasilpaw/ohsnapcoders/blob/main/ExamInfraArchitecture.png
3. Create the network for your school school [DONE]
4. Create firewall rules for all the VMs in the network 
	6. egress 20,21 (for FTP connection originated from the exam VM in your network)
	7. ingress 22 for SSH connection from outside
5. Add start up script
	1. create Google Storage as in  https://cloud.google.com/compute/docs/instances/startup-scripts/linux#passing-storage
	2. download the script file https://github.com/wasilpaw/ohsnapcoders/blob/main/exam_infra_project and save as a new file with .sh extension (for example ToynbeeInfoScript.sh). The script updates the installed packages, creates a new folder and a file with an example result. We are using here CSV (coma separated values) format which  is one of the most popular format for storing data and could be opened in MS Excel or GSheet.
		1. Replace the name of the .csv file so that it has you school in it's name
	3. Upload the script to Google Storage bucket
	4. click on the create instance button. Fill in the configuration with same options as previously plus usage of the script as defined in the manual from !) Don't start the process of the creation yet. Instead find the "Equivalent code" at the bottom to see how the chosen option could used in automation. Remember to cover:
		1. region
		2. OS
		3. Network interface
		4. start up script
	5. Build the VM and verify that the startup script has been executed and the file is there :
		1. Check VM logs 
		2. log to the SSH terminal and  run the below command updating the name of the file to your's
```bash 
		cat /exam_results/SchoolNameResults20231021.csv
```
6. Create VM instance template
	1. Delete the VM you created in step 6
	2. Create an instance template from console https://cloud.google.com/compute/docs/instance-templates/create-instance-templates setting the same parameters as in step 6 (choose regional rather than global)
	3. Create a new VM instance but this time choose "New VM instance from template" and choose the template you have just created. All configuration should be ready there so the only thing to update could be the name of the VM
7. Upload exam results
	1. update the file with results by adding few results. You can do it at least in a couple of ways
```bash
		nano /exam_results/SchoolNameResults20231021.csv
		echo "Ada Lovelace,2023-10-21,Computer Science,99," >> Exam_results/SchoolNameResults20231021.csv
```
8. use ftp client to connect to the central Exam server and upload the file.
	1. Connect to the FTP server by typing  ftp -p *server_ip* where the ip should be taken from the google console (IPs are ephemeral). -p starts ftp in a passive mode.
	2. Username and password will be the name of your school.
	3. Google for ftp command line commands for ubuntu to find out how to upload the files

