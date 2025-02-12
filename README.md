#Football matchmaker 

# Create directories

First you'll need to create the structure below in the project root:

`/data`


# how to build

`docker-compose build`


# how to access bash

`docker-compose run --rm processing bash`


# Run the scrip to create de croped images with faces
`python3 matchmaker.py`

# Run command directly

`docker-compose run --rm processing python3 matchmaker.py`
