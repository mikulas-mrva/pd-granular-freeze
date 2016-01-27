try:
    import pyext
except:
    print "ERROR: This script must be loaded by the PD/Max pyext external"

PING = 0

XY_PAD_A = 1
XY_PAD_B = 2
BUTTON_START = 3
BUTTON_STOP = 4
BUTTON_FREEZE = 5
TOGGLE_MUTE = 6
SLIDER_GRANNY_VOLUME = 7
BUTTON_DEFAULT = 8

BUTTON_START_PAGE = 9
BUTTON_STOP_PAGE = 10
BUTTON_FREEZE_PAGE = 11

MASTER_VOLUME = 12
CHANNEL_VOLUME = 13
CHANNEL_GAIN = 14
CHANNEL_MUTE = 15

MIX_SYMBOL = 'mix'
GRANNY_SYMBOL = 'granny'

BUTTON_PRESS = [1]
BUTTON_RELEASE = [0]

ROUTES = {
    XY_PAD_A: [
        ['set-speed', 200],
        ['set-pitch', 250]
    ],
    XY_PAD_B: [
        ['window-size', 200],
        ['window-offset', 200]
    ],
    BUTTON_FREEZE: 'toggle-freeze',
    BUTTON_START: 'toggle-start',
    BUTTON_STOP: 'toggle-stop',

    TOGGLE_MUTE: 'mute',

    SLIDER_GRANNY_VOLUME: ['set-volume', 300],
    BUTTON_DEFAULT: 'set-to-default',

    MASTER_VOLUME: ['master-volume', 200],
    CHANNEL_VOLUME: ['channel-volume', 200],
    CHANNEL_GAIN: ['channel-gain', 200],
    CHANNEL_MUTE: 'channel-mute',
}


