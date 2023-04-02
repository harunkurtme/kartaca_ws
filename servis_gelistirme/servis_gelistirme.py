
import asyncio
import json
import websockets

"""
{
    "type":"HELLO",
    "hint":"Use: a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z. input : ab,z result : zy,a",
    "message":"Povzhv hvmw z nvhhztv drgs xfiivmg hvhhrlm rm qhlm ulinzg erz gsrh vcznkov : {\"gbkv\":\"REGISTER\",\"mznv\":\"blfi mznv\",\"hfimznv\":\"blfi hfimznv\",\"vnzro\":\"blfi vnzro zwwivhh\",\"ivtrhgizgrlmKvb\":\"ccc\"}. Kvvk orhgvmrmt mvd nvhhztv uli gzhp xlmgvmg! Ylfi ivtrhgizgrlmKvb 
    : u9wuzuw3710wx36563w527311x139wu7x91v9yw8xy9w32v9753u4u00zwu64v1v"}
"""


def get_token(come_data) -> str:
    return (come_data.split(",")[len(come_data.split(","))-1].replace('"', "").replace('}', "")).split(" ")[(len((come_data.split(",")[len(come_data.split(","))-1].replace('"', "").replace('}', "")).split(" "))-1)]


async def hello():
    async with websockets.connect("wss://cekirdektenyetisenler.kartaca.com/ws") as websocket:
        
        value="a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split(",")
        reverseValue=[]
            
        print(type(value.reverse()))
        sendCommand = {"type": "REGISTER", "name": "Harun KURT",
                       "email": "harunkurt0000@gmail.com", "phone": "05458146806", "password": ""}
        come_data = await websocket.recv()
        print(json.loads(come_data)["message"])
        # print(come_data.replace('"', "").replace('}', ""))
        print(get_token(come_data=come_data))
        sendCommand["password"] = get_token(come_data=come_data)
        await websocket.send(json.dumps(sendCommand))


asyncio.run(hello())
