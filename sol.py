import sys

# read ext file info, manipulate canvas, and print results.
def ascii_input(external_file):
  f = open(external_file)
  size = f.readline() # obtain the size parameters for the canvas (infinitely large grid with rectangle filled with periods).
  size = size.split(' ')
  if not size[0].isdigit() or not size[1].isdigit():
    print("Error. One or both of the canvas size parameters specified in the .tvg file are not integers. Please fix and try again.")
    return
  length = int(size[0]) # [vertical size]
  width = int(size[1])  # [horizontal size]
  canvas = []
  i = 0
  j = 0
  # fill 2D array with period characters
  while i < length:
    canvas.append([])
    while j < width:
      canvas[i].append('.')
      j = j + 1
    i = i + 1
    j = 0

#  print(str(width) + ' ' + str(length))
#  print(canvas)

  command = f.readline()
  while command:
    command = command.split(' ')
    #print(command)
    char_to_write = command[0]
    row = int(command[1])
    column = int(command[2])
    hORz = command[3] == 'h'  # hORz = a boolean value --true if horizontal, false otherwise
    line_length = int(command[4])
    
    k = 0  # for keeping track of how many times we have written a character
    if hORz == True:
      j = column
      if column >= 0:
        while j < width and k < line_length:
          canvas[row][j] = char_to_write  # if we are writing horizontally, keep the row value constant
          j += 1
          k += 1
        k = 0
      else:  # if the coordinate is less than zero, we just start from zero and write onwards instead as
             # a negative coordinate is just outside of our editing bounds.
        j = 0
        while j < width and k < line_length:
          canvas[row][j] = char_to_write
          j += 1
          k += 1
        k = 0
    elif hORz == False:
      i = row
      if row >= 0:
        while i < length and k < line_length:
          canvas[i][column] = char_to_write  # if we are writing vertically, keep the row value constant
          i += 1
          k += 1
        k = 0
      else:
        i = 0
        while i < length and k < line_length:
          canvas[i][column] = char_to_write
          i += 1
          k += 1
        k = 0
#    print(canvas)
    command = f.readline()
  i = 0
  j = 0
  while i < length:
    j = 0
    while j < width:
      print(canvas[i][j], end="")
      j += 1
    print()
    i += 1

# main function (first function called)
def main(external_file):
  if len(sys.argv) < 2:
    print("Error. Not enough arguments")
    return
  ascii_input(external_file[1])

if __name__ == '__main__':
    main(sys.argv)
