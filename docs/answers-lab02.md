# Trả lời thảo luận Lab 02

1. Đồng bộ với `main` trước PR để kiểm tra mã khi tích hợp và giải quyết xung đột sớm. Nhánh càng cũ thì nguy cơ xung đột càng cao.
2. Không rebase các commit đã chia sẻ khi người khác có thể đang dựa vào chúng, vì rebase tạo SHA mới và buộc đồng bộ lại lịch sử. Trên nhánh riêng chưa chia sẻ, rebase có thể dùng để sắp xếp lịch sử.
3. `feature/*` thêm hành vi cho sản phẩm; `topic/*` chứa công việc hỗ trợ như tài liệu hoặc cấu hình.
4. Merge commit giữ lịch sử chi tiết của nhánh; squash gộp các commit thành một; rebase and merge tạo lịch sử tuyến tính nhưng đổi SHA của commit.
5. Khi push thêm commit sau approval, cần review lại vì mã cuối cùng đã khác mã được duyệt.
