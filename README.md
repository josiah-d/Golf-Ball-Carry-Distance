# Predicting Golf Ball Carry Distance from a Launch Monitor

Josiah Duhaime

---

## Background

---

## Goals

---

## Data

### Features

* Ball Speed: Meters per Second
    * The measurement of the golf balls velocity measured just after impact
* Azimuth: Degrees
    * The initial horizontal angle relative to the target line
* Launch Angle: Degrees
    * The initial vertical angle of ascent relative to the ground plane measured in degrees
* Back Spin: Revolutions per Minute
    * Rotation opposite to the direction it is flying
* Side Spin: Revolutions per Minute
    * Rotation sideways or horizontal to the direction it is flying
* Total Spin: Revolutions per Minute
    * The total amount of spin around the spin axis that creates curvature and lift
* Spin Axis:  Degrees
    * The axis that the golf ball rotates around to create shot curvature and lift.
* Offline Distance: Meters
    * The end position distance right or left measured from the target-line
* Max Height: Meters
    * The apex of the trajectory measured from the ground plane
* Descent Angle: Degrees
    * The vertical angle the ball descend from the apex
* Club Type:
    * Driver
    * Fairway Wood
    * Hybrid
    * Iron
    * Wedge

**Note: The club type was not used for analyses due to apparently errant data.**

For example, there was logged wedge data that had a flight path consistent with
a driver. Due to the quality of the data, a determination was made to trust the
launch monitor data and to attribute the classification error to human error.

### Target

* Carry Distance: Meters
    * The total distance of flight produced by initial launch condition

---

## Data Visualization

---

## Statistics

---

## Model

### Model Performance

---

## Conclusions

---

## Next Steps

* Add UI interaction declaring limiting feature of carry distance
* Feature creation
* Access raw data
* Comparision against other launch monitors
* Incorporate weather


## TODO

* Calc distance with physics
* Use ML

## Desciption

Features:



## Notes

* Missing data: 1878 files
    * System started without any shots taken
* dropping putter strokes
    * <1% of data
    * Different swing mechanics
* Some errant club data noted
    * eg 300 m wedge
    * Likely artifact of not switching the club selected
    * otherwise the data is sound
