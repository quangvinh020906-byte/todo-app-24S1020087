tasks = []

task1 = {
    'content': 'Làm bài tập Python',
    'status': 'todo'
}

task2 = {
    'content': 'Học cấu trúc dữ liệu',
    'status': 'doing'
}

task3 = {
    'content': 'Nộp báo cáo môn học',
    'status': 'done'
}

tasks.append(task1)
tasks.append(task2)
tasks.append(task3)
def add_task(content):
    task = {
        'content': content,
        'status': 'Pending'
    }
    tasks.append(task)
def view_tasks():
    if not tasks:
        print("Danh sách công việc đang trống.")
        return

    print("\nDanh sách công việc:")
    for i in range(len(tasks)):
        print(f"{i + 1}. {tasks[i]['content']} - {tasks[i]['status']}")

def main():
    while True:
        print("\n--- TODO LIST ---")
        print("1. Thêm công việc")
        print("2. Xem danh sách")
        print("3. Đánh dấu hoàn thành")
        print("4. Thoát")
        choice = input("Chọn chức năng: ")
        if choice == '1':          
            content = input("Nhập nội dung công việc: ")
            add_task(content)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            print("chức năng đánh dấu hoàn thành(chưa làm)")
        elif choice == '4':
            print("Kết thúc chương trình.")
            break
        else:
            print("lựa chọn không hợp lệ")
if __name__ == "__main__":
    main()