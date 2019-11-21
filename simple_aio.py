import asyncio

async def print_msg(msg, wait):
    await asyncio.sleep(wait)
    print(msg)

loop = asyncio.get_event_loop()

loop.run_until_complete(
       asyncio.gather(
           print_msg('hello world', 1),
           print_msg('grusse velt', 2),))
# Because of the yields from the awaits, 
#    the output above comes out in the order indicated 
#    the sequence, above
