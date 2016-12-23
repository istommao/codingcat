import asyncio
import aiomysql


def test_example(loop):
    mysql_config = dict(host='127.0.0.1', port=3306, user='root', loop=loop,
                        password='smilewusheng', db='xinyimei_backup',
                        charset='utf8', use_unicode=True,)
    conn = yield from aiomysql.connect(**mysql_config)

    cursor = yield from conn.cursor(aiomysql.DictCursor)

    yield from cursor.execute("SELECT * from info_article")

    results = yield from cursor.fetchone()
    conn.close()

    return results


def test():
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(test_example(loop))


if __name__ == '__main__':
    print(test())
