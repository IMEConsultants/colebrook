# colebrook.py

**Current Status:** Development

**Version:** 20190213

# TABLE OF CONTENTS

- [colebrook.py](#colebrookpy)
- [TABLE OF CONTENTS](#table-of-contents)
  - [TODO](#todo)
  - [DISCLAIMER](#disclaimer)
  - [BACKGROUND](#background)
  - [HOW TO USE](#how-to-use)
    - [USE AS MODULE](#use-as-module)
    - [USE AS STAND ALONE APPLICATION](#use-as-stand-alone-application)
  - [COLEBROOK-WHITE APPROXIMATIONS](#colebrook-white-approximations)
  - [REVISION HISTORY](#revision-history)

## TODO

- Add further approximation functions.
- Add warnings for parameters outside of the range for given formula.

## DISCLAIMER

**No guarantee of accuracy is provided, confirm results with other sources.**

## BACKGROUND

The Colebrook-White equation is used to solve for the [Darcy Friction Factor](https://en.wikipedia.org/wiki/Darcy_friction_factor_formulae) (f) for use in the determination of friction losses in pipe and open-channel flows.

The equation is expressed in terms of:

| Parameters | Description 
|---|---|
| [Reynolds Number](https://en.wikipedia.org/wiki/Reynolds_number) | A dimensionless value that describes the type of flow - As per | 
| Pipe Relative Roughness | A value which describes the roughness of the pipe material compared to its inner diameter. 

This module implements various approximations of the function for use in pipe flow calculations.

## HOW TO USE

### USE AS MODULE

Each approximation takes the Reynolds Number and Relative Roughness as required arguments, with the number of significant figures as an optional argument, in the format of ```function(reynolds, relative roughness, signficant figures)```

For example:

```python
    import colebrook
    factor = colebrook.sjFriction( 60000, 0.0023)
    print(factor)
```

Which outputs

```python
    0.027
```

### USE AS STAND ALONE APPLICATION

There is also limited ability to run the script from the command line. The script will run against all available functions.

```console
python colebrook.py <reynolds number> <roughness> [Optional Significant figures]
$ python colebrook.py 60000 0.0023
Ensure values are within range of applicability for equations (specifically around transition and laminar region)!
|METHOD          | VALUE  |
---------------------------
|sjFriction      | 0.027  |
|bntFriction     | 0.0203 |
|fngFriction     | 0.0267 |
|akFriction      | 0.0262 |
|bkcFriction     | 0.0271 |
|eptFriction     | 0.0269 |
DISCLAIMER: Use secondary verification. No guarantee of accuracy
```

## COLEBROOK-WHITE APPROXIMATIONS

The following functions are available in this module. They have been adapted from the Wikipedia [Darcy Friction Factor Formulae Table of Approximation](https://en.wikipedia.org/wiki/Darcy_friction_factor_formulae#Table_of_Approximations) page.

|FUNCTIONAME|AUTHOR|YEAR| VALIDITY RANGE|REF|
|-|-|-|-|-|
| sjFriction() | Swamee and Jain | 1976 | Re= 5000 to 10^8 and e/D = 0.00001 - 0.05| [Paper](https://cedb.asce.org/CEDBsearch/record.jsp?dockey=0006693) |
| btnFriction() | Bellos, Nalbantis, Tsarkris | 2018 | All Flow Regimes | [Paper](https://ascelibrary.org/doi/10.1061/%28ASCE%29HY.1943-7900.0001540) |
| fngFriction() | Fang et al. | 2011 |  R>=2300 | [Paper](https://www.sciencedirect.com/science/article/pii/S0029549311000173) |
| eptFriction() | Evangelides, Papaevangelou, Tzimopoulos | 2010 | R>=2300 | [Paper](http://blogs.sch.gr/geopapaevan/files/2010/07/full-paper_pre1128act.pdf) |
| akFriction() | Avci, Kargoz | 2009 |  R>=2300| [Paper](http://dx.doi.org/10.1115/1.3129132) |
| bkcFriction() | Brkic | 2011 |   R>=2300 | [Paper](https://doi.org/10.1080%2F10916461003620453) |

## REVISION HISTORY
| REVISION | DESCRIPTION |
| -- | -- |
| 20190213 | Initial Development Version |