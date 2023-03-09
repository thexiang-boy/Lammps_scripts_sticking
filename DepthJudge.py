import os
import numpy as np

# Define constants
A0 = 3.165
LENGTH_BOX = 46 * A0
LENGTH_TARGET = 30 * A0
LENGTH_BOTTOM = 10 * A0
LENGTH_UP = 16 * A0
PATH = "./coords/"

# Define functions with English comments
def get_file(path, file):
    """Load data from file and return as a numpy array"""
    position = os.path.join(path, file)
    return np.loadtxt(position)

def get_coord(data):
    """Get z coordinates from a numpy array"""
    return data[:, -1]

def get_coeff(final_coords):
    """Return a tuple of the number of reflect, stick, and channel atoms"""
    r = np.sum(final_coords > LENGTH_TARGET)
    s = np.sum((0 < final_coords) & (final_coords <= LENGTH_TARGET))
    c = np.sum(final_coords <= 0)
    return r, s, c

if __name__ == '__main__':
    # Get list of file names in directory
    files = sorted(os.listdir(PATH))

    # Initialize variables
    final_coords = np.empty(len(files))

    # Loop through files and get final z-coordinates
    for i, file in enumerate(files):
        data = get_file(PATH, file)
        coord_list = get_coord(data)
        final_coords[i] = coord_list[-1]

    # Print final z-coordinates and atom counts
    print(final_coords)
    r, s, c = get_coeff(final_coords)
    print("Energy = 80 eV")
    print(f"reflect = {r}, stick = {s}, channel = {c}")
