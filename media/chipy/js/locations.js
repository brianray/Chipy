$(function() {
  // Google Map options
  // var myLatLng = new google.maps.LatLng(lat,lng);
  var Ravenswood = new google.maps.LatLng(41.945972,-87.690372);
  if(_geo.length > 1) {
	  var myLatLng = new google.maps.LatLng(_geo[0][0],_geo[0][1]);
  } else {
	  var myLatLng = Ravenswood;
  };
  
  var myCanvas = document.getElementById("map_canvas");
  var myMapOpts = {
	  zoom: 12,
	  center: myLatLng,
	  mapTypeId: google.maps.MapTypeId.ROADMAP
  };
  var map_canvas = new google.maps.Map(myCanvas, myMapOpts);

  // Add markers to the map_canvas from the _geo array of points
  //
  if(map_canvas) {
	// add location markers from the _geo tuple to the map
	var markers = new Array();
	var myBounds = new google.maps.LatLngBounds();
	for(var i = 0; i < _geo.length; ++i) {
		var g = _geo[i];
		var markerLatLng = new google.maps.LatLng(g[0], g[1]);
		markers[i] = new google.maps.Marker({
											position: markerLatLng,
											map: map_canvas,
											title: g[2]
											});
		if (_geo.length > 1) {
			myBounds.extend(markerLatLng);
			map_canvas.fitBounds(myBounds);
		}
	}
  }
});