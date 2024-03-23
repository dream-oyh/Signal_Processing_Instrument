import logging

import cv2

from ui.app import APP

logging.basicConfig(level=logging.INFO)


app = APP()
app.title("Signal Processing Instrument")
app.geometry("2560x1600")
app.state("zoomed")
try:
    app.mainloop()
finally:
    cv2.destroyAllWindows()
    logging.info("程序结束")
    exit(0)
