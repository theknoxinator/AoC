# Determine the amount of wrapping paper and ribbon needed for packages
def parse_dimensions(dimensions):
    return list(map(int, dimensions.split('x')))


def part1(values):
    # Wrapping paper dimensions are given as height x width x depth
    # Surface area is calculated as each side plus smallest side once as extra area
    total_surface_area = 0
    for dimensions in values:
        height,width,depth = parse_dimensions(dimensions)
        height_width = height * width
        height_depth = height * depth
        width_depth = width * depth
        smallest_side = min(height_width, height_depth, width_depth)

        total_surface_area += 2 * height_width + 2 * height_depth + 2 * width_depth + smallest_side

    return total_surface_area


def part2(values):
    # Ribbon length is calculated as the shortest diameter plus total volume of box
    total_length = 0
    for dimensions in values:
        height,width,depth = parse_dimensions(dimensions)
        height_width_dia = 2 * height + 2 * width
        height_depth_dia = 2 * height + 2 * depth
        width_depth_dia = 2 * width + 2 * depth
        smallest_diameter = min(height_width_dia, height_depth_dia, width_depth_dia)

        total_length += smallest_diameter + height * width * depth

    return total_length
