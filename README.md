# strawberry-maturation-detection
Image processing implementation for segmenting strawberry from background and detecting the matured strawberry with color coding

## Image processing method
Background segmentation using binary thresholding, morphology manipulation (dilation and erotion) and masking on choosed 1 color channel
Color coding to desired color based on RGB values of the input image 

## Color Coding
|Maturation phase       |Color Code |
|-----------------------|-----------|
|Immature (Green)       | Yellow    |
|Half matured (White)   | Orange    |
|Almost matured (Orange)| Purple    |
|Matured (Red)          | Blue      |

## Input-Output images
<p align="center">Input 1</p>
<p align="center">
  <img src="https://github.com/wildanfajri1alfarabi/strawberry-maturation-detection/blob/main/images/strawberry%20in1.JPG" width="480" title="BotaRun">
</p>

<p align="center">Output 1</p>
<p align="center">
  <img src="https://github.com/wildanfajri1alfarabi/strawberry-maturation-detection/blob/main/images/strawberry%20out1.JPG" width="480" title="BotaRun">
</p>

<p align="center">Input 2</p>
<p align="center">
  <img src="https://github.com/wildanfajri1alfarabi/strawberry-maturation-detection/blob/main/images/strawberry%20in2.jpg" width="480" title="BotaRun">
</p>

<p align="center">Output 2</p>
<p align="center">
  <img src="https://github.com/wildanfajri1alfarabi/strawberry-maturation-detection/blob/main/images/strawberry%20out2.JPG" width="480" title="BotaRun">
</p>

<p align="center">Input 3</p>
<p align="center">
  <img src="https://github.com/wildanfajri1alfarabi/strawberry-maturation-detection/blob/main/images/strawberry%20in3.jpg" width="480" title="BotaRun">
</p>

<p align="center">Output 3</p>
<p align="center">
  <img src="https://github.com/wildanfajri1alfarabi/strawberry-maturation-detection/blob/main/images/strawberry%20out3.JPG" width="480" title="BotaRun">
</p>
