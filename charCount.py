frame = []
frameLen = int(input("Enter the length of the frame: "))
newLen = frameLen + 1

for i in range(frameLen):
    framechar = input("Enter the character: ")
    frame.append(framechar)

frame.insert(0, str(newLen))

frame_str = ' '.join(frame)
print(frame_str)
