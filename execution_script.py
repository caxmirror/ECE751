import subprocess
import argparse
import os
import random
from sys import stdout

# Setup argument parser
parser = argparse.ArgumentParser(description="Parse data from files")
parser.add_argument("--delete_files", action='store_true', help="Set this flag to delete files after processing")

# Parse arguments
args = parser.parse_args()

DISTANCE_RATE = 50#From online google of average distance rate for real drones
ALTITUDE_RATE = 80#Paper An overview of drone energy consumption factors and models.

def calculate_drone_energy_2d(x0, y0, x1, y1, distance_rate):
    """
    Calculate the energy expenditure of a drone moving from one point to another in 2D space.

    Parameters:
    x0, y0: Initial coordinates (old inputs) in 2D space.
    x1, y1: Final coordinates (current outputs from the script) in 2D space.
    distance_rate: Energy consumption rate per unit distance (Joules/meter).

    Returns:
    Total energy expended (Joules).
    """
    # Calculate the Euclidean distance between the two points in 2D
    distance = ((x1 - x0)**2 + (y1 - y0)**2)**0.5

    # Calculate total energy consumption
    energy = distance_rate * distance

    return energy

def calculate_drone_energy(x0, y0, z0, x1, y1, z1, distance_rate, altitude_rate):
    """
    Calculate the energy expenditure of a drone moving from one point to another.

    Parameters:
    x0, y0, z0: Initial coordinates (old inputs).
    x1, y1, z1: Final coordinates (current outputs from the script).
    distance_rate: Energy consumption rate per unit distance (Joules/meter).
    altitude_rate: Additional energy consumption rate per unit of altitude change (Joules/meter).

    Returns:
    Total energy expended (Joules).
    """
    # Calculate the Euclidean distance between the two points
    distance = ((x1 - x0)**2 + (y1 - y0)**2 + (z1 - z0)**2)**0.5

    # Calculate the altitude change
    altitude_change = abs(z1 - z0)

    if z1-z0 > 0:
        # Calculate total energy consumption
        energy = distance_rate * distance + altitude_rate * altitude_change
    else:
        energy = distance_rate * distance + altitude_rate * altitude_change * 0.5 #accounting for gravity making it easier to go down rather than up.
        
    return energy


if args.delete_files:
    try:
        os.remove("./confirmabletdmaSFTX_Z.dat")
        os.remove("./confirmabletdmaSFTX.dat")
    except Exception as e:
        print("File not found",e)
    
    
def run_script( val1, val2, val3, val4, val5,x=0,y=0):
    # Construct the command
    command = ['python3', f'FREEalpha=1.py', str(val1), str(val2), str(val3), str(val4), str(val5),str(x),str(y)]
    
    # Run the command
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


    for line in result.stdout.split("\n"):
        if "X:" in line:
            x2,y2 = line.split("\t")
            x2 = float(x2.split(":")[1])
            y2 = float(y2.split(":")[1])
    
    # You can process the result here (e.g., print or log it)
    # print(result.stdout)
    # print(result.stderr)
    print(x,y)
    energy = calculate_drone_energy_2d(x,y,x2,y2,DISTANCE_RATE)
    print(f"2D Energy {energy}")
    return x2,y2
    
def run_script_zaxis( val1, val2, val3, val4, val5,x=0,y=0,z=0):
    # Construct the command
    command = ['python3', f'FREE_Z.py', str(val1), str(val2), str(val3), str(val4), str(val5), str(x),str(y),str(z)]
    
    # Run the command
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # You can process the result here (e.g., print or log it)
    # print(result.stdout)
    # print(result.stderr)
    
    
    for line in result.stdout.split("\n"):
        if "X:" in line:
            x2,y2,z2 = line.split("\t")
            x2 = float(x2.split(":")[1])
            y2 = float(y2.split(":")[1])
            z2 = float(z2.split(":")[1])
    
    energy = calculate_drone_energy(x,y,z,x2,y2,z2,DISTANCE_RATE,ALTITUDE_RATE)
    
    print(f"3D Energy {energy}")
    
    return x2,y2,z2

def main():
    # Define ranges for your variables (example ranges are used here)
    val1_range = range(2,100)
    val2_range = [64]
    val3_range = [600]
    val4_range = [1]
    val5_range = [88]  # You can define your own ranges

    # Loop over the ranges and run the script with each combination of values
    x,y,z = 0,0,0
    x2,y2 = 0,0
    for val1 in val1_range:
        for val2 in val2_range:
            for val3 in val3_range:

                for val5 in val5_range:
                    x2,y2 = run_script( 1, val2, val3, int(random.random()*10000), val5,x2,y2)
                    x,y,z = run_script_zaxis( 1, val2, val3, int(random.random()*10000), val5,x,y,z)
                    

if __name__ == "__main__":
    main()
