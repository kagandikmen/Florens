# Florens

A small command-line tool written in Python which takes

meteorological data from [Open-Meteo Weather API](https://open-meteo.com)\
soil composition data from [Soilgrids REST API](https://rest.isric.org/)

and checks if the next 7 days are optimal for planting a particular plant specified by the user. To my knowledge, there is no other tool so far taking current soil temperature and local soil composition data into account while checking for optimal conditions, which makes Florens unique and first-of-its-kind.

## Dependencies

geopy\
requests

## Current Status

The general structure is completed and works fine. More plant types should be added. Uncommented API accesses can be turned on if wished.

## Contributing

Pull requests, suggestions, bug fixes etc. are all welcome. I would be more than glad if you're an expert in agricultural science who wants to contribute.

## License

MIT License