class OSCRoute(pyext._class):
    """
    class na routovani osc messages a posilani veci podle nich
    """
    _inlets = 1
    _outlets = 1

    mapping_data = {
        '/ping': (PING,),

        '/2/xy1': (GRANNY_SYMBOL, 1, XY_PAD_A),
        '/2/xy4': (GRANNY_SYMBOL, 1, XY_PAD_B),
        '/2/xy2': (GRANNY_SYMBOL, 2, XY_PAD_A),
        '/2/xy5': (GRANNY_SYMBOL, 2, XY_PAD_B),
        '/2/xy3': (GRANNY_SYMBOL, 3, XY_PAD_A),
        '/2/xy6': (GRANNY_SYMBOL, 3, XY_PAD_B),
        '/3/xy7': (GRANNY_SYMBOL, 4, XY_PAD_A),
        '/3/xy10': (GRANNY_SYMBOL, 4, XY_PAD_B),
        '/3/xy8': (GRANNY_SYMBOL, 5, XY_PAD_A),
        '/3/xy11': (GRANNY_SYMBOL, 5, XY_PAD_B),
        '/3/xy9': (GRANNY_SYMBOL, 6, XY_PAD_A),
        '/3/xy12': (GRANNY_SYMBOL, 6, XY_PAD_B),
        '/4/xy13': (GRANNY_SYMBOL, 7, XY_PAD_A),
        '/4/xy16': (GRANNY_SYMBOL, 7, XY_PAD_B),
        '/4/xy14': (GRANNY_SYMBOL, 8, XY_PAD_A),
        '/4/xy17': (GRANNY_SYMBOL, 8, XY_PAD_B),
        '/4/xy15': (GRANNY_SYMBOL, 9, XY_PAD_A),
        '/4/xy18': (GRANNY_SYMBOL, 9, XY_PAD_B),

        '/2/push9': (GRANNY_SYMBOL, 1, BUTTON_START),
        '/2/push10': (GRANNY_SYMBOL, 1, BUTTON_STOP),
        '/2/push11': (GRANNY_SYMBOL, 1, BUTTON_FREEZE),
        '/2/toggle1': (GRANNY_SYMBOL, 1, TOGGLE_MUTE),
        '/2/push36': (GRANNY_SYMBOL, 1, BUTTON_DEFAULT),
        '/2/fader27': (GRANNY_SYMBOL, 1, SLIDER_GRANNY_VOLUME),

        '/2/push12': (GRANNY_SYMBOL, 2, BUTTON_START),
        '/2/push13': (GRANNY_SYMBOL, 2, BUTTON_STOP),
        '/2/push14': (GRANNY_SYMBOL, 2, BUTTON_FREEZE),
        '/2/toggle2': (GRANNY_SYMBOL, 2, TOGGLE_MUTE),
        '/2/push37': (GRANNY_SYMBOL, 2, BUTTON_DEFAULT),
        '/2/fader28': (GRANNY_SYMBOL, 2, SLIDER_GRANNY_VOLUME),

        '/2/push15': (GRANNY_SYMBOL, 3, BUTTON_START),
        '/2/push16': (GRANNY_SYMBOL, 3, BUTTON_STOP),
        '/2/push17': (GRANNY_SYMBOL, 3, BUTTON_FREEZE),
        '/2/toggle3': (GRANNY_SYMBOL, 3, TOGGLE_MUTE),
        '/2/push38': (GRANNY_SYMBOL, 3, BUTTON_DEFAULT),
        '/2/fader29': (GRANNY_SYMBOL, 3, SLIDER_GRANNY_VOLUME),

        '/3/push18': (GRANNY_SYMBOL, 4, BUTTON_START),
        '/3/push19': (GRANNY_SYMBOL, 4, BUTTON_STOP),
        '/3/push20': (GRANNY_SYMBOL, 4, BUTTON_FREEZE),
        '/3/toggle4': (GRANNY_SYMBOL, 4, TOGGLE_MUTE),
        '/3/push39': (GRANNY_SYMBOL, 4, BUTTON_DEFAULT),
        '/3/fader30': (GRANNY_SYMBOL, 4, SLIDER_GRANNY_VOLUME),

        '/3/push21': (GRANNY_SYMBOL, 5, BUTTON_START),
        '/3/push22': (GRANNY_SYMBOL, 5, BUTTON_STOP),
        '/3/push23': (GRANNY_SYMBOL, 5, BUTTON_FREEZE),
        '/3/toggle5': (GRANNY_SYMBOL, 5, TOGGLE_MUTE),
        '/3/push40': (GRANNY_SYMBOL, 5, BUTTON_DEFAULT),
        '/3/fader31': (GRANNY_SYMBOL, 5, SLIDER_GRANNY_VOLUME),

        '/3/push24': (GRANNY_SYMBOL, 6, BUTTON_START),
        '/3/push25': (GRANNY_SYMBOL, 6, BUTTON_STOP),
        '/3/push26': (GRANNY_SYMBOL, 6, BUTTON_FREEZE),
        '/3/toggle6': (GRANNY_SYMBOL, 6, TOGGLE_MUTE),
        '/3/push41': (GRANNY_SYMBOL, 6, BUTTON_DEFAULT),
        '/3/fader32': (GRANNY_SYMBOL, 6, SLIDER_GRANNY_VOLUME),

        '/4/push27': (GRANNY_SYMBOL, 7, BUTTON_START),
        '/4/push28': (GRANNY_SYMBOL, 7, BUTTON_STOP),
        '/4/push29': (GRANNY_SYMBOL, 7, BUTTON_FREEZE),
        '/4/toggle7': (GRANNY_SYMBOL, 7, TOGGLE_MUTE),
        '/4/push42': (GRANNY_SYMBOL, 7, BUTTON_DEFAULT),
        '/4/fader33': (GRANNY_SYMBOL, 7, SLIDER_GRANNY_VOLUME),

        '/4/push30': (GRANNY_SYMBOL, 8, BUTTON_START),
        '/4/push31': (GRANNY_SYMBOL, 8, BUTTON_STOP),
        '/4/push32': (GRANNY_SYMBOL, 8, BUTTON_FREEZE),
        '/4/toggle8': (GRANNY_SYMBOL, 8, TOGGLE_MUTE),
        '/4/push43': (GRANNY_SYMBOL, 8, BUTTON_DEFAULT),
        '/4/fader34': (GRANNY_SYMBOL, 8, SLIDER_GRANNY_VOLUME),

        '/4/push33': (GRANNY_SYMBOL, 9, BUTTON_START),
        '/4/push34': (GRANNY_SYMBOL, 9, BUTTON_STOP),
        '/4/push35': (GRANNY_SYMBOL, 9, BUTTON_FREEZE),
        '/4/toggle9': (GRANNY_SYMBOL, 9, TOGGLE_MUTE),
        '/4/push44': (GRANNY_SYMBOL, 9, BUTTON_DEFAULT),
        '/4/fader35': (GRANNY_SYMBOL, 9, SLIDER_GRANNY_VOLUME),

        '/2/push45': (GRANNY_SYMBOL, [1, 2, 3], BUTTON_START_PAGE),
        '/2/push46': (GRANNY_SYMBOL, [1, 2, 3], BUTTON_STOP_PAGE),
        '/2/push47': (GRANNY_SYMBOL, [1, 2, 3], BUTTON_FREEZE_PAGE),
        '/3/push49': (GRANNY_SYMBOL, [4, 5, 6], BUTTON_START_PAGE),
        '/3/push50': (GRANNY_SYMBOL, [4, 5, 6], BUTTON_STOP_PAGE),
        '/3/push51': (GRANNY_SYMBOL, [4, 5, 6], BUTTON_FREEZE_PAGE),
        '/4/push52': (GRANNY_SYMBOL, [7, 8, 9], BUTTON_START_PAGE),
        '/4/push53': (GRANNY_SYMBOL, [7, 8, 9], BUTTON_STOP_PAGE),
        '/4/push54': (GRANNY_SYMBOL, [7, 8, 9], BUTTON_FREEZE_PAGE),

        '/1/fader13': (MIX_SYMBOL, None, MASTER_VOLUME),

        '/1/fader1': (MIX_SYMBOL, 1, CHANNEL_VOLUME),
        '/1/fader2': (MIX_SYMBOL, 2, CHANNEL_VOLUME),
        '/1/fader3': (MIX_SYMBOL, 3, CHANNEL_VOLUME),
        '/1/fader4': (MIX_SYMBOL, 4, CHANNEL_VOLUME),
        '/1/fader5': (MIX_SYMBOL, 5, CHANNEL_VOLUME),
        '/1/fader6': (MIX_SYMBOL, 6, CHANNEL_VOLUME),
        '/1/fader7': (MIX_SYMBOL, 7, CHANNEL_VOLUME),
        '/1/fader8': (MIX_SYMBOL, 8, CHANNEL_VOLUME),

        '/1/fader15': (MIX_SYMBOL, 1, CHANNEL_GAIN),
        '/1/fader16': (MIX_SYMBOL, 2, CHANNEL_GAIN),
        '/1/fader17': (MIX_SYMBOL, 3, CHANNEL_GAIN),
        '/1/fader18': (MIX_SYMBOL, 4, CHANNEL_GAIN),
        '/1/fader19': (MIX_SYMBOL, 5, CHANNEL_GAIN),
        '/1/fader20': (MIX_SYMBOL, 6, CHANNEL_GAIN),
        '/1/fader21': (MIX_SYMBOL, 7, CHANNEL_GAIN),
        '/1/fader22': (MIX_SYMBOL, 8, CHANNEL_GAIN),


        '/1/toggle10': (MIX_SYMBOL, 1, CHANNEL_MUTE),
        '/1/toggle11': (MIX_SYMBOL, 2, CHANNEL_MUTE),
        '/1/toggle12': (MIX_SYMBOL, 3, CHANNEL_MUTE),
        '/1/toggle13': (MIX_SYMBOL, 4, CHANNEL_MUTE),
        '/1/toggle14': (MIX_SYMBOL, 5, CHANNEL_MUTE),
        '/1/toggle15': (MIX_SYMBOL, 6, CHANNEL_MUTE),
        '/1/toggle16': (MIX_SYMBOL, 7, CHANNEL_MUTE),
        '/1/toggle17': (MIX_SYMBOL, 8, CHANNEL_MUTE),
        '/1/toggle18': (MIX_SYMBOL, 9, CHANNEL_MUTE),
        '/1/toggle19': (MIX_SYMBOL, 10, CHANNEL_MUTE),
        '/1/toggle20': (MIX_SYMBOL, 11, CHANNEL_MUTE),
        '/1/toggle21': (MIX_SYMBOL, 12, CHANNEL_MUTE),

        # todo '/5/xy19..30'
    }

    def _anything_(self, n, *args):
        osc_path = str(args[0])
        osc_data = list(args[1:])
        mapping_data = list(self.mapping_data.get(osc_path, []))

        if mapping_data and osc_data:
            for ret in self.route_osc_data(mapping_data, osc_data):
                self._outlet(1, *ret)
        else:
            print """
            nenamapovana vec:
            osc_path: %s
            osc_data: %s
            mapping_data: %s
            """ % (osc_path, osc_data, mapping_data)
            self._outlet(1, *args)

    @staticmethod
    def route_osc_data(mapping_data, osc_data):
        control_name = mapping_data[2]

        if control_name == PING:
            print 'pong.'

        elif control_name == XY_PAD_A:
            for i, route in enumerate(ROUTES[XY_PAD_A]):
                yield mapping_data[:2]+[route[0], osc_data[i]*route[1]]

        elif control_name == XY_PAD_B:
            for i, route in enumerate(ROUTES[XY_PAD_B]):
                yield mapping_data[:2]+[route[0], osc_data[i]*route[1]]

        elif control_name == BUTTON_FREEZE:
            if osc_data == BUTTON_RELEASE:
                yield mapping_data[:2]+[ROUTES[BUTTON_FREEZE]] + osc_data

        elif control_name == BUTTON_START:
            print osc_data
            if osc_data == BUTTON_RELEASE:
                yield mapping_data[:2]+[ROUTES[BUTTON_START]] + osc_data

        elif control_name == BUTTON_STOP:
            if osc_data == BUTTON_RELEASE:
                yield mapping_data[:2]+[ROUTES[BUTTON_STOP]] + osc_data

        elif control_name == TOGGLE_MUTE:
            yield mapping_data[:2]+[ROUTES[TOGGLE_MUTE]] + osc_data

        elif control_name == SLIDER_GRANNY_VOLUME:
            route = ROUTES[SLIDER_GRANNY_VOLUME]
            yield mapping_data[:2]+[route[0], osc_data[0]*route[1]]

        elif control_name == BUTTON_DEFAULT:
            if osc_data == BUTTON_RELEASE:
                route = ROUTES[BUTTON_DEFAULT]
                yield mapping_data[:2]+[route]+osc_data

        elif control_name == BUTTON_START_PAGE:
            if osc_data == BUTTON_RELEASE:
                for gran in mapping_data[1]:
                    yield [mapping_data[0], gran, ROUTES[BUTTON_START], 0]

        elif control_name == BUTTON_STOP_PAGE:
            if osc_data == BUTTON_RELEASE:
                for gran in mapping_data[1]:
                    yield [mapping_data[0], gran, ROUTES[BUTTON_STOP], 0]

        elif control_name == BUTTON_FREEZE_PAGE:
            if osc_data == BUTTON_RELEASE:
                for gran in mapping_data[1]:
                    yield [mapping_data[0], gran, ROUTES[BUTTON_FREEZE], 0]

        elif control_name == MASTER_VOLUME:
            route = ROUTES[MASTER_VOLUME]
            yield [mapping_data[0], route[0], osc_data[0]*route[1]]

        elif control_name == CHANNEL_VOLUME:
            route = ROUTES[CHANNEL_VOLUME]
            yield mapping_data[:2] + [route[0], osc_data[0]*route[1]]

        elif control_name == CHANNEL_GAIN:
            route = ROUTES[CHANNEL_GAIN]
            yield mapping_data[:2] + [route[0], osc_data[0]*route[1]]

        elif control_name == CHANNEL_MUTE:
            route = ROUTES[CHANNEL_MUTE]
            yield mapping_data[:2]+[route]+osc_data

        else:
            print """
            ###########
            dbg | else:
            ###########
            mapping_data: %s
            osc_data: %s
            """ % (mapping_data, osc_data)

"""
todo:
sines - s global vol
"""