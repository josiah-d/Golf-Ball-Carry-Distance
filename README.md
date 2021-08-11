# Predicting Golf Ball Carry Distance from a Launch Monitor

Josiah Duhaime

---

![launch_demo](img/launch_demo.png)

## Table of Contents

* [Background](#background)
* [Goals](#goals)
* [Data](#data)
    * [Features](#features)
    * [Target](#target)
* [Data Visualization](#data-visualization)
* [Model](#model)
    * [Model Performance](#model-performance)
* [Conclusions](#conclusions)
* [Next Steps](#next-steps)

## Background

Launch monitors use highspeed, high-resolution cameras to capture ball
launch conditions with a high degree of accuracy. These data is then used to
predict the direction and distance of the golf ball. This information, coupled
with proper instruction, can be used to optimize one's golf swing to provide
creater control of the distance the ball travels and increase the ball's
distance. Further, the data collected from a launch monitor is frequently used
to simulate playing golf in indoor and outdoor environments. This is especially
apparent with the recent rise of [Top Golf](https://topgolf.com/us/).

---

## Goals

* Attempt to recreate a proprietary algorithm
* Increase understanding of ML models

---

## Data

The data was obtained from a privately owned
[ForeSight GCHawk](https://www.foresightsports.com/gchawk) and was requested
by the owner not to be shared publically.

![gchawk](img/gchawk.png)

The data was formatted as .json files containing user data and launch monitor
data from numerous golf swings. There were 10 features and 10,467 observations.
Unfortunately, there were 1,878 total instances were the system was started but
there were no golf swings executed and 86 strokes executed with a putter. Both
were excluded from analysis.

**Table 1: Manufactured Sample Data**

![data](img/sample_data.png)

### Features

![features](img/features.png)

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

![target](img/target.png)

* Carry Distance: Meters
    * The total distance of flight produced by initial launch condition

---

## Data Visualization

As seen in `Figure 1-3`, there are several features that have an apparent linear
relationship with the target and a colinearity between ball speed and max height.
These relationships persist across varied club types.

**Figure 1: Comparison of Ball Speed and Max Height Against Carry Distance**

![scatter](img/scatter_matrix/scatter.png)

**Figure 2: Ball Speed Against Carry Distance**

![ball_speed](img/ball_speed/ball_speed.png)

**Figure 3: Max Height Against Carry Distance**

![max_height](img/max_height/max_height.png)

The vast majority of the shots had a central tendency with thoses that were not
straight tending to have a lesser carry distance.

**Figure 4: Azimuth Against Carry Distance**

![launch_direction](img/launch_direction/launch_direction.png)

---

## Model

SKLearn was used to build various models. Each of these were initially tuned
with rough hyperparamters using GridSearchCV. These models were used due to
their ability to fit to a continuous target. The models used and the rationale
behind them include:

* Elastic Net Regularization
    * Allowance for both Lasso (L1) and Ridge (L2) regularization
* Partial Least Squares Regression
    * Multivariate regression that is resistant to the effect of colinearities
* Random Forest
    * Decreasing variance due to the injection of randomness, e.g. random
    sampling with replacement, node splitting by a random subset of features
* XGBoost
    * Regularization gradient boosting & speed/memory efficiency
* Gradient Boosting
    * Ability to combine weak learning models
    
### Baseline

Basic kinematic equations were used to estimate carry distance as a baseline.

**Equation 1: Maximizing Horizontal Distance**

![equation](img/kinematics.png)

### Model Performance

**Table 2: Model Performance**

| **Model**                 | **R2**        | **RMSE**   |
|---------------------------|---------------|------------|
| Kinematic Baseline        | 0.7984        | 29.3485    |
| ElasticNet                | 0.8911        | 20.2416    |
| PLSRegression             | 0.8911        | 20.2422    |
| RandomForestRegressor     | 0.9817        | 8.5562     |
| ***XGBRegressor***        | **0.9900**    | **6.4763** |
| GradientBoostingRegressor | 0.9880        | 6.9630     |

The XGBRegressor model with the following hyperparameters performed the best:

```python
base_score=0.5, booster='gbtree', colsample_bylevel=1,
colsample_bynode=1, colsample_bytree=0.9, gamma=0, gpu_id=-1,
importance_type='gain', interaction_constraints='',
learning_rate=0.003, max_delta_step=0, max_depth=3,
min_child_weight=1, missing=nan, monotone_constraints='()',
n_estimators=1000000, n_jobs=16, num_parallel_tree=1,
random_state=0, reg_alpha=0, reg_lambda=1, scale_pos_weight=1,
subsample=0.9, tree_method='exact', validate_parameters=1,
verbosity=None
```

Using this model, it is rather apparent that the ball speed as it leaves the
club head is the most important feature for predicting the cary distance of the
ball.

**Figure 4: Model Results**

![feature_importances](img/feature_importances.png)

---

## Conclusions

Golf ball carry distance can be reasonably predicted off the tee, e.g. ~6 m,
from initial conditions. The XGBoost Regressor was most effective and paints an
understandable picture that ball speed is most predictive of carry distance.

---

## Next Steps

* Add UI interaction declaring limiting feature of carry distance
* Feature creation
* Additional hyperparameter tuning
* Access raw data
* Comparision against other launch monitors
* Incorporate weather
