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