# Trả lời thảo luận Lab 05

1. Cách sửa trên `main` trước giúp sửa lỗi ngay tại dòng phát triển chính và giảm nguy cơ quên nó; đổi lại phải chuyển bản vá về từng nhánh release bị ảnh hưởng. Cách sửa trên release trước ưu tiên khôi phục phiên bản đang phát hành, nhưng bắt buộc chuyển bản vá ngược về `main` và các release khác.
2. Nếu quên đưa bản vá vào `release/lab05`, dùng `git cherry -v origin/release/lab05 origin/release/lab04` để thấy commit sửa lỗi còn dấu `+`; đồng thời chạy test hồi quy trên `v1.1.0` sẽ phát hiện hành vi sai.
3. `git cherry-pick -x` giữ dòng ghi nguồn commit, giúp kiểm toán dù SHA của commit mới khác SHA trên release gốc.
4. Tag `v1.0.1` vẫn chỉ bản 1.0.x đã vá; tag `v1.1.0` phải tạo sau khi nhánh Lab 05 đã nhận bản vá.
