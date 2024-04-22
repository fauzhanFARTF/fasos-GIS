// Control Mouse Position
let ctlMousePosition = L.control.mousePosition({
    position: 'bottomright',
}).addTo(map); 

// Control Pan
let ctlPan = L.control.pan({position: "bottomleft"}).addTo(map);

// Implementation: Set native zoomControl option to false!
//  ZoomBar uses the initial map view as the home position.
    let zoom_bar = new L.Control.ZoomBar({position: 'topleft'}).addTo(map);
    L.tileLayer(
        'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', 
        {maxZoom: 11}).addTo(map);
    
    function getCenterAndZoom(){
    //    console.log("Lat: "+map.getCenter().lat);
    //    console.log("Lon: "+map.getCenter().lng);
    //    console.log("Zoom: "+map.getZoom());
        alert("Lat: "+map.getCenter().lat+"\nLon: "+map.getCenter().lng+"\nZoom: "+map.getZoom());
    }
// Control Zoom Slider
let ctlZoomSlider = L.control.zoomslider({position: 'topright'}).addTo(map);

// Plugins Control Minimap
let osmUrl='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
let osmAttrib='Map data &copy; OpenStreetMap contributors';
let osm2 = new L.TileLayer(osmUrl, {minZoom: 0, maxZoom: 13, attribution: osmAttrib });
let miniMap = new L.Control.MiniMap(osm2, { 
    toggleDisplay: true,
    position:'bottomright' 
}).addTo(map);

// Plugins Control Polyline Measure
let ctlMeasure = L.control.polylineMeasure().addTo(map);