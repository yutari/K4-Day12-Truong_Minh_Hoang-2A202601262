# Phiếu phản ánh — K4 Ngày 12

Họ và tên: Trương Minh Hoàng  
Mã học viên: 2A202601262

### Câu 1 — Fail fast (CP1)

Nếu deploy lên Render mà quên đặt `API_TOKEN`, app dừng ngay khi khởi động và log lỗi cấu hình. Điều này tốt hơn nhiều so với dùng token mặc định `changeme`: service có thể vẫn chạy nhưng bất kỳ ai biết token đó đều gọi được API và làm phát sinh chi phí.

### Câu 2 — Log cho máy đọc (CP1)

Ví dụ log: `{"event":"chat_completed","severity":"INFO","ts":"2026-08-10T08:00:00+00:00","client_id":"sv01","usd_cost":0.0001}`.

Từ một dòng JSON, mình có thể lọc tất cả event `chat_completed` hoặc tính tổng `usd_cost` theo `client_id`. `print()` thông thường chỉ là một chuỗi khó lọc và khó dùng để tạo cảnh báo chính xác.

### Câu 3 — Kích thước image (CP2)

Image multi-stage mình build được có kích thước khoảng **270MB**. Mình chưa giữ lại Dockerfile một-stage để đo trực tiếp nên không điền một con số giả cho bản đó. Multi-stage nhỏ hơn vì runtime chỉ chứa Python slim, dependencies và source; các file tạm, cache pip và công cụ build không được đưa sang stage cuối.

### Câu 4 — Thứ tự lệnh trong Dockerfile (CP2)

Docker copy `requirements.txt` và cài dependency trước, nên khi chỉ sửa `app/main.py`, các layer cài dependency được dùng lại từ cache; chỉ các layer copy source và phần sau phải chạy lại. Nếu `COPY . .` đặt trước `pip install`, mọi thay đổi source sẽ làm mất cache của layer cài thư viện, khiến build chậm hơn.

### Câu 5 — Vì sao không chạy bằng root (CP2)

Nếu app có lỗ hổng, kẻ tấn công có thể thực thi lệnh trong container. Khi container chạy bằng root, các lệnh đó có quyền đọc/ghi nhiều file và khai thác thêm cấu hình hệ thống. `USER app` cắt chuỗi này bằng cách chạy process với quyền thường; lỗ hổng vẫn cần được xử lý nhưng mức ảnh hưởng bị giới hạn.

### Câu 6 — Bearer token (CP3)

`WWW-Authenticate: Bearer` là chuẩn HTTP cho biết client phải xác thực bằng Bearer token khi nhận 401. Mình dùng cùng một thông báo cho thiếu header, sai scheme và sai token để không tiết lộ cho người dò biết họ đã đoán đúng một phần nào của thông tin xác thực.

### Câu 7 — Token bucket (CP3)

Sau 10 phút im lặng, bucket vẫn chỉ có tối đa 10 token vì có `min(capacity, tokens)`. Client gửi được 10 request liên tiếp rồi request thứ 11 nhận 429. Nếu bỏ `min`, 10 phút sẽ tích lũy 100 token, cho phép burst lớn bất thường và làm mất ý nghĩa giới hạn tốc độ.

### Câu 8 — Ngân sách theo ngày (CP3)

Với hạn $30/tháng, sự cố bắt đầu lúc 2h sáng có thể gây thiệt hại gần như toàn bộ $30 trước khi có người phát hiện; service chỉ hồi theo chu kỳ tháng. Với hạn $1/ngày, thiệt hại tối đa trong ngày đó là $1 và ngân sách tự mở lại khi sang ngày UTC tiếp theo. Hạn theo ngày giới hạn rủi ro tốt hơn.

### Câu 9 — `/healthz` khác `/readyz` (CP4)

Nếu `/healthz` cũng kiểm tra Redis, Redis mất kết nối thì cả 3 container đều báo unhealthy. Orchestrator có thể restart cả cụm dù process vẫn chạy; restart liên tục không sửa được lỗi Redis và làm gián đoạn traffic. Vì vậy `/healthz` chỉ kiểm tra process, còn `/readyz` kiểm tra Redis để load balancer ngừng gửi request mới đúng nơi.

### Câu 10 — Deploy thật (CP5)

Khi chạy local trực tiếp, mình gặp lỗi 500 ở `/chat` vì `REDIS_URL` trỏ tới `redis://localhost:6379/0` nhưng Redis chưa chạy. Mình kiểm tra log server và thấy lỗi kết nối Redis, sau đó dùng `REDIS_URL=fake://` cho local; khi chạy Docker Compose thì dùng `redis://redis:6379/0`. Cách này giữ local đơn giản nhưng production vẫn dùng Redis thật.
