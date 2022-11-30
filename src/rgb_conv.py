def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb
rgb_to_hex((255, 255, 195))

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3))
hex_to_rgb("FF65BA")

if __name__ == '__main__':
    rgb_vals = [
        (210,238,250),
        (255,255,255),
        (82,181,236)
    ]

    for val in rgb_vals:
        print('RGB: {}\t Hex: {}'.format(val, rgb_to_hex(val)))

# Output
#RGB: (210, 238, 250)     Hex: d2eefa
#RGB: (255, 255, 255)     Hex: ffffff
#RGB: (82, 181, 236)      Hex: 52b5ec