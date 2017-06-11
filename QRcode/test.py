import ugfx
import pyqrnative
# up to level 27 (125x125px) can be displayed
qr = pyqrnative.QRCode(2, pyqrnative.QRErrorCorrectLevel.Q)
qr.addData("https://sha2017.org/")
qr.make()
max_x = max_y = qr.getModuleCount()
matrix = qr.modules

disp_x, disp_y = (296, 128)
block_x = int(disp_x/max_x)
block_y = int(disp_y/max_y)

block_size = min(block_x, block_y)
offset_x = int(disp_x/2) - int(block_size*max_y/2)
offset_y = int(disp_y/2) - int(block_size*max_x/2)

ugfx.init()
ugfx.clear(ugfx.WHITE)
for y, row in enumerate(matrix):
    for x, col in enumerate(row):
        if qr.isDark(x, y):
            ugfx.area(offset_x+x*block_size, offset_y+y*block_size, block_size, block_size, ugfx.BLACK)
ugfx.flush()
