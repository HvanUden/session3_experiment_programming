from psychopy import visual, sound, core

window = visual.Window(size=(400, 400))

message = visual.TextStim(window) #always do this at the start of the experiment to minimize delays
image = visual.ImageStim(window, image="images/baby.png")

#note_c = sound.Sound("C", secs=1.0)
#note_g = sound.Sound("G", secs=1.0)
audio = sound.Sound("sounds/HF/baby.wav")

message.text = "Hello word!"
message.draw() #to control the timing
window.flip() #to control the timing: your screen runs at a certain refresh rate. but this makes sure all images (e.g.) are showed at the same time
#to remember: you draw on a screen. Only when you flip it, does the person on the other side see it. 
#note_c.play()
core.wait(1)

image.draw()
window.flip()
#note_g.play()
core.wait(1)

audio.play()
core.wait(2)





