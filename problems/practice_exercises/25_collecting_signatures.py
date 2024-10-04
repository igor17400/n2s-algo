from sys import stdin
from collections import namedtuple

Segment = namedtuple("Segment", "start end")


def optimal_points(segments):
    points = []

    # Sort segments by their end points 
    segments.sort(key=lambda x: x.end)

    current_point = None
    for segment in segments:
        if (
            current_point is None
            or current_point < segment.start
            or current_point > segment.end
        ):
            # Place the point at the end of the current segment
            # We want to save both the first point and the largest point that cuts
            # the biggeest amount of segments possible
            current_point = segment.end
            points.append(current_point)
    return points

# Example 1
segments = [Segment(1, 3), Segment(2, 5), Segment(3, 6)]
points = optimal_points(segments)
print(len(points))
print(points)

# Example 2
segments = [Segment(4, 7), Segment(1, 3), Segment(2, 5), Segment(5, 6)]
points = optimal_points(segments)
print(len(points))
print(points)
