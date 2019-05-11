from PIL import Image


def build_mosaic(image, source_text, size):
    image = image.convert("L")          # convert to grayscale (ignore alpha)
    width, height = image.size
    scale_factor = size / max(width, height)
    aspect_ratio_correction = 0.46      # font dependent
    width = int(width * scale_factor)
    height = int(height * scale_factor * aspect_ratio_correction)

    image = image.resize((width, height))
    mosaic_grid = [[' ' for x in range(width)] for y in range(height)]

    text_index = 0

    threshold = 90
    for y in range(height):
        for x in range(width):
            value = image.getpixel((x, y))
            if value < threshold:
                mosaic_grid[y][x] = source_text[text_index]
                text_index = (text_index + 1) % len(source_text)

    return "\n".join(["".join(row) for row in mosaic_grid])


if __name__ == "__main__":
    image_filename = "evan.png"
    test_image = Image.open(image_filename)
    text = "I respect that.  "
    # text = "BONJOUR HOLA HALLO GUTEN TAG CIAO OLÀ NAMASTE SALAAM ZDRAS-TVUY-TE KONNICHIWA AHN-YOUNG-HA-SE-YO MERHABA SAIN BAINUU SZIA NI HAU"
    # text = "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible. Yellow, black. Yellow, black. Yellow, black. Yellow, black. Ooh, black and yellow! Let's shake it up a little. Barry! Breakfast is ready! Ooming! Hang on a second."
    # text = "Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal. Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this. But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth."

    mosaic = build_mosaic(test_image, text, 200)
    print(mosaic)
    file = open("mosaic_" + image_filename.split(".")[0] + ".txt", "w")
    file.write(mosaic)
