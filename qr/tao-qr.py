"""Tạo hình nền điện thoại có mã QR hình trái tim.

Cách dùng:
    python tao-qr.py https://ten-mien-cua-ban.com
    python tao-qr.py https://ten-mien-cua-ban.com -o hinh-nen.png --mau "#2a2426"
"""
import argparse, random, sys
import cv2, numpy as np
from PIL import Image, ImageDraw

ap = argparse.ArgumentParser(description="Tạo hình nền QR trái tim")
ap.add_argument("url", help="Đường link website của bạn")
ap.add_argument("-o", "--out", default="hinh-nen-qr-trai-tim.png", help="Tên file ảnh xuất ra")
ap.add_argument("--rong", type=int, default=1179, help="Chiều rộng ảnh (px), mặc định 1179 (iPhone)")
ap.add_argument("--cao", type=int, default=2556, help="Chiều cao ảnh (px), mặc định 2556 (iPhone)")
ap.add_argument("--mau", default="#282426", help="Màu chấm, mặc định gần đen (nên giữ màu đậm để dễ quét)")
ap.add_argument("--nen", default="#ffffff", help="Màu nền, mặc định trắng")
ap.add_argument("--seed", type=int, default=2010, help="Đổi số này để có kiểu rải chấm khác")
a = ap.parse_args()

# 1) Mã hoá QR (mức sửa lỗi Q)
pp = cv2.QRCodeEncoder_Params()
pp.correction_level = cv2.QRCodeEncoder_CORRECT_LEVEL_Q
raw = cv2.QRCodeEncoder.create(pp).encode(a.url)
ys, xs = np.where(raw < 128)
raw = raw[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
M = (raw < 128).tolist()
n = len(M)

W, H, SS = a.rong, a.cao, 2
img = Image.new("RGB", (W * SS, H * SS), a.nen)
d = ImageDraw.Draw(img)

def inheart(x, y):
    return (x * x + y * y - 1) ** 3 - x * x * y ** 3 <= 0

cells = n + 4  # QR + vùng trống 2 ô mỗi bên
G = max(76, int(cells * 2.05))
pitch = W * 0.8 / G
cx0, cy0 = W / 2, H * 0.56

def toheart(i, j):
    return (i - G / 2 + .5) / (G / 2) * 1.2, -(j - G / 2 + .5) / (G / 2) * 1.2 + 0.15

q0 = G // 2 - cells // 2
q1 = q0 + cells
ok = [r for r in range(G - cells)
      if all(inheart(*toheart(i, j)) for i in range(q0 - 1, q1 + 1) for j in range(r - 1, r + cells + 1))]
if not ok:
    sys.exit("Link quá dài, mã QR không vừa trong trái tim. Hãy dùng link ngắn hơn.")
r0 = ok[len(ok) // 2]
r1 = r0 + cells

ink = a.mau
def dot(i, j, f=0.82):
    x = (cx0 + (i - G / 2) * pitch) * SS; y = (cy0 + (j - G / 2) * pitch) * SS; s = pitch * SS
    m = s * (1 - f) / 2
    d.ellipse([x + m, y + m, x + s - m, y + s - m], fill=ink)
def sq(i, j):
    x = (cx0 + (i - G / 2) * pitch) * SS; y = (cy0 + (j - G / 2) * pitch) * SS; s = pitch * SS
    d.rounded_rectangle([x, y, x + s + .5, y + s + .5], radius=s * .12, fill=ink)

# 2) Rải chấm ngẫu nhiên tạo hình trái tim
random.seed(a.seed)
for i in range(G):
    for j in range(G):
        if q0 <= i < q1 and r0 <= j < r1:
            continue
        if inheart(*toheart(i, j)) and random.random() < 0.5:
            dot(i, j)

# 3) Vẽ mã QR ở giữa
for x in range(n):
    for y in range(n):
        if M[y][x]:
            finder = (x < 7 and y < 7) or (x >= n - 7 and y < 7) or (x < 7 and y >= n - 7)
            if finder: sq(q0 + 2 + x, r0 + 2 + y)
            else: dot(q0 + 2 + x, r0 + 2 + y, 0.92)

img = img.resize((W, H), Image.LANCZOS)
img.save(a.out)

# 4) Tự kiểm tra: quét thử ảnh vừa tạo
check = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
small = cv2.resize(check, None, fx=0.35, fy=0.35, interpolation=cv2.INTER_AREA)
got = cv2.QRCodeDetector().detectAndDecode(small)[0]
print(f"Đã lưu: {a.out}")
print("Quét thử:", "OK ✓" if got == a.url else f"KHÔNG đọc được (đọc ra: {got!r}) — thử màu chấm đậm hơn hoặc link ngắn hơn")
