import vk_api
import json

group_id = -43938013
def main():
    # Пример получения всех постов со стены
    login, password = '<ВАШ ЛОГИН>', '<ВАШ ПАРОЛЬ>'
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    tools = vk_api.VkTools(vk_session)
    wall = tools.get_all('wall.get', 100, {'owner_id': group_id})
    print('Posts count:', wall['count'])
    f = open(r" wall_asp.txt", 'a')
    f.write(json.dumps(wall))
    f.close()

if __name__ == '__main__':
    main()