$(function() {
  // Google Map options
  // var myLatLng = new google.maps.LatLng(lat,lng);
  var myMapOpts = {
	  zoom: 12,
	  center: new google.maps.LatLng(41.965972,-87.690372),
	  mapTypeId: google.maps.MapTypeId.ROADMAP
  }
  var map_canvas = new google.maps.Map(document.getElementById("map_canvas"), myMapOpts);

  // DISABLED FOR TESTING
  if(map_canvas && false) {
	// add location markers from the _geo tuple to the map
	for(var i = 0; i < _geo.length; ++i) {
		var g = _geo[i];
		var myLatLng = new google.maps.LatLng(g[0], g[1]);
		var myMarker = new YMarker(yPoint);
		// Create some content to go inside the SmartWindow
		var myMarkerContent = g[2];
		// When the marker is clicked, show the SmartWindow
		YEvent.Capture(myMarker, EventsList.MouseClick, function() {
			myMarker.openSmartWindow(myMarkerContent); 
		});
		// Put the marker on the map
		map.addOverlay(myMarker);
		var pageLink = document.getElementById('loc_' + i);
		if(pageLink) {
			pageLink.onclick = function() {
				var geoIndex = parseInt(this.id.replace('loc_', ''), 10);
				var g = _geo[geoIndex];
				var yPoint = new YGeoPoint(g[0], g[1]);
				map.drawZoomAndCenter(yPoint, 12);
				};
			}
		}
	}
});