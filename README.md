# Predicting Golf Ball Carry Distance from a Launch Monitor

Josiah Duhaime

---

## Background

---

## Goals

---

## Data

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

* ball_speed          Meters per Second
* azimuth             Degrees
* launch_angle        Degrees
* back_spin           Revolutions per Minute
* side_spin           Revolutions per Minute
* total_spin          Revolutions per Minute
* spin_axis           Degrees
* carry_distance      Meters
* total_distance      Meters
* offline_distance    Meters
* distance_to_pin     Meters
* max_height          Meters
* descent_angle       Degrees

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
