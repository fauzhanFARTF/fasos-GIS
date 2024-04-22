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