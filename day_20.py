from collections import defaultdict
from math import prod

import aoc_helper

raw = aoc_helper.fetch(20, year=2020)


def parse_raw():
    tiles = raw.split("\n\n")
    return dict(
        (int(tile.splitlines()[0][5:-1]), tile.splitlines()[1:]) for tile in tiles
    )


data = parse_raw()


def get_data():
    edges = defaultdict(set)
    neighbours = defaultdict(set)
    for id, tile in data.items():
        top_edge = tile[0]
        neighbours[id] |= edges[top_edge]
        for neighbour in edges[top_edge]:
            neighbours[neighbour].add(id)
        edges[top_edge].add(id)
        neighbours[id] |= edges[top_edge[::-1]]
        for neighbour in edges[top_edge[::-1]]:
            neighbours[neighbour].add(id)
        edges[top_edge[::-1]].add(id)

        bottom_edge = tile[-1]
        neighbours[id] |= edges[bottom_edge]
        for neighbour in edges[bottom_edge]:
            neighbours[neighbour].add(id)
        edges[bottom_edge].add(id)
        neighbours[id] |= edges[bottom_edge[::-1]]
        for neighbour in edges[bottom_edge[::-1]]:
            neighbours[neighbour].add(id)
        edges[bottom_edge[::-1]].add(id)

        left_edge = "".join(i[0] for i in tile)
        neighbours[id] |= edges[left_edge]
        for neighbour in edges[left_edge]:
            neighbours[neighbour].add(id)
        edges[left_edge].add(id)
        neighbours[id] |= edges[left_edge[::-1]]
        for neighbour in edges[left_edge[::-1]]:
            neighbours[neighbour].add(id)
        edges[left_edge[::-1]].add(id)

        right_edge = "".join(i[-1] for i in tile)
        neighbours[id] |= edges[right_edge]
        for neighbour in edges[right_edge]:
            neighbours[neighbour].add(id)
        edges[right_edge].add(id)
        neighbours[id] |= edges[right_edge[::-1]]
        for neighbour in edges[right_edge[::-1]]:
            neighbours[neighbour].add(id)
        edges[right_edge[::-1]].add(id)
    corners = [k for k, v in neighbours.items() if len(v) == 2]
    return edges, neighbours, corners


def get(set):
    return next(iter(set))


def part_one():
    edges, neighbours, corners = get_data()
    return prod(corners)


def flip_x(im):
    return [row[::-1] for row in im]


def flip_y(im):
    return im[::-1]


def rotate(im):
    return [[im[x][y] for x in range(len(im[0]))] for y in range(len(im))]


def monsters(im):
    monsters = 0
    hashes = "\n".join("".join(row) for row in im).count("#")
    for x in range(len(im[0]) - 18):
        for y in range(len(im[0]) - 2):
            if im[y][x : x + 20][18] != "#":
                continue
            if any(
                monster == "#" and image != monster
                for monster, image in zip("#    ##    ##    ###", im[y + 1][x : x + 20])
            ):
                continue
            if any(
                monster == "#" and image != monster
                for monster, image in zip(" #  #  #  #  #  #   ", im[y + 2][x : x + 20])
            ):
                continue
            monsters += 1
    return monsters, hashes - monsters * 15


