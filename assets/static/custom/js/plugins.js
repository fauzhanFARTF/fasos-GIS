// Control Mouse Position
let ctlMousePosition = L.control.mousePosition({
    position: 'bottomright',
}).addTo(map); 

// Control Pan
let ctlPan = L.control.pan({position: "bottomleft"}).addTo(map);
