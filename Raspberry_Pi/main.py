import websockets
import asyncio
import Display
import blanket_ctrl
import time
import os
from w1thermsensor import W1ThermSensor

PORT = 8080
on = False
status = " "

async def handleMessage(websocket, path):
    status = "awaiting command..."
    sensor = W1ThermSensor()
    disp = Display.On_Display() #from the display script

    async for message in websocket: # anytime there is an await, need to wrap it with an async
        global on
        global status
        if on == True:
            temp = sensor.get_temperature()
            disp.draw_labels(temp, status)
            
        if message == "ON": # turn on blanket
            if on == False:
                on = True
                status = "Ready to Heat"
                temp = sensor.get_temperature()
                disp.draw_labels(temp, status)

        elif message == "OFF": # turn off blanket
            if on == True:
                on = False
                disp.draw_labels(temp, "Powering down...") #calling disp instead of changing status so this will be seen
                time.sleep(2)
                os.system("shutdown now") #if this doesn't work, chmod the script
                
        else: # change the temp of the blanket
            if on == True: 
                req_temp = int(message) # cast to an int, this will get passed to blanket_ctrl
                blanket_ctrl.change_temp(req_temp)# should be right, might throw errors

        await websocket.send("Server received " + message) # send the message back to the client

start_server = websockets.serve(handleMessage, "10.16.84.97", PORT) # store the instance of the new server
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()