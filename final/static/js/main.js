$(document).ready(function(){
  var markers = window.cities;

  // Initialize Japan's map
  var map = L.map('map').setView([35.915952, 134.774506], 6);

  L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18
  }).addTo(map);

  L.control.scale().addTo(map);

  DrawCities();
  //Tsunami circle
  /*
  L.circle([{{ latTsunami }}, {{ lonTsunami }}], 400000, {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.1
  }).addTo(map);
  L.circle([{{ latTsunami }}, {{ lonTsunami }}], 500, {
    color: 'red',
    fillColor: '#fff',
    fillOpacity: 0.8
  }).addTo(map);*/
  //-------------------------------------------------
  //alert(inCircle(34.204902,137.411225,500000,35.462635, 139.774854));
  map.on('click', function(e) {
  //alert("Lat, Lon : " + e.latlng.lat + ", " + e.latlng.lng)
  });
  //-------------------------------------------------
  //People circle
  /*{% for data in datas %}
  L.circle([{{ data.0 }},{{ data.1 }}], 500, {
    color: 'green',
    fillColor: '#fff',
    fillOpacity: 0.5
  }).addTo(map);
  {% endfor %}
  //L.marker([35.462635,139.774854]).addTo(map).on('mouseover', onClick);
  /*function onClick(e) {
  alert(this.getLatLng());
  }*/

  $("#tsunami_submit").click(function(){
    tsunami();
  });

  function tsunami(){

    // Retrieve data
    var long = $("#tsunami_lon").val();
    var lat = $("#tsunami_lat").val();
    var dat = $("#tsunami_date").val();
    var data = {lon : long,lat:lat,date:dat}
    // Notify server
    $.ajax({
      type: "POST",
      url: "/tsunami",
      data: data,
      dataType:"json",
      success: function(data){
        console.log(data);
      }
    });
  }


  function DrawCities() {
    for ( var i=0; i < markers.length; ++i )
    {
      L.marker( [markers[i].lat, markers[i].lng] )
      .bindPopup( '<center><a href="' + markers[i].url + '" target="_blank">' + markers[i].name + '</a></center>' + '<div>Population: ' + markers[i].population + '</div>')
      .addTo( map );
    }
  }

  function inCircle(latCenterCircle,lonCenterCircle,rad,lat,lon){
    rad = rad / 1.6;
    var dis = L.latLng([latCenterCircle, lonCenterCircle]).distanceTo([lat, lon]);
    if(dis<=rad){
      return true;
    }
    else{
      return false;
    }
  }
});
