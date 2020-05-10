import vkbee, asyncio,time

tocken = str(input('Введите свой вк токен-->'))

ownid = int(input('Введите свой ЦИФРОВОЙ айди--->'))

psid = int(input('Введите айди поста--->'))

async def main(loop):

    vk=vkbee.VkApi(tocken,loop=loop)

    while 111111==111111:

        comment=await vkbee.VkApi.call(vk,'wall.createComment',{'owner_id':ownid,'post_id':psid,'sticker_id':14084})

        print('Комментарий отправлен[+]--->'+ str(comment))

        time.sleep(1)

loop = asyncio.get_event_loop()

loop.run_until_complete(main(loop))