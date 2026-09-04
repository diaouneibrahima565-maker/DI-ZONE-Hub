# Required Libraries
import math
import tkinter as tk

# Hexagon Geometry
def calculate_hexagon_points(center_x, center_y, radius, rotation):
    POINTS = []

    for vertex in range(6):
        angle_degree = rotation + (vertex * 60)
        angle_radians = math.radians(angle_degree)

        cos_radians = math.cos(angle_radians)
        sin_radians = math.sin(angle_radians)

        horizontal_offset = radius * cos_radians
        vertical_offset = radius * sin_radians

        x = center_x + horizontal_offset
        y = center_y + vertical_offset

        POINTS.append(x)
        POINTS.append(y)

    return POINTS

# Draw Hexagon
def draw_hexagon(surface, center_x, center_y, radius, rotation, outline, line_width):
    points = calculate_hexagon_points(center_x, center_y, radius, rotation)

    polygon = surface.create_polygon(*points, fill = "",outline = outline, width = line_width)

    return polygon

# Logo Dimensions
def calculate_logo_dimensions(width, height):
    center_x = width / 2
    center_y = height / 2

    logo_size = min(width, height)

    outer_radius = 0.40 * logo_size

    inner_radius = 0.31 * logo_size

    return center_x, center_y, logo_size, outer_radius, inner_radius

# Draw 2 Hexagons
def draw_hub_frame(surface, width, height):
    