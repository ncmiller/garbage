def get_layers(digits, w, h):
    layersize = w * h
    layers = []
    while digits:
        layers.append(digits[:layersize])
        digits = digits[layersize:]
    return layers

def part1(chars):
    layers = get_layers(chars, 25, 6)

    min_zeros = 25*6
    min_layer = layers[0]
    for layer in layers:
        num_zeros = sum([1 for d in layer if d == '0'])
        if num_zeros < min_zeros:
            min_zeros = num_zeros
            min_layer = layer

    num_ones = sum([1 for d in min_layer if d == '1'])
    num_twos = sum([1 for d in min_layer if d == '2'])
    print(num_ones * num_twos)

def render(image, w, h):
    rows = get_layers(image, w, 1)
    for row in rows:
        row_str = ""
        for c in row:
            if c == '0':
                c = ' '
            row_str += c
        print row_str

def part2(chars):
    w, h = (25, 6)
    layers = get_layers(chars, w, h)
    image = ""
    for i in range(len(layers[0])):
        pixel = 2
        for j in range(len(layers)):
            if layers[j][i] != '2':
                pixel = layers[j][i]
                break
        image += pixel
    render(image, w, h)

with open("day8_input.txt") as f:
    chars = f.read().rstrip()
# chars = "0222112222120000"

part1(chars)
part2(chars)
