# Thư 20/10 💌

Website tặng quà 20/10. Người nhận quét mã QR hình trái tim trên hình nền điện thoại, trang web mở ra một phong bì hồng. Chạm vào phong bì thì thiệp "Happy Womenday 20/10" bật lên cùng hoa, sau đó chuyển sang lá thư tự cuộn kèm ảnh polaroid. Nền có cánh hoa hồng, trái tim rơi và bay lên.

- Chỉ có **1 file HTML**, không cần Node.js, không cần build, không cần server riêng.
- Chạy tốt trên điện thoại (iPhone/Android) và máy tính.
- Font chữ tải từ Google Fonts, cần có mạng Internet khi xem.

---

## 1. Cấu trúc thư mục

```
thu-20-10-source/
├── index.html          ← toàn bộ website (HTML + CSS + JS)
├── images/             ← để ảnh của bạn vào đây
├── qr/
│   ├── tao-qr.py       ← script tạo hình nền QR trái tim
│   └── requirements.txt
└── README.md
```

---

## 2. Xem thử trên máy

Cách nhanh nhất là mở file `index.html` bằng trình duyệt (nhấp đúp vào file).

Để xem thử trên điện thoại cùng mạng Wi-Fi, chạy một server đơn giản trong thư mục này:

```bash
# Cần Python 3
python -m http.server 8000
```

Sau đó mở `http://localhost:8000` trên máy tính. Trên điện thoại, mở `http://<IP-máy-tính>:8000`, ví dụ `http://192.168.1.10:8000`.

---

## 3. Sửa nội dung

Mở `index.html` bằng trình soạn thảo bất kỳ (VS Code, Notepad++…) và tìm đoạn `/* ======= NỘI DUNG — sửa ở đây ======= */`:

```js
const THU = {
  loiChao: "Em yêu của anh,",
  doan: [
    "Đoạn thứ nhất…",
    "Đoạn thứ hai…",
    // thêm hoặc bớt đoạn tùy ý, mỗi đoạn một dòng trong ngoặc kép, cách nhau bằng dấu phẩy
  ],
  kyTen: "Anh yêu em rất nhiều! ♡",
  anh: ""
};
```

| Mục | Ý nghĩa |
|---|---|
| `loiChao` | Dòng mở đầu lá thư |
| `doan` | Các đoạn của lá thư, mỗi phần tử là một đoạn |
| `kyTen` | Dòng ký tên cuối thư, hiển thị bằng chữ viết tay màu hồng |
| `anh` | Đường dẫn ảnh polaroid. Để trống `""` thì hiện khung ảnh mẫu |

> ⚠️ Trong một đoạn thư, nếu muốn dùng dấu ngoặc kép `"` thì viết thành `\"`. Dấu nháy đơn `'` dùng bình thường.

### Thêm ảnh

1. Chép ảnh vào thư mục `images/`, ví dụ `images/anh-doi.jpg`.
2. Sửa dòng `anh: ""` thành `anh: "images/anh-doi.jpg"`.

Mẹo:
- Ảnh vuông hiển thị đẹp nhất. Ảnh không vuông sẽ được cắt giữa cho vừa khung.
- Nên giảm ảnh xuống khoảng 800×800 px, dung lượng dưới 300 KB, để trang tải nhanh trên 4G.
- Tên file nên viết không dấu, không khoảng trắng (`anh-doi.jpg`, không dùng `ảnh đôi.JPG`). Trên server Linux, chữ hoa và chữ thường trong tên file được tính là khác nhau.

### Đổi chữ trên thiệp

Tìm trong `index.html`:

```html
<div class="l1">Happy</div>
<div class="l2">Womenday</div>
<div class="l3">20/10</div>
```

Ví dụ có thể đổi thành `Chúc mừng` / `ngày của em` / `20/10`.

### Đổi màu

Các màu chính nằm ở đầu phần `<style>`, trong khối `:root`:

```css
--ground:#fbf7f8;     /* màu nền trang */
--ink:#4a3a40;        /* màu chữ thư */
--rose:#f2b8c4;       /* màu phong bì */
--rose-deep:#e98fa3;  /* màu chữ thiệp, chữ ký */
--rose-soft:#fde4ea;  /* màu túi phong bì dưới lá thư */
```

### Tinh chỉnh khác

| Muốn đổi | Tìm trong `index.html` | Gợi ý |
|---|---|---|
| Tốc độ thư tự cuộn | `const SPEED=reduce?0:20;` | Đổi số `20` (px/giây): nhỏ hơn thì chậm hơn |
| Thời gian chờ trước khi chuyển sang lá thư | `setTimeout(showLetter,reduce?600:3600)` | `3600` = 3,6 giây |
| Số cánh hoa, trái tim | `const TARGET={env:{petal:28,heart:10,rise:8}` | `env` là màn hình phong bì, `letter` là màn hình thư. `petal` là cánh hoa, `heart` là tim rơi, `rise` là tim bay lên |

---

## 4. Deploy (đưa lên mạng)

Vì đây là trang tĩnh nên host nào cũng chạy được. Dưới đây là 4 cách miễn phí, bạn chọn **một** cách.

### Cách A: Netlify Drop (nhanh nhất, không cần tài khoản Git)

1. Vào <https://app.netlify.com/drop>.
2. Kéo cả thư mục `thu-20-10-source` thả vào trang.
3. Sau vài giây Netlify trả về link dạng `https://ten-ngau-nhien.netlify.app`.
4. Đổi tên link cho dễ nhớ: **Site configuration → Change site name**, ví dụ `thu-gui-em` → `https://thu-gui-em.netlify.app`.

