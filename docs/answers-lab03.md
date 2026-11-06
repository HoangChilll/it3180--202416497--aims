# Trả lời thảo luận Lab 03

1. Merge base là commit tổ tiên chung tốt nhất của hai nhánh. Git so sánh thay đổi của mỗi nhánh từ mốc này khi merge.
2. Với `main` và `release/*` đã chia sẻ, dùng `git revert` để tạo commit đảo ngược có thể truy vết. `git reset` dời con trỏ nhánh và viết lại lịch sử, dễ làm mất công việc của người khác.
3. Nếu PR bugfix hiện nhiều commit không liên quan, kiểm tra lại base. Bugfix tạo từ `feature/discount` phải merge vào nhánh tính năng trước, sau đó mới đưa tính năng vào `main`.
4. `reset --soft` giữ thay đổi trong staging, `reset --mixed` giữ trong working tree. `reset --hard` loại bỏ thay đổi nên chỉ dùng khi chắc chắn không cần chúng.
5. Khi xung đột, kết hợp ý đồ hai phía, xóa dấu `<<<<<<<`, `=======`, `>>>>>>>`, chạy test rồi mới hoàn tất merge.
