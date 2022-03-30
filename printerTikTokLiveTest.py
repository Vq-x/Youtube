from TikTokLive import TikTokLiveClient
from escpos.printer import Usb
from TikTokLive.types.events import CommentEvent, ConnectEvent, GiftEvent, ShareEvent, LikeEvent, FollowEvent, ViewerCountUpdateEvent

p = Usb(0x04b8, 0x0202)

client: TikTokLiveClient = TikTokLiveClient(
    unique_id="userName", **(
        {
            "enable_extended_gift_info": True
        }
    )
)

@client.on("connect")
async def on_connect(_: ConnectEvent):
    print("Connected to Room ID:", client.room_id)

@client.on("comment")
async def on_connect(event: CommentEvent):
    p.text(f'{event.user.uniqueId} commented on the video saying {event.comment}\n')
    p.image(event.user.profilePicture.urls[0])

@client.on("gift")
async def on_gift(event: GiftEvent):
    p.text(f"{event.user.uniqueId} sent a {event.gift.gift_id}!\n")




if __name__ == '__main__':
    # Run the client and block the main thread
    # await client.start() to run non-blocking
    
    client.run()
