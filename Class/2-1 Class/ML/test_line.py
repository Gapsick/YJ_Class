import requests

def send_line_notify(message):
    token = 'Zu9dvTz0DhW6UBW7Fsm53inArx31c3WbmlrkHeG1MmC'
    url = 'https://notify-api.line.me/api/notify'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    data = {'message': message}
    requests.post(url, headers=headers, data=data)

# 사용 예시
send_line_notify("✅ 게시물이 등록되었습니다!")
