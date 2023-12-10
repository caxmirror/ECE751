import subprocess
import argparse
import os

# Setup argument parser
parser = argparse.ArgumentParser(description="Parse data from files")
parser.add_argument("--delete_files", action='store_true', help="Set this flag to delete files after processing")

# Parse arguments
args = parser.parse_args()

if args.delete_files:
    try:
        os.remove("./confirmabletdmaSFTX_Z.dat")
    except Exception as e:
        print("File not found",e)
    
    os.remove("./confirmabletdmaSFTX.dat")
    
def run_script( val1, val2, val3, val4, val5):
    # Construct the command
    command = ['python3', f'FREEalpha=1.py', str(val1), str(val2), str(val3), str(val4), str(val5)]
    
    # Run the command
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # You can process the result here (e.g., print or log it)
    print(result.stdout)
    print(result.stderr)
    
def run_script_zaxis( val1, val2, val3, val4, val5):
    # Construct the command
    command = ['python3', f'FREE_Z.py', str(val1), str(val2), str(val3), str(val4), str(val5)]
    
    # Run the command
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # You can process the result here (e.g., print or log it)
    print(result.stdout)
    print(result.stderr)


def main():
    # Define ranges for your variables (example ranges are used here)
    val1_range = range(2,100)
    val2_range = [64]
    val3_range = [600]
    val4_range = [1]
    val5_range = [88]  # You can define your own ranges

    # Loop over the ranges and run the script with each combination of values
   
    for val1 in val1_range:
        for val2 in val2_range:
            for val3 in val3_range:
                for val4 in val4_range:
                    for val5 in val5_range:
                        run_script( val1, val2, val3, val4, val5)
                        run_script_zaxis( val1, val2, val3, val4, val5)
                        

if __name__ == "__main__":
    main()
