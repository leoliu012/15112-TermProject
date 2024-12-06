# Welcome to TimeWise Transport!

## Description: 
This project is a traffic simulation game where users design a road network to efficiently transport cars to their destinations. 
The goal is to minimize the average time cars spend traveling.

## Features

| Feature                           | Description                                                                                                                                                                                                     |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Dynamic Road Building             | Create straight and curved roads, as well as bridges, to form a comprehensive transportation network.                                                                                                           |
| Magnetic Cursor                   | The location of the cursor will be magnetically attracted to road starting/ending points, and will cross the intersecting roads automatically                                                                   |
| Difficulty Levels                 | Users can select the difficulty level from 3-8, representing the number of traffic outlets they need to connect                                                                                                 |
| Traffic Simulation                | Watch as cars navigate through the network and how they to reach their destinations efficiently.                                                                                                                |
| Path Finding                      | Finds the top three shortest paths and allow each car to select the optimal path based on the road conditions.                                                                                                  |
| Traffic Lights                    | Traffic lights will be generated at eligible intersections and will control the car's movement depending on the car's intended direction (going straight, right, and left).                                     |
| Customize Traffic Lights Duration | The user can customize the duration of traffic lights when drawing the roads                                                                                                                                    |
| Settings Customization            | Toggle background music, sound effects, car representations for display, and car paths.                                                                                                                         |
| Instructions and History          | Access detailed instructions and view historical scores to track your progress.                                                                                                                                 |
| Scoring System                    | Earn points based on the efficiency of the road network and the performance of traffic management (the number of cars reached their destinations, the difficulty level, and the average time spent by each car. |


## Run Instructions:

### Prerequisites
Windows 10+

macOS 10.13+

Python 3.6-3.11

## Project Installation

### Project Setup
Clone the repository:
```commandline
git clone https://github.com/leoliu012/15112-TermProject
```

```commandline
cd 15112-TermProject
```

### Setup Virtual Environment
Setting up a virtual environment is recommended
```commandline
python -m venv venv
```
Then activate the virtual environment:
#### On Windows:
```commandline
venv\Scripts\activate
```
#### On MacOS/Linux:
```commandline
source venv/bin/activate
```

### Required Libraries
cmu-graphics package and Pillow are two required libraries for this project.

Under the directory of this project, run:
```commandline
pip install -r requirements.txt
```
Or:
```commandline
pip install cmu_graphics Pillow
```

### Running the game
To run the game, run:
```commandline
cd ./src
```
Then:
```commandline
python main.py
```

## Instructions
This instruction can also be accessed by click "Instructions" button on the menu. But the instruction below is more 
detailed and throughout for developing purposes.
### Player goal
In this game, the player's goal is to design an efficient road network that allows each car to reach its destination as 
quickly as possible. Cars are generated from different outlets on the screen, and each outlet also serves as a 
destination. Player's task is to connect these traffic outlets by designing straight roads, curved roads, and bridges
### Drawing straight roads
To draw straight roads, please elect the 'Straight' road mode from the toolbar on the top left of the screen. 
Then click on the canvas where you want the road to start. 
Then click again at the desired end point to complete the straight road.
The road will automatically align to the grid for precision. 

Tip: Please ensure that roads are spaced adequately to prevent traffic congestion.

### Drawing curved roads
To draw curved roads, please elect the 'Curved' road mode from the toolbar.
Click on the canvas to set the starting point of the curve.
Then click at the midpoint where you want the curve to bend.
Click once more at the end point to complete the curved road.

### Drawing bridges
To create a bridge, select the Straight or Curved road mode and click once on the canvas to connect your road to a 
ground-level road. Press the 'Up' key to elevate the road to bridge level, 
then continue drawing the bridge as usual. 
To connect the bridge back to the ground, switch to Bridge mode, click the desired starting point, 
and press the 'Down' key to lower the road back to ground level and click the desired end point.

### Remove road
To remove a road, select the 'Bulldoze' mode from the toolbar.
Hover over the road segment you wish to remove. The selected  road will be highlighted. 
Click on the highlighted road to remove it from your network.

### Customize traffic lights durations
Click "Traffic Lights" at the toolbar and drag the slider to customize the duration of the traffic lights

NOTE: This action only effective to roads that haven't been drawn yet/

### Run the simulation
Once the user have designed the road network, click the 'Finished' button to begin the simulation.

