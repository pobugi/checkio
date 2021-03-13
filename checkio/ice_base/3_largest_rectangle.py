"""
You have a histogram. Try to find the size of the biggest rectangle you can build out of the histogram bars.
https://www.geeksforgeeks.org/largest-rectangle-under-histogram/
"""


def largest_histogram(histogram):
    max_s = max(histogram)
    max_s = max(max_s, len(histogram))
    for i in range(1, len(histogram)):
        s = min(histogram[i], histogram[i-1]) * 2
        if s > max_s:
            max_s = s
    return max_s


if __name__ == "__main__":
    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print("Done! Go check it!")
