import requests
import folium


def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        data = {
            '[Ip]': response.get('query'),
            '[Provider]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Contry]': response.get('country'),
            '[Region]': response.get('regionName'),
            '[City]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon')
        }
        for k, v in data.items():
            print(f'{k} : {v}')
        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f'{response.get("query")}_{response.get("city")}.html')
    except requests.exceptions.ConnectionError:
        print("Error, try again")


def main():
    ip = input("Enter ip: ")
    get_info_by_ip(ip=ip)


if __name__ == '__main__':
    main()
