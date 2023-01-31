+ Must be stateless
+ Use HTTP Verbs
+ Transfer json (or xml)
+ Use directory like url pattern for routes

See [https://fem-node-api.netlify.app/](https://fem-node-api.netlify.app/)

1. Model the data!

Motorcycle resource

```json
{
  "brand": "Honda",
  "model": "Click 125i",
  "slug": "honda-click-125i",
  "name": "Honda Click 125i (2022)"
  "specifications": {
	  "engineType": "4 Stroke, 2- Valve, SOHC, Liquid-Cooled, eSP",
	  "ignitionType": "Full Transisterized",
	  "tireSizeFront": "90/80 - 14 M/C 43P (Tubeless)",
	  "tireSizeRear": "100/80 - 14 M/C 48P (Tubeless)",
	  "overallDimension": "1,918 x 679 x 1,066 (mm)",
	  "curbWeight": "112 Kg",
	  "groundClearance": "131mm",
	  "fuelTankCapacity": "5.5 L",
	  "batteryType": "12V - 5Ah (MF-WET)",
	  "displacement": "125 cc",
	  "brakeTypeFront": "Hydraulic Disc",
	  "brakeTypeRear": "Mechanical Leading Trailing",
	  "maximumPower": "8.2 kW @ 8,500 rpm",
	  "startingSystem": "Electric (ACG Sarter)",
	  "wheelType": "Cast Wheel",
	  "seatHeight": "769 mm",
	  "fuelSystem": "PGM-Fi",
	  "maximumTorque": "10.8 Nm @ 5,000 rpm"
  },
  "srp": "80,900"
}
```

2. Design the routes

```json
{
	"GET /motorcycles": {
		"desc": "Return all motorcycles",
		"response": "200 application/json",
		"data": [{},{}.{}]
	},
	"GET /motorcycles/keyword?filter=:filter&sort=:sort&page=:page&size=:size": {
		"desc": "Search for motorcycles by name, filter by TBD.",
		"response": "200 application/json",
		"data": [{},{}.{}]
	},
	"GET /motorcycles:slug": {
		"desc": "Return one motorcycle represented by its slug.",
		"response": "200 application/json",
		"data": {}
	},
	"POST /motorcycles": {
		"desc": "Create and return a new motorcycle.",
		"response": "201 application/json",
		"data": {}
	},
	"PUT /motorcycles:slug": {
		"desc": "Update and returns the matching motorcycle.",
		"response": "200 application/json",
		"data": {}
	},
	"DELETE /motorcycles:slug": {
		"desc": "Deletes and returns the matching motorcycle.",
		"response": "200 application/json",
		"data": {}
	},
}
```



## TODO
1. Validations! = Client and Database via Schema!
2. Closure. To return a function in middleware or not? Return = closure.
3. How to debug?
4. 