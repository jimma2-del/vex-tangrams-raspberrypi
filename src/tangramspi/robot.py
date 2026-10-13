import asyncio
import time

# from gpiozero import Motor

async def schedule(delay, coroutine, *args, **kwargs):
    await asyncio.sleep(delay)
    await coroutine(*args, **kwargs)

class Robot:
    FAILSAFE_NS = 200e6 # time (ns) after which we will automatically stop the robot, in case of a bug with the server/connection

    def __init__(self, id):
        self.id = id

        self._action = None # latest action sent by server
        self._network_delay = None # difference between time.monotonic_ns() on robot vs on server

        # self._wheels = (
        #     Motor(forward=5, backward=6),
        #     Motor(forward=7, backward=8),
        #     Motor(forward=9, backward=10)
        # )

    def set_action(self, action):
        cur_delay = time.monotonic_ns() - action['time']
        if self._network_delay is None or cur_delay < self._network_delay:
            self._network_delay = cur_delay
        
        asyncio.create_task(schedule(self.FAILSAFE_NS / 1e9, self._check_failsafe))
        self._set_action(action)  

    async def _check_failsafe(self):
        if self._action is None: return

        latest_action_time = self._action['time'] - self._network_delay

        if time.monotonic_ns() - latest_action_time > self.FAILSAFE_NS:
            self._set_action(None)

    def _set_action(self, action):
        self._action = action

        print(action)

        if self._action == None:
            return self._stop()

        # set wheel speeds
        # for wheel, speed in zip(self._wheels, self._action['wheel_speeds']):
        #     wheel.value = speed

    def _stop(self):
        pass
        # for wheel in self._wheels:
        #     wheel.stop()
