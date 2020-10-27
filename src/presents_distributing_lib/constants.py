# Time an elf takes to wrap a present
WEIGHT_TO_WRAPPING_TIME = {
    1: .5,
    2: 1,
    5: 2,
}

PRESENT_SIZES = sorted(list(WEIGHT_TO_WRAPPING_TIME.keys()))
# The dependency is added so whenever present weight need to be added, we make sure it is added to both elements

DEFAULT_MAX_CAPACITY = 12
