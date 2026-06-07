import json
import csv


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
    def load_json(self, filepath: str) -> list:
        with open(filepath, "r") as f:
            data = json.load(f)

        stitches = data["stitches"]

        print(f"Loaded {len(stitches)} stitches from {filepath}")

        return stitches

    def save_csv(self, stitches: list, filepath: str):
        fieldnames = ["x", "y", "color", "type"]

        with open(filepath, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()

            for stitch in stitches:
                row = stitch.copy()
                row["color"] = str(row["color"])

                writer.writerow(row)

        print(f"Pattern saved to {filepath} ({len(stitches)} stitches)")