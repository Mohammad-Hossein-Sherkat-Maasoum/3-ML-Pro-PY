#3-ML-Pro-PY
import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])

# تغییر شکل آرایه به یک ماتریس دو بعدی 2x3
b = a.reshape((2, 3))
print(a)
print(b)
# تبدیل آرایه به لیست
c = a.tolist()
print(c)