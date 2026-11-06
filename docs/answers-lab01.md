# Trả lời thảo luận Lab 01

1. `git config --global` lưu cấu hình người dùng trong tệp `~/.gitconfig` trên máy; `--local` lưu trong `.git/config` và chỉ áp dụng cho repo hiện tại. Cấu hình local có mức ưu tiên cao hơn global.
2. `git mv` vừa chuyển tệp vừa đưa thao tác vào staging. Git thực tế nhận diện đổi tên bằng cách so sánh nội dung, nên `git mv` giúp thao tác gọn hơn chứ không tạo một loại lịch sử riêng.
3. `release/lab01` là baseline vì nó chốt một trạng thái đã được kiểm tra để nộp bài. Commit ở đầu nhánh xác định chính xác nội dung của baseline.
4. Kể cả làm một mình, thay đổi qua nhánh và Pull Request vẫn giúp kiểm tra diff, ghi lại lý do và tránh sửa trực tiếp baseline trên `main`.
