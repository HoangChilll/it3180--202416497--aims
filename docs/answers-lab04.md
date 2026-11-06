# Trả lời thảo luận Lab 04

1. Chuẩn bị phiên bản trên `main` trước khi tạo nhánh release để baseline lấy từ mã đã qua PR và kiểm thử; nhánh release chỉ nhận hotfix.
2. Tag định danh một commit cụ thể và không di chuyển. Nhánh `release/*` là dòng bảo trì, có thể tiến thêm khi nhận bản vá.
3. Không merge cả nhánh release ngược về `main` vì commit nâng phiên bản và các thay đổi riêng của bản cũ có thể làm hỏng dòng phát triển mới. Chỉ chuyển commit sửa lỗi cần thiết bằng `cherry-pick -x`.
4. Release Flow của bài dùng `main` làm dòng phát triển và các nhánh release để bảo trì. GitFlow thường có thêm `develop` và các nhánh release/hotfix với quy trình merge khác.
5. `1.0.0` biểu thị mốc ổn định đầu tiên; các mốc Lab 01–03 là phiên bản tiền ổn định `0.x`.