def part_two():
    edges, neighbours, corners = get_data()
    rev_edges = defaultdict(set)
    for k, v in edges.items():
        for id in v:
            rev_edges[id].add(k)
    edge_tiles = len([k for k, v in neighbours.items() if len(v) == 3]) // 4
    all_values = set.union(*neighbours.values())
    grid = [
        [all_values.copy() for i in range(edge_tiles + 2)]
        for i in range(edge_tiles + 2)
    ]
    grid[0][0] = {corners[0]}
    grid[0][1] = {neighbours[corners[0]].pop()}
    grid[1][0] = neighbours[corners[0]]
    used = set.union(grid[0][0], grid[0][1], grid[1][0])
    while any(len(v) > 1 for row in grid for v in row):
        for y, row in enumerate(grid):
            for x, poss in enumerate(row):
                if len(poss) == 1:
                    continue
                poss -= used
                if x > 0:
                    poss &= set.union(*[neighbours[i] for i in row[x - 1]])
                if y > 0:
                    poss &= set.union(*[neighbours[i] for i in grid[y - 1][x]])
                if len(poss) == 1:
                    used |= poss
                    continue
    image = []
    for y in grid:
        l_idx = get(y[0])
        c_idx = get(y[1])
        shared_side = rev_edges[l_idx] & rev_edges[c_idx]
        tile = data[l_idx]
        top_edge = "".join(tile[0])
        bottom_edge = "".join(tile[-1])
        left_edge = "".join(i[0] for i in tile)
        right_edge = "".join(i[-1] for i in tile)
        if top_edge in shared_side:
            tile = flip_x(rotate(tile))
        if bottom_edge in shared_side:
            tile = rotate(tile)
        if left_edge in shared_side:
            tile = flip_x(tile)
        edge = "".join(i[-1] for i in tile)
        row = [tile]
        for last, current in zip(y, y[1:]):
            l_idx = get(last)
            c_idx = get(current)
            shared_side = rev_edges[l_idx] & rev_edges[c_idx]
            tile = data[c_idx]
            top_edge = "".join(tile[0])
            bottom_edge = "".join(tile[-1])
            left_edge = "".join(i[0] for i in tile)
            right_edge = "".join(i[-1] for i in tile)
            if top_edge in shared_side:
                tile = rotate(tile)
            if bottom_edge in shared_side:
                tile = flip_x(rotate(tile))
            if right_edge in shared_side:
                tile = flip_x(tile)
            my_edge = "".join(i[0] for i in tile)
            my_right_edge = "".join(i[-1] for i in tile)
            if my_edge == edge:
                row.append(tile)
                edge = my_right_edge
            else:
                row.append(tile[::-1])
                edge = my_right_edge[::-1]
        processed_row = [[] for i in row[0]]
        for tile in row:
            for prow, trow in zip(processed_row, tile):
                prow.extend(trow[1:-1])
        image.append(processed_row)
    processed_image = []
    c_top = "".join(image[0][0])
    c_bottom = "".join(image[0][-1])
    n_top = "".join(image[1][0])
    n_bottom = "".join(image[1][-1])
    if c_bottom in (n_top, n_bottom):
        processed_image.extend(image[0][1:-1])
        edge = c_bottom
    else:
        processed_image.extend(image[0][::-1][1:-1])
        edge = c_top
    for prev, current in zip(image, image[1:]):
        c_top = "".join(current[0])
        c_bottom = "".join(current[-1])
        if c_top == edge:
            processed_image.extend(current[1:-1])
            edge = c_bottom
        else:  # this doesn't work for malformed inputs but why should it
            processed_image.extend(flip_y(current)[1:-1])
            edge = c_top
    results = {}
    results[result[0]] = (result := monsters(processed_image))[1]
    results[result[0]] = (result := monsters(flip_y(processed_image)))[1]
    results[result[0]] = (result := monsters(flip_x(processed_image)))[1]
    results[result[0]] = (result := monsters(flip_x(flip_y(processed_image))))[1]
    results[result[0]] = (result := monsters(rotate(processed_image)))[1]
    results[result[0]] = (result := monsters(flip_y(rotate(processed_image))))[1]
    results[result[0]] = (result := monsters(flip_x(rotate(processed_image))))[1]
    results[result[0]] = (result := monsters(flip_x(flip_y(rotate(processed_image)))))[
        1
    ]
    return results[max(results)]


aoc_helper.lazy_submit(day=20, year=2020, solution=part_one)
aoc_helper.lazy_submit(day=20, year=2020, solution=part_two)
