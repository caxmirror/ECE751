import subprocess
import argparse
import os
import random
from sys import stdout
import numpy as np
import matplotlib.pyplot as plt


# Setup argument parser
parser = argparse.ArgumentParser(description="Parse data from files")
parser.add_argument("--delete_files", action='store_true', help="Set this flag to delete files after processing")

energy_calc = True

# Parse arguments
args = parser.parse_args()

average_jouels = 4000*14.8*3.6 #Value from paper https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8486942

energies_2D = []
energies_3D = []

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
    energy = 16.248*distance - 0.045

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

    
    term1 = 16.248*distance - 0.045
    
    if z1-z0 > 0:
        # Calculate total energy consumption
        energy = term1 + (315*altitude_change - 211.261)
    else:
        energy = term1 + (68.956*altitude_change - 65.183)
        
    return energy


if args.delete_files:
    try:
        os.remove("./confirmabletdmaSFTX_Z.dat")
        os.remove("./confirmabletdmaSFTX.dat")
    except Exception as e:
        print("File not found",e)
    
    
def run_script( val1, val2, val3, val4, val5,x=0,y=0):
    
    global energies_2D
    global energies_3D
    if energy_calc:
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
        energies_2D.append(energy)
        return x2,y2
    else:
        
        # Construct the command
        command = ['python3', f'FREEalpha=1.py', str(val1), str(val2), str(val3), str(val4), str(val5)]
        
        # Run the command
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout)
        print(result.stderr)
    
def run_script_zaxis( val1, val2, val3, val4, val5,x=0,y=0,z=0,maxHeight=5):
    
    global energies_2D
    global energies_3D
    if energy_calc:
        # Construct the command
        command = ['python3', f'FREE_Z.py', str(val1), str(val2), str(val3), str(val4), str(val5), str(x),str(y),str(z),str(maxHeight)]
        
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
        energies_3D.append(energy)
        
        print(f"3D Energy {energy}")
        
        return x2,y2,z2
    else:
        # Construct the command
        command = ['python3', f'FREE_Z.py', str(val1), str(val2), str(val3), str(val4), str(val5)]
        
        # Run the command
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout)
        print(result.stderr)

def main():
    global energies_2D
    global energies_3D
    # Define ranges for your variables (example ranges are used here)
    val1_range = range(2,100)
    val2_range = [64]
    val3_range = [600]
    val4_range = [1]
    val5_range = [5*i for i in range(1,20)]  # You can define your own ranges

    averages2d = []
    averages3d = []
    
    average_nodes = []
    average_nodes_2d = []
    # Loop over the ranges and run the script with each combination of values
    x,y,z = 0,0,0
    x2,y2 = 0,0
    
    for val5 in val5_range:                
        for val1 in val1_range:
            for val2 in val2_range:
                for val3 in val3_range:

    
                    if energy_calc: 
                        #Energy calculation mode
                        x2,y2 = run_script( 1, val2, val3, int(random.random()*10000), val5,x2,y2)
                        x,y,z = run_script_zaxis( 1, val2, val3, int(random.random()*10000), val5,x,y,z,val5)
                    else:
                        run_script( val1, val2, val3, 42, val5)
                        run_script_zaxis( val1, val2, val3, 42, val5)
                        
                        
        averages2d.append(np.mean(energies_2D))
        averages3d.append(np.mean(energies_3D))
        
        average_nodes.append((average_jouels)/(np.mean(energies_3D)*2))
        average_nodes_2d.append((average_jouels)/(np.mean(energies_2D)*2))
        
        
        energies_2D = []
        energies_3D = []
                
    num_averages = len(averages2d)
    x = range(num_averages)
    
    # Assuming some sample data for demonstration purposes
    # Plotting the bar chart with larger figures
    plt.figure(figsize=(10, 6))  # Increased figure size
    x = np.arange(len(val5_range))
    plt.bar(x - 0.2, averages2d, width=0.4, label='2D Averages', align='center')
    plt.bar(x + 0.2, averages3d, width=0.4, label='3D Averages', align='center')

    plt.xlabel('Different Averages')
    plt.ylabel('Average Energy Consumption')
    plt.title('Comparison of Multiple Average Energy Consumptions in 2D and 3D')
    plt.legend()
    plt.xticks(x, [f'0-{i}' for i in val5_range])
    plt.tight_layout()
    plt.savefig("./figures/average_energy.png")
    plt.clf()

    # Plotting the line chart with larger figures
    plt.figure(figsize=(10, 6))  # Increased figure size
    plt.plot(range(len(val5_range)), average_nodes, label="3D")
    plt.plot(range(len(val5_range)), average_nodes_2d, label="2D")

    plt.xlabel('Z-Axis Range')
    plt.ylabel('Average Number of Nodes Reachable')
    plt.title('Comparison of Reachable Nodes in 2D and 3D')
    plt.xticks(x, [f'0-{i}' for i in val5_range])
    plt.tight_layout()
    plt.savefig("./figures/average_reachable_nodes.png")
    plt.clf()
        


if __name__ == "__main__":
    main()
