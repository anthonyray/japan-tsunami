# Japan Tsunami alert (Cassandra version)
The project aims to build a tsunami warning system with SMS for japanese people following an earthquake. People in threatened areas have to be warned as soon as possible. 

## Tools
- [Cassandra](http://cassandra.apache.org/) : Database column oriented with high scalability and high availability without compromising performance.
- [Leaflet](http://leafletjs.com/) : Javascript library to build interactive maps.
- [Flask](http://flask.pocoo.org/) : Tiny python framework to build web applications.  

## Cassandra design
<table>
<thead>
<tr>
	<th>Column</th>
	<th>Type</th>
	<th>Description</th>
	<th>Key type</th>
</tr>
</thead>
<tbody>
<tr>
	<td> timestamp </td>
	<td> timestamp </td>
	<td>People's geolocalisation date</td>
	<td>Primary key</td>	
</tr>
<tr>
	<td> latitude </td>
	<td> float </td>
	<td>Antenna's latitude</td>
	<td>-</td>
</tr>
<tr>
	<td> longitude </td>
	<td> float </td>
	<td>Antenna's longitude</td>
	<td>-</td>
</tr>
<tr>
	<td> codegsm </td>
	<td> text </td>
	<td>Gsm of the antenna</td>
	<td>Partition key</td>
</tr>
<tr>
	<td> phone </td>
	<td> text </td>
	<td>People's phone number</td>
	<td>-</td>
</tr>
</tbody>
</table>  

## Installation
Just install the flask module  
```
pip install Flask
```  
And follow [these](cassandracluster.md) instructions for the cluster configuration

## Visualization  
<table>
<thead>
<tr>
	<th>Icon</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td> <center><img src="pictures/greencircle.png" /><center> </td>
	<td>One person geolocalized into tsunami radius</td>
</tr>
<tr>
	<td> <center><img src="pictures/redcircle.png" /><center> </td>
	<td>Tsunami radius</td>
</tr>
<tr>
	<td> <center><img src="pictures/marker.png" /><center> </td>
	<td>One city</td>
</tr>
</tbody>
</table> 
![screen1Japan](pictures/screen1Japan.png)  
