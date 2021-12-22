$("#calendar").evoCalendar({
    theme: 'Royal Navy',
    calendarEvents: [{
            id: 'bHay68s', // Event's ID (required)
            name: "New Year", // Event name (required)
            date: "February/1/2021", // Event date (required)
            type: "holiday", // Event type (required)
            everyYear: true // Same event every year (optional)
        },
        {
            name: "Vacation Leave",
            badge: "02/13 - 02/15", // Event badge (optional)
            date: ["February/13/2021", "February/15/2021"], // Date range
            description: "Vacation leave for 3 days.", // Event description (optional)
            type: "event",
            color: "#63d867" // Event custom color (optional)
        },
        {
            name: "Vacation Leave",
            badge: "02/13 - 02/15", // Event badge (optional)
            date: ["December/31/2021"], // Date range
            description: "Vacation leave for 3 days.", // Event description (optional)
            type: "event",
            color: "#63d867" // Event custom color (optional)
        },
        {
            name: "Vacation Leave",
            badge: "02/13 - 02/15", // Event badge (optional)
            date: ["December/12/2021"], // Date range
            description: "Vacation leave for 3 days.", // Event description (optional)
            type: "event",
            color: "red" // Event custom color (optional)
        }

    ]
});