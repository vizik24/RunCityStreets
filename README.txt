RunCityStreets v0.1 (Alpha)

Motivation + Aims:
This project was started with a desire to run the length of my entire local area. I soon learned that
route planning could get pretty complicated - especially if you want to avoid re-running streets.

This project aims to find the most efficient running routes to achieve the above goal. 

Current State of the Project:
Provided with a shapefile of a given road network, the program converts this to a graph. From this graph,
the Eulerian path is calculated, if this is not possible you can calculate the semi-eulirian path.

Next steps:
- calculate hamiltonian path if eulirian or semi-eulirian paths are not possible.
- output calculated path to a gpx file
- automate path calculation so that it finds the eulirian, then semi-eulirian then hamiltonian - in that order.
- GUI
- produce a shapefile automatically from an area selected on an open streetmap


Please don't distribute or try and make money using my code without my permission etc.