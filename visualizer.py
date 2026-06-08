import matplotlib.pyplot as plt


class Visualizer:

    def preview_pattern(self, stitches, title="Embroidery Pattern"):

        xs = []
        ys = []
        colors = []

        sizes = []

        for stitch in stitches:

            xs.append(stitch["x"])
            ys.append(stitch["y"])

            r, g, b = stitch["color"]


            colors.append([r/255, g/255, b/255])#because matplot not under stand 255 and so  on

            if stitch["type"] == "fill":
                sizes.append(8)

            else:
                sizes.append(12)

        fig, ax = plt.subplots(figsize=(8, 8))

        ax.scatter(xs, ys, c=colors, s=sizes, marker=".")


        ax.invert_yaxis()
        ax.set_facecolor("#f5f0e8")




        ax.set_title(title)
        ax.set_xlabel("X (mm)")#as matlab x-label
        ax.set_ylabel("Y (mm)")

        plt.show()

    def compare_original_and_pattern(self, original_image, stitches):#not required construc.


        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

        ax1.imshow(original_image)


        xs = []
        ys = []
        colors = []
        sizes = []

        for stitch in stitches:

            xs.append(stitch["x"])
            ys.append(stitch["y"])

            r, g, b = stitch["color"]
            colors.append([r / 255, g / 255, b / 255])

            if stitch["type"] == "fill":
                sizes.append(8)#small size 
            else:

                sizes.append(12)
        ax2.scatter(xs, ys, c=colors, s=sizes, marker=".")

        ax2.invert_yaxis()


        ax2.set_facecolor("#f5f0e8")



        fig.suptitle("Smart Mini Embroidery Machine — Pattern Preview")

        plt.show()



    def show_thread_colors(self, colors):
        

        fig, ax = plt.subplots(figsize=(8, 2))#return tow value figure and axes .fig dont care


        for i, color in enumerate(colors):

            r, g, b = color

            rect = plt.Rectangle(
                (i, 0),1,1,

                color=[r / 255, g / 255, b / 255]
            )

            ax.add_patch(rect)


            hex_color = f"#{r:02X}{g:02X}{b:02X}"

            ax.text(i + 0.1, -0.2, hex_color)


        ax.set_xlim(0, len(colors))
        ax.set_ylim(-0.5, 1)

        ax.axis("off")

        plt.show()