import math
import stdio
import sys
from blob_finder import BlobFinder
from picture import Picture


# Entry point
def main():
    # Accept command-line arguments pixels (int), tau (float), and delta (float).
    pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])
    frames = sys.argv[4:]

    # Construct a BlobFinder object for the frame sys.argv[4]
    # From it get a list of beads prevBeads that have at least pixels
    blob_find = BlobFinder(Picture(frames[0]), tau)
    prev_Beads = blob_find.getBeads(pixels)

    # Construct a BlobFinder object
    # From it get a list of beads currBeads that have at least pixels.
    for i in range(1, len(frames)):
        blob_find = BlobFinder(Picture(frames[i]), tau)
        curr_beads = blob_find.getBeads(pixels)
        # For each bead currBead in currBeads,
        for curr_bead in curr_beads:
            dist = math.inf
            # find a bead prevBead from prevBeads
            # that is no further than delta and is closest to currBead
            for prev_bead in prev_Beads:
                bead = curr_bead.distanceTo(prev_bead)
                if bead <= delta and bead < dist:
                    dist = bead
            # if such a bead is found, write its distance to currBead.
            if dist != math.inf:
                stdio.writef('%.4f\n', dist)
        # Write a newline character.
        stdio.writeln()
        # Set prevBeads to currBeads.
        prev_Beads = curr_beads


if __name__ == '__main__':
    main()
