// Routing Basic Example
    /*
    L.Routing.control({
        waypoints: [
            L.latLng(-6.270112, 106.484313),
            L.latLng(-6.224910, 106.506233)
        ],
        routeWhileDragging: true
    }).addTo(map);
    */

// Routing Machine Basic
    const control = L.Routing.control({
        language: 'id',
        formatter:  new L.Routing.Formatter({
            language: 'id' 
        }),
        waypoints: [
            L.latLng(-6.222281, 106.560478),
            L.latLng(-6.270123, 106.484379)
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

// Routing use GraphHopper
    // var routingControl = L.Routing.control({
    //     waypoints: [
    //         L.latLng(-6.222045, 106.560920),
    //         L.latLng(-6.197103, 106.439644)
    //     ],
    //     geocoder: L.Control.Geocoder.nominatim(),
    //     router: L.Routing.graphHopper('4a404492-6e4e-4237-bb8d-645ee9fafe67'),
    //     routeWhileDragging: false
    // }).addTo(map);

    // var router = routingControl.getRouter();
    // router.on('response',function(e){
    // console.log('This request consumed ' + e.credits + ' credit(s)');
    // console.log('You have ' + e.remaining + ' left');
    // });


    function keSini(Lat,Lng){
        let latLng = L.latLng(Lat, Lng)
        control.spliceWaypoints(control.getWaypoints().length - 1, 1, latLng)
    }

    