text = "X-DSPAM-Confidence:    0.8475";
str = text.find(' ')
new = text[str:]
new = float(new)
print(new)#python
