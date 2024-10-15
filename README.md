# Stadium Map Visualizer

This project visualizes the locations and capacities of various stadiums around the world using Folium, a Python library for interactive maps.

## Features

- Displays stadiums categorized by continent.
- Uses color coding to represent stadium capacities.
- Interactive map that can be explored in a web browser.

## Requirements

- Python 3.x
- Libraries:
  - folium
  - pandas

You can install the required libraries using pip:

```bash
pip install folium pandas
```

## Data
The data for the stadiums is stored in a CSV file named stadiums.txt. The expected format of the file is as follows:

```bash
NAME,CAPACITY,REGION,LOCATION,LAT,LON
Stadium Name,Capacity,Region,City,Latitude,Longitude
```

## Example
```bash
Wembley Stadium,51.556, -0.279, 90000, Europe
```

## Usage
1.  Make sure you have the stadiums.txt file in the same directory as your script.
2.  Run the script:
```bash
python main.py
```
3.  Open the generated index.html file in your web browser to view the interactive map.

## Marker Color Coding
Red: Capacity less than 70.000
Beige: Capacity between 70.000 and 80.000
Dark Red: Capacity 80.000 and above

## [Visit Live Site](https://stadium-mapping.onrender.com)
