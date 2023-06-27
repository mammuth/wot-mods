...


    "vehicleDistance": {
      "enabled": true,
      "x": -25,
      "y": -2,
      "alpha": 100,
      "name": "vehicleDistance",
      "shadow": {
        "enabled": true,
        "distance": 0,
        "angle": 0,
        "color": "0x000000",
        "alpha": 100,
        "blur": 2,
        "strength": 2
      },
      "textFormat": {
        "font": "$FieldFont",
        "size": 14,
        "color": "0xe3e3e3",
        "align": "center",
        "bold": true,
        "italic": false
      },
          "format": "{{py:vehicleDistance('{{name}}')}} m"
    },



...


    "textFields": [
      ${ "def.playerName" },
      ${ "def.hpPercent" },
      ${ "def.rating" },
      ${ "def.vehicleDistance" },
	  {}
    ]







    
