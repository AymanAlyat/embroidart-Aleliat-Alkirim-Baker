import numpy as np


class PatternGenerator:

    def edges_to_stitches(self, edge_map: np.ndarray, stitch_gap: int = 2) -> list:
        stitches = []

        ys, xs = np.where(edge_map > 0)

        for x, y in zip(xs[::stitch_gap], ys[::stitch_gap]):
            stitches.append({
                "x": int(x),
                "y": int(y),
                "color": [0, 0, 0],
                "type": "outline"
            })

        return stitches
    
    def fill_to_stitches(self, index_map: np.ndarray, colors: list, stitch_gap: int = 3) -> list:
        stitches = []

        for color_idx, color in enumerate(colors):
            mask = (index_map == color_idx)

            ys, xs = np.where(mask)

            for x, y in zip(xs[::stitch_gap], ys[::stitch_gap]):
                stitches.append({
                    "x": int(x),
                    "y": int(y),
                    "color": list(color),
                    "type": "fill"
                })

        return stitches
    
    def generate_pattern(self, edge_map, index_map, colors) -> list:
        outline_stitches = self.edges_to_stitches(edge_map)

        fill_stitches = self.fill_to_stitches(
            index_map,
            colors
        )

        pattern = fill_stitches + outline_stitches

        print(f"Total stitches: {len(pattern)}")

        return pattern