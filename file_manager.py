import json


class FileManager:

    def save_json(self, stitches: list, filepath: str):

        data = {
            "machine": "Smart Mini Embroidery Machine",
            "total_stitches": len(stitches),
            "stitches": stitches
        }

        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)

        print(
            f"Pattern saved to {filepath} ({len(stitches)} stitches)"
        )