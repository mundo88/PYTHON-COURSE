# Vòng lặp while là để sử dụng thực thi một cái khối câu lệnh lặp đi lặp lại cho đến khi kết thúc một điều kiện thỏa mãn

a = 1
# while + condition đúng : 
while True:
    # khối câu lệnh được thực thi trong while
    a += 1
    print(a)
    #điều kiện khi a lớn hơn hoặc bằng 100 thì thực thi câu lệnh bên trong if
    if a >= 100:
        # Câu lệnh break để bắt buộc thoát vòng lặp
        break