Lưu ý: nếu không đăng nhập, site tạo bằng Drop chỉ tồn tại khoảng 1 giờ. Hãy tạo tài khoản (miễn phí) và nhận site (claim) để giữ link lâu dài.

### Cách B: GitHub Pages

1. Tạo repository mới trên GitHub, ví dụ `thu-20-10`. Repo phải để **Public** nếu dùng tài khoản miễn phí.
2. Đẩy code lên:
   ```bash
   cd thu-20-10-source
   git init
   git add .
   git commit -m "Thu 20/10"
   git branch -M main
   git remote add origin https://github.com/<ten-ban>/thu-20-10.git
   git push -u origin main
   ```
3. Trên GitHub: **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: `main` / `(root)` → Save**.
4. Đợi 1–2 phút, link sẽ là `https://<ten-ban>.github.io/thu-20-10/`.

### Cách C: Vercel

```bash
npm i -g vercel
cd thu-20-10-source
vercel          # lần đầu: đăng nhập và trả lời các câu hỏi (cứ Enter)
vercel --prod   # deploy bản chính thức
```

Bạn cũng có thể đẩy code lên GitHub rồi vào <https://vercel.com/new>, chọn repo và bấm **Deploy**. Framework Preset để **Other**, không cần build command.

### Cách D: Cloudflare Pages

1. Vào **Cloudflare Dashboard → Workers & Pages → Create → Pages → Upload assets**.
2. Đặt tên project, kéo thư mục `thu-20-10-source` vào, rồi bấm **Deploy**.
3. Link sẽ có dạng `https://<ten-project>.pages.dev`.

### Dùng tên miền riêng (tuỳ chọn)

Cả 4 nơi trên đều cho gắn tên miền riêng, ví dụ `thuguiem.com`, trong phần **Domains / Custom domain**. Bạn làm theo hướng dẫn trỏ DNS (bản ghi CNAME hoặc A) mà họ hiển thị.

---

## 5. Tạo hình nền QR trái tim cho link của bạn

Sau khi deploy xong và có link chính thức, tạo lại hình nền QR để mã trỏ đúng tới link đó.

```bash
cd qr
pip install -r requirements.txt
python tao-qr.py https://thu-gui-em.netlify.app
```

Kết quả là file `hinh-nen-qr-trai-tim.png`, cỡ 1179×2556 (vừa iPhone). Script tự quét thử ảnh vừa tạo và in ra `Quét thử: OK ✓` nếu mã đọc được.

Tuỳ chọn:

```bash
python tao-qr.py <link> -o hinh-nen.png        # đổi tên file xuất
python tao-qr.py <link> --rong 1080 --cao 2400 # cỡ màn Android phổ biến
python tao-qr.py <link> --mau "#7a2440"        # chấm màu đỏ rượu (nên giữ màu đậm)
python tao-qr.py <link> --seed 14              # kiểu rải chấm khác
```

Lưu ý:
- Link càng ngắn thì mã QR càng thưa và càng dễ quét. Nếu báo "Link quá dài", hãy dùng tên miền hoặc tên site ngắn hơn.
- Không nên dùng màu chấm nhạt (hồng nhạt, xám nhạt) vì camera khó đọc.
- Đặt ảnh làm **hình nền màn hình khoá**. Để quét được, cần một điện thoại khác: mở camera hướng vào màn hình, như trong video mẫu.

---

## 6. Kiểm tra trước khi tặng ✅

- [ ] Mở link trên **điện thoại** (không chỉ trên máy tính), chạm phong bì, đọc hết thư.
- [ ] Ảnh polaroid hiện đúng. Nếu không hiện, kiểm tra lại tên file và chữ hoa/thường.
- [ ] Dùng một điện thoại khác quét mã QR trên hình nền, xem có mở đúng trang không.
- [ ] Thử mở bằng 4G (tắt Wi-Fi) để chắc trang tải nhanh.
- [ ] Đọc lại lời thư một lượt để tránh lỗi chính tả 😄

---

## 7. Xử lý sự cố

| Hiện tượng | Cách xử lý |
|---|---|
| Chữ không phải kiểu viết tay | Font tải từ Google Fonts. Kiểm tra mạng, hoặc đợi vài giây cho font tải xong |
| Ảnh không hiện sau khi deploy | Sai đường dẫn hoặc sai chữ hoa/thường trong tên file. Đường dẫn phải là `images/...` và không có `/` ở đầu |
| Không thấy hoa rơi | Điện thoại đang bật chế độ giảm chuyển động (iOS: Cài đặt → Trợ năng → Chuyển động → Giảm chuyển động). Trang cố ý tắt hiệu ứng trong trường hợp này |
| Quét QR mở ra link cũ | Bạn chưa tạo lại hình nền sau khi đổi link. Chạy lại `tao-qr.py` với link mới |
| GitHub Pages báo 404 | Đợi thêm vài phút. Kiểm tra `index.html` nằm ở **gốc** repo, không nằm trong thư mục con |
| Lỗi ký tự lạ khi sửa file trên Windows | Lưu file với mã hoá **UTF-8**. Trong Notepad: Save As → Encoding: UTF-8 |

---

Chúc bạn có một ngày 20/10 thật ngọt ngào 🌸
