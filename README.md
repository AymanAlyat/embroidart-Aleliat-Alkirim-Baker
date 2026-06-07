# EmbroidArt — Embroidery Pattern Generator

**Course:** Python Programming

## Group Members

- Ahmed Mohammed Fakhri AlKirim — 202110545
- Mohammed Awni Mustafa Baker — 201912050
- Ayman Faeq Taher Aleliat — 202211286

---

## Project Description

EmbroidArt is a Python CLI application that convert images into embroidery stitch pattern. It use Pillow and OpenCV for image processing, NumPy for array operation, and Matplotlib for visualization. The system generate stitch coordinate that can be used by a Smart Mini Embroidery Machine to recreate design on fabric.

---

## Installation

Install all required libraries:

```bash
pip install -r requirements.txt
```

---



## How to Run



### Generate embroidery pattern

```bash
python main.py generate test_flower.png --colors 6 --compare --output pattern.json
```

### Preview saved pattern

```bash
python main.py preview pattern.json
```



----

## GitHub Repository

https://github.com/AymanAlyat/embroidart-Aleliat-Alkirim-Baker.git