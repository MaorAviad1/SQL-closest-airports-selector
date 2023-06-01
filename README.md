# Closest Airports Selector

## Description

The "closest-airports-selector.py" script calculates and returns the five nearest airports from a specified latitude and longitude. This script is specifically designed to operate with databases where coordinates are stored as varchar.

## Prerequisites

Before you begin, ensure you have met the following requirements:

-   You have installed the latest version of Python.
-   You have a MySQL database named `navigation_data`, with table `navdata` that includes airport data.
-   You have a MySQL server running and accessible.

## Using Closest Airports Selector

To use the script, follow these steps:

1.  Clone the repository to your local machine.
2.  Navigate to the directory where the script is located.
3.  Run the script from the command line with the following syntax:

cssCopy code

`python closest-airports-selector.py --lat [LATITUDE] --lon [LONGITUDE]` 

Replace `[LATITUDE]` and `[LONGITUDE]` with the decimal values of the coordinates from which you want to find the nearest airports.
