from django.http import HttpResponse

#from core.hero import get_hero

from core import GLOBAL
from core.battle.hero import BattleHero, MonsterHero
from core.battle.battle import Battle
from core.mongoscheme import MongoChar

from utils import pack_msg

import protomsg


class PVE(Battle):
    def load_my_heros(self):
        char_data = MongoChar.objects.get(id=self.my_id)
        socket_ids = char_data.formation
        sockets = char_data.sockets

        self.my_heros = []
        for hid in socket_ids:
            if hid == 0:
                self.my_heros.append(None)
            else:
                sock = sockets[str(hid)]
                hid = sock.hero
                if not hid:
                    self.my_heros.append(None)
                else:
                    #_, original_id, level = get_hero(hid)
                    #h = BattleHero(hid, original_id, level, [])
                    h = BattleHero(hid)
                    self.my_heros.append(h)



    def load_rival_heros(self):
        monster_ids = GLOBAL.STAGE[self.rival_id]['monsters']
        self.rival_heros = []
        for mid in monster_ids:
            if mid == 0:
                self.rival_heros.append(None)
            else:
                h = MonsterHero(mid)
                self.rival_heros.append(h)


def pve(request):
    msg = protomsg.Battle()

    req = request._proto
    print req

    _, _, char_id = request._decrypted_session.split(':')
    char_id = int(char_id)

    b = PVE(char_id, req.stage_id, msg)
    b.start()

    response = protomsg.PVEResponse()
    response.ret = 0
    response.stage_id = req.stage_id
    response.battle.MergeFrom(msg)

    data = pack_msg(response)
    return HttpResponse(data, content_type='text/plain')

