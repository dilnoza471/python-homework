from bs4 import BeautifulSoup

def weather_info():
    """prints out weather info from weather.html file, handles fileNotFound exception"""
    try:
        file = open('weather.html')
    except FileNotFoundError:
        print('weather.html file not found')
    else:
        high_day = ''
        high_temp = 0
        sum_temp = 0
        sunny = []
        soup = BeautifulSoup(file.read(), 'html.parser')
        headers = [x.text for x in soup.find_all('th')]
        body = soup.find('tbody').find_all('td')
        data = [[body[i].text, body[i + 1].text, body[i + 2].text] for i in range(0, len(body), 3)]
        print(' ', end='')
        for i in range(53):
            print('_', end='')
        print()
        print(f"| {headers[0]:^15} | {headers[1]:^15} | {headers[2]:^15} |")
        print('|', end='')
        for i in range(53):
            print('-', end='')
        print('|')
        for i in data:
            if i[2] == 'Sunny':
                sunny.append(i[0])
            print(f"| {i[0]:^15} | {i[1]:^15} | {i[2]:^15} |")
            sum_temp += int(i[1][:2])
            if int(i[1][:2]) > high_temp:
                high_day = i[0]
                high_temp = int(i[1][:2])
        print()
        print(f"Highest temperature's detected on {high_day}: {high_temp}°C")
        print(f"Average temperature over the week is {sum_temp/5}°C")
        print("Sunny days are: ", ', '.join(sunny))
        file.close()

if __name__ == '__main__':
    weather_info()


