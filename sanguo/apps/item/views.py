from django.http import HttpResponse

from models import Equipment

from core import GLOBAL
from core import notify
from core.exception import SanguoViewException
from core.equip import get_equip_level_by_whole_exp, delete_equip
from core.mongoscheme import MongoChar
from utils import pack_msg

from apps.item.cache import get_cache_equipment

from protomsg import StrengthEquipResponse, SellEquipResponse


EQUIP_TEMPLATE = GLOBAL.EQUIP.EQUIP_TEMPLATE
EQUIP_LEVEL_INFO = GLOBAL.EQUIP.EQUIP_LEVEL_INFO

def strengthen_equip(request):
    req = request._proto
    print req
    
    _, _, char_id = request._decrypted_session.split(':')
    char_id = int(char_id)
    
    char = MongoChar.objects.only('equips').get(id=char_id)
    char_equips = char.equips
    
    if req.id not in char_equips:
        raise SanguoViewException(500, "StrengthEquipResponse")
    
    for _id in req.cost_ids:
        if _id not in char_equips:
            raise SanguoViewException(500, "StrengthEquipResponse")
    
    all_exp = 0
    all_gold = 0
    for _id in req.cost_ids:
        print 'get equip, ', _id
        equip = get_cache_equipment(_id)
        level = equip.level
        tid = equip.tid
        quality = EQUIP_TEMPLATE[tid]['quality']
        
        this_level_quality = EQUIP_LEVEL_INFO[level]['quality'][quality]
        exp = this_level_quality['exp']
        gold = EQUIP_LEVEL_INFO[level]['cost']
        
        all_exp += exp
        all_gold += gold
    
    target = get_cache_equipment(req.id)
    final_exp = target.exp + all_exp
    
    new_level = get_equip_level_by_whole_exp(final_exp)
    
    target_model_obj = Equipment.objects.get(id=req.id)
    target_model_obj.exp = final_exp
    target_model_obj.level = new_level
    target_model_obj.save()
    
    target = get_cache_equipment(req.id)
    notify.update_equipment_notify(request._decrypted_session, target)
    
    
    delete_equip([_id for _id in req.cost_ids])
    notify.remove_equipment_notify(
        request._decrypted_session,
        [_id for _id in req.cost_ids]
        )

    response = StrengthEquipResponse()
    response.ret = 0
    data = pack_msg(response)
    return HttpResponse(data, content_type='text/plain')


def sell_equip(request):
    req = request._proto
    print req
    
    _, _, char_id = request._decrypted_session.split(':')
    char_id = int(char_id)
    
    char = MongoChar.objects.only('equips').get(id=char_id)
    char_equips = char.equips
    
    for _id in req.ids:
        if _id not in char_equips:
            raise SanguoViewException(500, "StrengthEquipResponse")
    
    all_gold = 0
    for _id in req.ids:
        equip = get_cache_equipment(_id)
        level = equip.level
        tid = equip.tid
        quality = EQUIP_TEMPLATE[tid]['quality']
        
        this_level_quality = EQUIP_LEVEL_INFO[level]['quality'][quality]
        gold = this_level_quality['gold']
        all_gold += gold
    
    print 'all_gold =', all_gold
    
    removed_ids = [_id for _id in req.ids]
    delete_equip(removed_ids)
    notify.remove_equipment_notify(
        request._decrypted_session,
        removed_ids
    )
    
    response = SellEquipResponse()
    response.ret = 0
    data = pack_msg(response)
    return HttpResponse(data, content_type='text/plain')