# Thông Tin Deploy — Checkpoint 5

## Thông Tin Học Viên

| Mục | Nội dung |
|---|---|
| Họ và tên | Trương Minh Hoàng |
| Mã học viên | 2A202601262 |
| Repo | https://github.com/yutari/K4-Day12-2A202601262-TruongMinhHoang.git |

## Service

| Mục | Nội dung |
|---|---|
| Public URL | https://k4-day12-truong-minh-hoang-2a202601262.onrender.com |
| Platform | Render |
| Ngày deploy | 10/08/2026 |

## Biến Môi Trường Đã Set Trên Cloud

| Biến | Đã set | Ghi chú |
|---|---|---|
| `PORT` | ✅ | Render tự gán |
| `API_TOKEN` | ✅ | Đặt trong dashboard, không ghi giá trị vào repo |
| `REDIS_URL` | ✅ | Render Redis service |
| `BUCKET_CAPACITY` | ✅ | 10 |
| `REFILL_PER_MINUTE` | ✅ | 10 |
| `DAILY_BUDGET_USD` | ✅ | 1.0 |
| `LOG_LEVEL` | ✅ | INFO |

## Lệnh Kiểm Tra

Public URL dùng để kiểm tra:

```text
https://k4-day12-truong-minh-hoang-2a202601262.onrender.com
```

## Kết Quả Chạy Thật

### 1. Liveness — `/healthz`

```text
HTTP/1.1 200 OK
Content-Type: application/json

{"status":"ok","service":"day12-chat-service","version":"1.0.0"}
```

### 2. Readiness — `/readyz`

```text
HTTP/1.1 200 OK
Content-Type: application/json

{"status":"ready","redis":true}
```

Hai kết quả trên xác nhận service đang chạy và đã kết nối được Redis trên Render.

### 3–5. Chat, authentication và rate limit

Chưa ghi output vào repository vì các lệnh này cần giá trị `API_TOKEN` bí mật. Token chỉ được đặt trong terminal/dashboard, tuyệt đối không commit vào file công khai.

## Ảnh Chụp Màn Hình

- `screenshots/dashboard.png` — dashboard Render.
- `screenshots/healthz.png` — kết quả gọi `/healthz`.
