frame = []
frameLen = int(input("Enter the length of the frame: "))
newLen = frameLen + 1

for i in range(frameLen):
    framechar = input("Enter the character: ")
    frame.append(framechar)

if 'z' in frame:
    zIndex = frame.index("z")
    frame.insert(zIndex, '$')

if 'y' in frame:
    yIndex = frame.index("y")
    frame.insert(yIndex, '$')

frame.insert(0, 'y')
frame.insert(len(frame)+1, 'z')

frame_str = ' '.join(frame)
print("\nYour frame start after y and ends before z:")
print(frame_str)