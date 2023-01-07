# Goodwin-Griffith-genetic-oscillator-model

I. Kontrola genów Model zaproponowany przez Griffitha, w którym X to koncentracja pewnego białka proporcjonalna do
aktywności opisywanego genu, a Y to koncentracja odpowiedniego mRNA,

$$\dot{X} = -\alfa X+Y$$
$$\dot{Y} = \frac{x^2}{1+X^2}-\beta Y$$

parametry alfa i beta dodatnie

zrudla:
https://www.researchgate.net/figure/Goodwin-Griffith-genetic-oscillator-model-The-transcription-factor-TF-gene-A-is_fig2_262381116

wnioski z artykułu warunki poczatkowe:
X_a,Z_a,M_a,P_a = 0 i tau = 0 oraz V_a = 0 sigma_a = 0 i K_a = 0

Obliczenie pkt stabilnych:
https://www.wolframalpha.com/input?i2d=true&i=-%CE%B1x%2By+%3D+0%5C%2844%29+Divide%5BPower%5Bx%2C2%5D%2C1%2BPower%5Bx%2C2%5D%5D-%CE%B2y+%3D+0

https://www.wolframalpha.com/input?i2d=true&i=-%CE%B1x%2By+%3D+0%5C%2844%29+Divide%5BPower%5Bx%2C2%5D%2C1%2BPower%5Bx%2C2%5D%5D-%CE%B2y+%3D+0+solve+for+x%5C%2844%29y