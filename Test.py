list_bill = [
    {
        "id" : "HD001",
        "name" : "Ban phim Co Corsair",
        "price" : 1800000,
        "quantity" : 2,
        "discount" : 200000,
        "total_price" : 3740000,
        "value_bill" : "Lớn"
    }
]
def validate_bill_1(id):
    for i,bill in enumerate(list_bill) :
        if id == bill["id"]:
            return i
        return -1
    
def caculate_price(price, quantity, discount):
    total_bill = ((price*quantity)-discount)*1.1
    return total_bill

def validate_quantity():
    while True:
        try:
            quantity = int(input("Nhập số lượng sản phẩm : "))
            if quantity < 0:
                print("Số lượng lớn hơn 0")
                continue
            return quantity
        except :
            print("Số lượng phải là số")
            continue
        
def validate_price_and_discount(type):
    while True:
        try:
            money = int(input(f"Nhập số tiền {type} :"))
            if money <= 0:
                print(f"{type} phải là số lớn hoặc bằng 0")
                continue
            return money
        except:
            print("Số tiền không hợp lệ")
            continue
        
def validate_rank(total):
    if total == 1000000:
        return "Nhỏ"
    elif total >= 1000000 and total <= 5000000:
        return "Vừa"
    elif total >= 5000000 and total <= 15000000:
        return "Lớn"
    else :
        return "Cao cấp"
        
def display_bill(bills):
    if len(list_bill) == 0:
        print("Danh sách hóa đơn hiện đang trống")
    else:
        print("Danh sách hóa đơn : ")
        print(f"{"Mã HD":<5} | {"Sản phẩm":<20} | {"Đơn giá":<7} | {"Số lượng":<9} | {"Giảm giá":<8} | {"Tổng tiền thanh toán":<20} | {"Phân loại giá trị":<20}")
        for item in bills:
            print(f"{item["id"]:<5} | {item["name"]:<20} | {item["price"]:<7} | {item["quantity"]:<9} | {item["discount"]:<8} | {item["total_price"]:<20} | {item["value_bill"]:<20}")
            
def add_bill():
    while True:
        id_bill = input("Nhập mã hóa đơn : ").strip().upper()
        index = validate_bill_1(id_bill)
        if id_bill == "":
            print("Mã hóa đơn không được để trống")
            continue
        if index != -1:
            print("Mã hóa đơn đã tồn tại")
            continue
        break
    while True:
        name_product = input("Nhập tên sản phẩm : ").strip()
        if not name_product:
            print("Tên sản phẩm không được để trống")
            continue
        break
    
    quantity = validate_quantity()
    price = validate_price_and_discount("đơn giá")
    discount = validate_price_and_discount("giảm giá")
    total = caculate_price(price, quantity, discount)
    rank = validate_rank(total)
    
    new_bill = {
        "id" : id_bill,
        "name" : name_product,
        "price" : price,
        "quantity" : quantity,
        "discount" : discount,
        "total_price" : total,
        "value_bill" : rank
    }
    
    list_bill.append(new_bill)
    
def update_bill():
    while True:
        update_id = input("Nhập mã hóa đơn cần cập nhật : ").strip().upper()
        index = validate_bill_1(update_id) 
        if update_id == "":
            print("Mã hóa đơn không được để trống")
            continue
        if index == -1:
            print("Không tìm thấy mã hóa đơn")
            continue
        break
    
    quantity = validate_quantity()
    price = validate_price_and_discount("đơn giá")
    discount = validate_price_and_discount("giảm giá")
    total = caculate_price(price, quantity, discount)
    rank = validate_rank(total)
    
    list_bill[index]["price"] = price
    list_bill[index]["quantity"] = quantity
    list_bill[index]["discount"] = discount
    list_bill[index]["total_price"] = total
    list_bill[index]["value_bill"] = rank
    
def delete_bill():
    while True:
        delete_id = input("Nhập mã hóa đơn đơn muốn xóa : ").strip().upper()
        index = validate_bill_1(delete_id)
        if delete_id == "":
                print("Mã hóa đơn không được để trống")
                continue
        if index == -1:
            print("Không tìm thấy mã hóa đơn")
            continue
        break
    confirm = input("Bạn có chắc muốn hủy và xóa đơn này không? (Y/N)  ").strip().upper()
    if confirm == "Y":
        list_bill.pop(index)
        
def search_by_id(bills):
    while True:
        id_search = input("Nhập mã hóa đơn cần tìm : ").strip().upper()
        index = validate_bill_1(id_search)
        if id_search == "":
                print("Mã hóa đơn không được để trống")
                continue
        if index == -1:
            print("Không tìm thấy mã hóa đơn")
            continue
        break
    
    print(display_bill([list_bill[index]]))
    
def search_by_name(bills):
    while True:
        name_search = input("Nhập tên sản phẩm cần tìm : ").strip().title()
        if name_search == "":
            print("Tên sản phẩm không được để trống")
            continue
        result = []
        if name_search.upper() in list_bill["name"].upper():
            result.append(list_bill)
            print(display_bill(result))
        break

def display_total_price():
    cao_cap = 0
    vua = 0
    small = 0
    big = 0
    if list_bill["value_bill"] == "Cao cấp":
        cao_cap += 1
    elif list_bill["value_bill"] =="Lớn":
        big += 1
    elif list_bill["value_bill"] == "Vừa":
        vua += 1
    else :
        small += 1
    
    print(f"Số lượng hóa đơn thuộc nhóm Cao Cấp : {cao_cap}")
    print(f"Số lượng hóa đơn thuộc nhóm lớn : {big}")
    print(f"Số lượng hóa đơn thuộc nhóm vừa : {vua}")
    print(f"Số lượng hóa đơn thuộc nhóm nhỏ : {small}")

    
def main():
    while True:
        choice = int(input("""
        ---- MENU ----
        1. Hiển thị danh sách hóa đơn
        2. Lập hóa đơn mới tại quầy
        3. Cập nhật thông tin hóa đơn
        4. Hủy hóa đơn lỗi
        5. Tìm kiếm hóa đơn
        6. Thống kê phân loại doanh thu
        7. Thoát chương trình
        Mời bạn nhập lựa chọn (1-7) : """))
        
        match choice:
            case 1:
                display_bill(list_bill)
            case 2:
                add_bill()
            case 3:
                update_bill()
            case 4:
                delete_bill()
            case 5:
                choose = int(input("""
                1. Tìm kiếm theo mã hóa đơn
                2. Tìm theo tên sản phẩm 
                Mời bạn nhập lựa chọn : """))
                match choose:
                    case 1:
                        search_by_id(list_bill)
                    case 2:
                        search_by_name(list_bill)
main()