Hi Joe!
Jon noticed that our I2C pull up resistors on the Wagons for the Hexaboard setup were too large. I have replaced them, as per his recommendation, from 200kOhms to 1kOhm resistors. Now I am checking the system again. I am seeing that the hexacontroller on the east side of the engine is setup properly and the clkSource output looks as expected (without errors, notably: ROC err:  0 0 0). But for the hexacontroller on the west side of the engine I am getting ROC errors when I run the clkSource script (ROC err:  1 0 1). Do you know how I can investigate these ROC errors further?


