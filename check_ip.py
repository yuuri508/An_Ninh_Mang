import socket

number = int(input("nhap so luong domain muon check: "))

ls_domain = []

for i in range(number):
    domain = input("Nhập domain: ")
    ls_domain.append(domain)

for i in ls_domain:
    try:
        ip = socket.gethostbyname(i)
        print(f"[+] {i} -> {ip}")

    except socket.gaierror:
        print("[-] Không tìm thấy domain")