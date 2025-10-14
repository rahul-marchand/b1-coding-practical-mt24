# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a coding practical for the B1 Scientific Coding course at Oxford (MT24). The project simulates an Unmanned Underwater Vehicle (UUV) submarine navigating through an underwater cave system while following a reference trajectory.

## Development Environment

Install dependencies:
```bash
pip install -r requirements.txt
```

Dependencies: numpy, pandas, matplotlib

## Code Architecture

### Core Module: `uuv_mission/`

**dynamic.py** - Contains the simulation dynamics and control loop:
- `Submarine`: Physics model with mass, drag, and actuator dynamics. Uses discrete-time simulation with constant x-velocity and controlled y-position (depth)
- `Mission`: Dataclass holding reference trajectory and cave boundaries (cave_height, cave_depth). Create via `Mission.random_mission(duration, scale)` or `Mission.from_csv(file_name)` (student to implement)
- `Trajectory`: Stores and visualizes position history. Key method: `plot_completed_mission(mission)` shows trajectory overlaid on cave terrain
- `ClosedLoop`: Simulation engine combining plant (Submarine) and controller. Run with `simulate(mission, disturbances)` or `simulate_with_random_disturbances(mission, variance)`

**terrain.py** - Mission generation utilities:
- `generate_reference_and_limits(duration, scale)`: Creates reference trajectory with upper/lower cave boundaries using multisine signals
- `generate_random_multisine_timeseries(length)`: Base signal generator using fixed frequencies [0.05, 0.1, 0.5, 1]
- `write_mission_to_csv(mission, file_name)`: Exports Mission to CSV with columns: reference, cave_height, cave_depth

### Key Implementation Details

The `Submarine` physics model (dynamic.py:22-28):
- Position updates: `pos_x += vel_x * dt`, `pos_y += vel_y * dt`
- Force model: `force_y = -drag * vel_y + actuator_gain * (action + disturbance)`
- Y-axis acceleration driven by control action and disturbances

The `ClosedLoop.simulate()` method (dynamic.py:87-103) contains a placeholder at line 100 where students should call their controller with `observation_t` (current depth) and `mission.reference[t]` to compute `actions[t]`.

### Data Format

CSV missions (data/mission.csv) have three columns:
- `reference`: Target depth at each timestep
- `cave_height`: Upper cave boundary (positive values)
- `cave_depth`: Lower cave boundary (negative values)

### Development Workflow

Work in Jupyter notebooks (notebooks/demo.ipynb) to:
1. Implement controller logic
2. Implement `Mission.from_csv()` method (dynamic.py:77-79)
3. Run closed-loop simulations with provided missions
4. Visualize results using `trajectory.plot_completed_mission(mission)`

Note: The controller integration point in ClosedLoop.simulate() (line 100) is currently commented out and needs student implementation.
