# nesting dictionaries in dictionaries
# travel_log = {
#   "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12,},
#   "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"],"total_visits": 15,},
# }
# print(travel_log)

# nesting dictionaries into lists
travel_log = [
  {
    "country" :"France",
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12,
  },

  {
    "country": "Germany",
    "cites_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 15,
  },
]
print(travel_log)
