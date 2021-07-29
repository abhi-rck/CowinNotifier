import requests
import datetime



def getDataFromApi(pincode):
    center_list = []
    current_date = datetime.date.today().strftime('%d-%m-%Y')

    payload = requests.get(
        f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pincode}&date={current_date}')
    sessions = payload.json()
    center_list = []
    for session in sessions['sessions']:
        if session.get('available_capacity') > 0:
            center_list.append(session)

    return center_list
