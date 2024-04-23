// MAP HOME
    /*  const map = L.map('peta').setView([-6.1950,106.5528], 11);
        L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>' 
        }).addTo(map);
    */

    const cities = L.layerGroup();

// Map Provider
    // Layer OSM
    const osm = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    });
    // Layer OSM Hot
    const osmHOT = L.tileLayer('https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '© OpenStreetMap contributors, Tiles style by Humanitarian OpenStreetMap Team hosted by OpenStreetMap France'
    });
    // Layer ESRI World Imagery
    const Esri_WorldImagery = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
        attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'
    });
    //  Layer CartoDB_Positron
    const CartoDB_Positron = L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
        subdomains: 'abcd',
        maxZoom: 20
    });

    
    const map = L.map('peta', {
        center: [-6.1950, 106.5528],
        zoom: 11,
        layers: [CartoDB_Positron, cities]
    })
    
    const baseLayers = {
        "OpenStreetMap": osm,
        "OpenStreetMap.HOT": osmHOT,
        "Sattelite ESRI World Imagery" : Esri_WorldImagery,
        "CartoDB": CartoDB_Positron,

    };
    
    const overlays = {
        'Fasilitas Kesehatan': cities
    };

    const layerControl = L.control.layers(baseLayers, overlays, {position: 'topleft' }).addTo(map);
    

