try:
    import pyext
except:
    print "ERROR: This script must be loaded by the PD/Max pyext external"

PRVNI = 0
DRUHY = 1
BUTTON_START = 2
BUTTON_STOP = 3
BUTTON_FREEZE = 4
TOGGLE_MUTE = 5


class OSCRoute(pyext._class):
    """
    class na routovani osc messages a posilani veci podle nich
    """
    _inlets=1
    _outlets=1

    mapping_data = {
        '/2/xy1': (1, PRVNI),
        '/2/xy4': (1, DRUHY),
        '/2/xy2': (2, PRVNI),
        '/2/xy5': (2, DRUHY),
        '/2/xy3': (3, PRVNI),
        '/2/xy6': (3, DRUHY),
        '/3/xy7': (4, PRVNI),
        '/3/xy10': (4, DRUHY),
        '/3/xy8': (5, PRVNI),
        '/3/xy11': (5, DRUHY),
        '/3/xy9': (6, PRVNI),
        '/3/xy12': (6, DRUHY),
        '/4/xy13': (7, PRVNI),
        '/4/xy16': (7, DRUHY),
        '/4/xy14': (8, PRVNI),
        '/4/xy17': (8, DRUHY),
        '/4/xy15': (9, PRVNI),
        '/4/xy18': (9, DRUHY),

        '/2/push9': (1, BUTTON_START),
        '/2/push10': (1, BUTTON_STOP),
        '/2/push11': (1, BUTTON_FREEZE),

        '/2/push12': (2, BUTTON_START),
        '/2/push13': (2, BUTTON_STOP),
        '/2/push14': (2, BUTTON_FREEZE),

        '/2/push15': (3, BUTTON_START),
        '/2/push16': (3, BUTTON_STOP),
        '/2/push17': (3, BUTTON_FREEZE),

        '/3/push18': (4, BUTTON_START),
        '/3/push19': (4, BUTTON_STOP),
        '/3/push20': (4, BUTTON_FREEZE),

        '/3/push21': (5, BUTTON_START),
        '/3/push22': (5, BUTTON_STOP),
        '/3/push23': (5, BUTTON_FREEZE),

        '/3/push24': (6, BUTTON_START),
        '/3/push25': (6, BUTTON_STOP),
        '/3/push26': (6, BUTTON_FREEZE),

        '/4/push27': (7, BUTTON_START),
        '/4/push28': (7, BUTTON_STOP),
        '/4/push29': (7, BUTTON_FREEZE),

        '/4/push30': (8, BUTTON_START),
        '/4/push31': (8, BUTTON_STOP),
        '/4/push32': (8, BUTTON_FREEZE),

        '/4/push33': (9, BUTTON_START),
        '/4/push34': (9, BUTTON_STOP),
        '/4/push35': (9, BUTTON_FREEZE),

    }

    def _anything_(self, n, *args):
        print "Message into inlet %s: %s" % (n, args)
        self._send('osc-test', args[1:])

    def resolve_granular(self, page, xy_id):
        """
        vraci id ovladaneho granularu a konstantu
         jestli byl pouzit prvni nebo druhy xy_pad
        :param page:
        :param xy_id:
        :return:
        """
        return 1, PRVNI
