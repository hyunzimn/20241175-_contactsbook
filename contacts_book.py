def addC(name, number):
    try: 
        with open('contacts.txt', 'a') as f:
            f.write(f"\n{name} : {number}")
            print("연락처가 추가되었습니다.")
    except FileNotFoundError :
        print("연락처 파일이 없어 연락처를 추가할 수 없습니다.")

def viewC() :
    try:
        with open('contacts.txt', 'r') as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("연락처 파일이 없습니다.")

def searchC(name):
    try:
        with open('contacts.txt', 'r') as f:
            contacts = {}
            for line in f:
                line = line.strip()
                if ":" in line:
                    n, p = line.split(":", 1)
                    contacts[n.strip()] = p.strip()
        if name in contacts:
            print(name + '의 연락처는 ' + contacts[name] + '입니다.')
        else:
            print("연락처를 찾을 수 없습니다.")
    except FileNotFoundError:
        print("연락처 파일이 없어 연락처를 검색할 수 없습니다.")

def main() :
    while True:
        print("번호를 하나만 입력하세요.")
        a = input("1)추가 2)보기 3)검색 4)종료 : ")
        if a == '1' :
            name = input("이름을 입력하세요 :")
            number = input("전화번호를 입력하세요 :")
            addC(name, number)
        elif a == '2' :
            viewC()
        elif a == '3' :
            name = input("검색할 이름을 입력하세요 :")
            searchC(name)
        elif a == '4' :
            print("종료합니다.")
            break
        else : 
            print("잘못된 입력입니다.")

main()