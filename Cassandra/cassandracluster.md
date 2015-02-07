Installing a Cassandra cluster on Amazon EC2
====================
Documentation : [http://datastax.com/documentation/cassandra/2.1/cassandra/install/installAMI.html](http://datastax.com/documentation/cassandra/2.1/cassandra/install/installAMI.html)

Project japan-tsunami :  
[https://github.com/AndreiArion/bigdata-project-2014/](https://github.com/AndreiArion/bigdata-project-2014/)  
[https://github.com/anthonyray/japan-tsunami](https://github.com/anthonyray/japan-tsunami)


# DataStax AMI specification
- Ubuntu 12.04 LTS (Precise Pangolin), image (Ubuntu Cloud 20140227 release), Kernel 3.8+  
- Latest version of Cassandra
- Oracle Java 7 
- OpsCenter  
- Metrics tools : dstat, ethtool, make, gcc, and s3cmd
- Private interface for intra-cluster communication
- Sets the seed nodes cluster-wide

# Install Cassandra cluster
## Creating EC2 security group
Step1 : Open the Security Groups page  
Step 2 : Create a new security group with a name like 'CassandraRules'   
Step 3 : Add the following rules    
<table>
<thead>
<tr>
	<th>Port Number</th>
	<th>Type</th>
	<th>Protocol</th>
	<th>Source</th>
</tr>
</thead>
<tbody>
<tr>
	<td> 22 </td>
	<td> SSH </td>
	<td> TCP </td>
	<td> 0.0.0.0/0 </td>
</tr>
<tr>
	<td> 8888 </td>
	<td> Custom </td>
	<td> TCP </td>
	<td> 0.0.0.0/0 </td>
</tr>
<tr>
	<td> 1024 - 65355 </td>
	<td> Custom </td>
	<td> TCP </td>
	<td> mySecurityGroup </td>
</tr>
<tr>
	<td> 7000 </td>
	<td> Custom </td>
	<td> TCP </td>
	<td> mySecurityGroup </td>
</tr>
<tr>
	<td> 7001 </td>
	<td> Custom </td>
	<td> TCP </td>
	<td> mySecurityGroup </td>
</tr>
<tr>
	<td> 7199 </td>
	<td> Custom </td>
	<td> TCP </td>
	<td> mySecurityGroup </td>
</tr>
<tr>
	<td> 9042 </td>
	<td> Custom </td>
	<td> TCP </td>
	<td> 0.0.0.0/0 </td>
</tr>
<tr>
	<td> 9160 </td>
	<td> Custom </td>
	<td> TCP </td>
	<td> 0.0.0.0/0 </td>
</tr>
<tr>
	<td> 61620 </td>
	<td> Custom </td>
	<td> TCP </td>
	<td> mySecurityGroup </td>
</tr>
<tr>
	<td> 61621 </td>
	<td> Custom </td>
	<td> TCP </td>
	<td> mySecurityGroup </td>
</tr>
</tbody>
</table>   

## Create a key pair
Don't forget to create your keypair to have a complete SSH access, if it's not done so.

## Launching AMI
Step 1 : Choose the right region. For us-east-1 here is the link : 
[https://console.aws.amazon.com/ec2/home?region=us-east-1#launchAmi=ami-ada2b6c4](https://console.aws.amazon.com/ec2/home?region=us-east-1#launchAmi=ami-ada2b6c4)

Step 2 : Choose an instance type.  
- Development and light production: m3.large  
- Moderate production: m3.xlarge  
- SSD production with light data: c3.2xlarge  
- Largest heavy production: m3.2xlarge (PV) or i2.2xlarge (HVM)  
Warning : Micro, small, and medium types are not supported !  

Step 3 : Configure Instance Details and configure the instances to suit your requirements  
For example:  
```
--clustername japanCluster --totalnodes 5 --version community
```

Step 4 : Add Storage, and add volumes as needed  

Step 5 : Configure Security Groups. Add the one you created before  

Step 6 : Select an existing keypair. Add the one you created before  

Step 7 : Launch Instances  

## Access to OpsCenter
When your cluster is fully launched, go see your instances and select the one with an 'AMI launch index' equals to 0. Then open this URL :  
```
http://public_dns_of_first_instance:8888/
```  

Nb : if agents have not automatically been connected, click the Fix link located near the top left of the Dashboard. When prompted for credentials for the agent nodes, use the username ubuntu and copy and paste the entire contents from your private key (.pem).

# Python configuration
## Packages installation
```
sudo apt-get install python-setuptools python-dev build-essential python-pip  
sudo pip install --upgrade virtualenv  
pip install --upgrade setuptools  
sudo pip install datetime
sudo pip install math  
sudo pip install cassandra-driver  
sudo pip install pandas
sudo apt-get install git
```  
## Scripts installation
```
git clone https://github.com/anthonyray/japan-tsunami.git
```

# Import data into the cluster
## From S3
Configure s3cmd :  
```
s3cmd --configure
```  
```
AWSAccessKeyId=AKIXXXXXXXXX  
AWSSecretKey=4gXxxxxxxxxxxxxxxxxxxxxxx/
```  
Then connect to the node 0 with ssh and type the following command :  
```
s3cmd get s3://bigdata-paristech/projet2014/data/data_1MB.csv data_1MB.csv
```  

## Launch the process
Install the blist library (optimization)

````
sudo pip install blist
````

You have to launch the shell process called 'process.sh'. For example : 
```
sh process.sh 'japtest' 'bigtable' 'data_1MB.csv' 1000 1000
```  
<table>
<thead>
<tr>
	<th>Argument</th>
	<th>Description</th>
	<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
	<td>1</td>
	<td>Cassandra keyspace</td>
	<td>'japantest'</td>
</tr>
<tr>
	<td> 2 </td>
	<td> Cassandra table </td>
	<td> 'bigtable' </td>
</tr>
<tr>
	<td> 3 </td>
	<td> Data file </td>
	<td> 'data_1GB.csv' </td>
</tr>
<tr>
	<td> 4 </td>
	<td> Offset </td>
	<td> 1000 </td>
</tr>
<tr>
	<td> 5 </td>
	<td> Loop argu </td>
	<td> 1000 </td>
</tr>
</tbody>
</table> 

# Alert phones process
```
python sushiProcess.py 'japjapo' 'bigtablebis' 1000 1000 36.055 140.061 2015-01-05-10-32 2015-01-10-10-30 500
```  
<table>
<thead>
<tr>
	<th>Argument</th>
	<th>Description</th>
	<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
	<td>1</td>
	<td>Cassandra keyspace</td>
	<td>'japantest'</td>
</tr>
<tr>
	<td> 2 </td>
	<td> Cassandra table </td>
	<td> 'bigtable' </td>
</tr>
<tr>
	<td> 3 </td>
	<td> Offset </td>
	<td> 1000 </td>
</tr>
<tr>
	<td> 4 </td>
	<td> Loop argu </td>
	<td> 1000 </td>
</tr>
<tr>
	<td> 5 </td>
	<td> Tsunami latitude </td>
	<td> 36.055 </td>
</tr><tr>
	<td> 6 </td>
	<td> Tsunami longitude </td>
	<td> 140.061 </td>
</tr>
<tr>
	<td> 7 </td>
	<td> Range date inferior (y-m-d-h-m)</td>
	<td> 2015-01-05-10-32 </td>
</tr>
<tr>
	<td> 8 </td>
	<td> Range date superior (y-m-d-h-m)</td>
	<td> 2015-01-10-10-30 </td>
</tr>
<tr>
	<td> 9 </td>
	<td> Tsunami Radius (in km)</td>
	<td> 500 </td>
</tr>
</tbody>
</table>   
