// Routing Machine
    const control = L.Routing.control({
        language: 'id',
        formatter:  new L.Routing.Formatter({
            language: 'id' 
        }),
        waypoints: [
            L.latLng(-6.222045, 106.560920),
            L.latLng(-6.197103, 106.439644)
        ],
        geocoder: L.Control.Geocoder.nominatim(),
        routeWhileDragging: true,
        reverseWaypoints: true,
        showAlternatives: true,
        altLineOptions: {
            styles: [
                {color: 'black', opacity: 0.15, weight: 9},
                {color: 'white', opacity: 0.8, weight: 6},
                {color: 'blue', opacity: 0.5, weight: 2}
            ],
        },
    //router: L.Routing.mapbox('pk.eyJ1Ijoic2NvdGhpcyIsImEiOiJjaWp1Y2ltYmUwMDBicmJrdDQ4ZDBkaGN4In0.sbihZCZJ56-fsFNKHXF8YQ')
    })
    control.addTo(map);

    /*
    L.Routing.control({
        waypoints: [
            L.latLng(-6.270112, 106.484313),
            L.latLng(-6.224910, 106.506233)
        ],
        routeWhileDragging: true
    }).addTo(map);
    */

    function keSini(Lat,Lng){
        let latLng = L.latLng(Lat, Lng)
        control.spliceWaypoints(control.getWaypoints().length - 1, 1, latLng)
    }