players = [
    <!-- Player 1 (user class) -->
    {
        "user_id": 5678, (int)
        "balance": "$50", (float)
        "Aquarium": { (aquarium class)
            "channel_id": 789456123, (int)
            "cycled": True, (bool)
            "volume": 50 litres, (bool)
            "substrate": "gravel", (str)
            "heater": True, (bool)
            "pollution": { (dict)
                "ammonia": 0.5,
                "nitrite": 0.3,
                "nitrate": 20,
            },
            "plants": [ (list)
                "anubias" (plant class),
                "hornwort" (plant class)
            ],
            "ph": 6.8, (float)
            "temperature": 27 C, (float)
            "fish": [ (list)
                {
                    "guppy", (fish class)
                    "betta", (fish class)
                    "koi" (fish class)
                }
            ]
        }
    },
    <!-- Player 2 -->
    {
        "user_id": 91011,
        "balance": "$20",
        "Aquarium": {
            "channel_id": 123456789,
            "cycled": False,
            "volume": 30 litres,
            "substrate": "sand",
            "heater": False,
            "pollution": {
                "ammonia": 1,
                "nitrite": 0.5,
                "nitrate": 10,
            },
            "plants": [
                "java_moss", "amazon_sword"
            ],
            "ph": 7.5,
            "temperature": "25 C",
            "fish": [

            ]
        }
    }
]
