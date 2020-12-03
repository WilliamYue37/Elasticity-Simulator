# Physics C Elasticity Simulation
## Introduction
The purpose of this simulation is to model the process of a ball with a certain predetermined elasticity and mass being dropped from a certain height and bouncing in a vacuum while displaying measurements and calculations throughout the process such as:
- Current velocity
- Height
- Momentum
- Kinetic energy
- Potential energy
- Total mechanical energy 

## Installation

To install the program clone the repository to a local folder using: 

`git clone`

Then run the program by entering:

`simulation.py`
  
## Running the Simulation
Enter the starting values (Mass, Elasticity, and Initial Height) into the table on the right and then press "Start".

The simulation can be paused and played using the "Pause"/"Play" buttons on the right.

To reset the simulation after starting it, press the "Reset" button.

## Limitations
The simulation assumes that the ball is being dropped in a vaccum, i.e. air resistance is not considered.

Once the ball bounces enough that it's velocity goes below 10^-3 the ball is stopped and the simulation ends. In reality, a ball bouncing in a vacuum would bounce infinitely. 
