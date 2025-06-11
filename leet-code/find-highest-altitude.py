from typing import List


def largestAltitude(gain: List[int]) -> int:
    altitudes: List = list()
    gain.insert(0, 0)
    altitude = 0

    for net_gain in gain:
        altitude += net_gain
        altitudes.append(altitude)

    return max(altitudes)


print(largestAltitude([-5, 1, 5, 0, -7]))
print(largestAltitude([0, -4, -7, -9, -10, -6, -3, -1]))
