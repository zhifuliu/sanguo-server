# -*- coding: utf-8 -*-

import core.drives
from mongoengine import *

# 充值记录
class MongoPurchaseLog(Document):
    char_id = IntField()
    # 充值获得元宝
    sycee = IntField()
    purchase_at = IntField()  # UTC timestamp

    meta = {
        'collection': 'purchase_log',
        'indexes': ['char_id', 'purchase_at']
    }

MongoPurchaseLog.ensure_indexes()

# 消费元宝记录
class MongoCostSyceeLog(Document):
    char_id = IntField()
    sycee = IntField()
    cost_at = IntField() # UTC timestamp

    meta = {
        'collection': 'cost_sycee_log',
        'indexes': ['char_id', 'cost_at']
    }

MongoCostSyceeLog.ensure_indexes()


class MongoPurchaseRecord(Document):
    id = IntField(primary_key=True)
    # times 记录每个商品购买的次数, key为商品ID, value为购买次数
    times = DictField()

    yueka_sycee = IntField(default=0)
    yueka_remained_days = IntField(default=0)

    # lock 用在多个进程同时处理 yueka_remained_days 用来互斥
    # 以保证正确设置days
    yueka_lock = BooleanField(default=False)

    meta = {
        'collection': 'purchase_record',
        'indexes': ['yueka_remained_days',]
    }

MongoPurchaseRecord.ensure_indexes()


class MongoFunctionOpen(Document):
    id = IntField(primary_key=True)
    # list of freeze func ids
    freeze = ListField(IntField())

    meta = {
        'collection': 'function_open',
    }


class MongoCharacter(Document):
    id = IntField(primary_key=True)
    account_id = IntField()
    server_id = IntField()

    name = StringField()
    gold = IntField(default=0)
    sycee = IntField(default=0)
    level = IntField(default=1)
    exp = IntField(default=0)
    official = IntField(default=0)
    official_exp = IntField(default=0)

    # 充值真实获得
    purchase_got = IntField(default=0)
    vip = IntField(default=0)
    # vip 经验， 2016.1.1 新增
    # 以前是直接用purchase_got 判断，现在改成用vip_exp
    # 方便做VIP充值活动，vip经验翻倍这样的，不用改变本来的purchase_got
    vip_exp = IntField(default=0)
    # 用来标识已经领取的VIP奖励
    vip_has_reward = ListField(IntField())

    # 创建角色时间
    create_at = DateTimeField()
    last_login = DateTimeField()

    meta = {
        'collection': 'character',
        'indexes': ['level', 'name', 'last_login'],
    }

MongoCharacter.ensure_indexes()


class MongoTimesLog(Document):
    # 次数记录
    id = StringField(primary_key=True)  # uuid
    key = StringField() # function:char_id
    timestamp = IntField()

    meta = {
        'collection': 'times_log',
        'indexes': ['key', 'timestamp']
    }


class MongoEmbeddedEquipment(EmbeddedDocument):
    oid = IntField()
    level = IntField()
    gems = ListField(IntField())


class MongoItem(Document):
    id = IntField(primary_key=True)
    # 装备
    equipments = MapField(EmbeddedDocumentField(MongoEmbeddedEquipment))
    # 宝石
    gems = DictField()
    # 材料
    stuffs = DictField()

    meta = {
        'collection': 'item'
    }


class MongoSocket(EmbeddedDocument):
    # 阵法插槽
    hero = IntField(default=0)
    weapon = IntField(default=0)
    armor = IntField(default=0)
    jewelry = IntField(default=0)
    horse = IntField(default=0)



class MongoFormation(Document):
    id = IntField(primary_key=True)
    sockets = MapField(EmbeddedDocumentField(MongoSocket))
    formation = ListField(IntField())

    meta = {
        'collection': 'formation'
    }

class MongoStage(Document):
    id = IntField(primary_key=True)
    # 已经打过的关卡，key为关卡ID，value 为 bool 值表示是否三星
    stages = DictField()
    # 最大三星关卡
    max_star_stage = IntField()
    stage_new = IntField()
    # 开启的精英关卡, key 为关卡ID， value 为今日打的次数
    elites = DictField()
    # 精英关卡的星级，key 为关卡ID， value True表示三星
    elites_star = DictField()
    # 精英小关卡购买记录 key 为 ID, value 为购买次数
    elites_buy = DictField()
    # 经验关卡通过次数。用于一定次数后发武将卡
    elites_times = IntField(default=0)
    # 开启的活动关卡
    activities = ListField(IntField())

    # 精英关卡有每天刷新的定时任务，为了避免每次无意义的刷死号
    # 这里用一个标志来表示当前这个人的是否需要刷新
    # 代码里如果精英关卡相关功能做过，就要设置elite_changed = True
    # 定时任务只去处理 elite_changed == True 的这些集合
    # 处理完后再把 elite_changed 设置为 False
    elite_changed = BooleanField(default=True)

    meta = {
        'collection': 'stage',
        'indexes': ['elite_changed',]
    }

MongoStage.ensure_indexes()

class MongoEmbeddedHeroPanelHero(EmbeddedDocument):
    oid = IntField()
    # 是否是好卡
    good = BooleanField()
    opened = BooleanField()


class MongoHeroPanel(Document):
    id = IntField(primary_key=True)
    panel = MapField(EmbeddedDocumentField(MongoEmbeddedHeroPanelHero))
    # 刷新次数，0表示刚刚初始化
    refresh_times = IntField(default=0)
    has_opened = BooleanField(default=False)

    meta = {
        'collection': 'heropanel',
        'indexes': ['has_opened',]
    }

MongoHeroPanel.ensure_indexes()


class MongoEmbeddedHeroWuxing(EmbeddedDocument):
    level = IntField(default=1)
    # 当前经验
    exp = IntField(default=0)


class MongoHero(Document):
    id = IntField(primary_key=True)
    char = IntField(required=True)
    oid = IntField(required=True)
    step = IntField(required=True)
    # 升阶是一点一点来的，而不是一下升上去的，progress记录了当前进度
    progress = IntField(required=True)

    wuxings = MapField(EmbeddedDocumentField(MongoEmbeddedHeroWuxing))

    meta = {
        'collection': 'hero',
        'indexes': ['char', ]
    }


MongoHero.ensure_indexes()



class MongoHeroSoul(Document):
    id = IntField(primary_key=True)
    # key 为将魂ID， value 为数量
    souls = DictField()

    meta = {
        'collection': 'hero_soul',
    }


class MongoPlunder(Document):
    id = IntField(primary_key=True)
    points = IntField(default=0)

    # 可用次数
    current_times = IntField(default=0)
    # 用来设置次数的锁
    current_times_lock = BooleanField(default=False)

    # wocao
    plunder_times = IntField(default=0)

    # 刷新出的对手
    char_id = IntField(default=0)
    char_name = StringField(default="")
    char_gold = IntField(default=0)
    char_power = IntField(default=0)
    char_leader = IntField(default=0)
    char_formation = ListField(IntField())
    char_hero_original_ids =ListField(IntField())
    char_city_id = IntField(default=0)
    # 为了支持跨服，将对手的InBattleHero信息也保持下来
    battle_heros = StringField()
    server_url = StringField()

    meta = {
        'collection': 'plunder'
    }


# 掠夺次数排行
class MongoPlunderBoard(Document):
    id = IntField(primary_key=True)
    times = IntField(default=0)

    meta = {
        'collection': 'plunder_board',
        'indexes': ['times',]
    }

MongoPlunderBoard.ensure_indexes()



class MongoEmbededPrisoner(EmbeddedDocument):
    oid = IntField()
    prob = IntField()
    active = BooleanField(default=True)

    # 掠夺收益金币/2，这就是释放所得金币
    gold = IntField()

class MongoPrison(Document):
    id = IntField(primary_key=True)
    prisoners = MapField(EmbeddedDocumentField(MongoEmbededPrisoner))

    meta = {
        'collection': 'prison'
    }


class MongoCounter(Document):
    id = IntField(primary_key=True)
    # key 是 preset.settings.COUNTER 中的key，值表示已经进行了多少次
    counter = DictField()

    meta = {
        'collection': 'counter'
    }


class MongoFriend(Document):
    id = IntField(primary_key=True)
    # 已经是好友的
    friends = ListField(IntField())
    # 自己发出申请等待对方确认的
    pending = ListField(IntField())
    # 别人发来的申请需要我接受的
    accepting = ListField(IntField())

    # 赠送掠夺次数的好友列表
    plunder_gives = ListField(IntField())
    # 获取掠夺次数的好友列表
    plunder_gots = ListField(IntField())
    # 谁送我的掠夺次数
    plunder_senders = ListField(IntField())

    meta = {
        'collection': 'friend'
    }


class MongoEmbededMail(EmbeddedDocument):
    name = StringField(required=True)
    content = StringField(required=True)
    attachment = StringField(required=False)
    has_read = BooleanField(required=True)
    create_at = StringField(required=True)

class MongoMail(Document):
    id = IntField(primary_key=True)
    mails = MapField(EmbeddedDocumentField(MongoEmbededMail))

    meta = {
        'collection': 'mail'
    }


class MongoCheckIn(Document):
    id = IntField(primary_key=True)
    # 当天是否已经签过。 次标志用定时任务修改
    has_checked = BooleanField(default=False)
    # 目前签到天数
    day = IntField()

    meta = {
        'collection': 'checkin',
        'indexes': ['has_checked',]
    }

MongoCheckIn.ensure_indexes()


class MongoTask(Document):
    id = IntField(primary_key=True)
    # key 为任务类型ID， value为此类型次数
    tasks = DictField()
    # 已领取奖励的任务ID列表（彻底完成）
    complete = ListField()
    # 已经完成但还没领取奖励的ID列表
    finished = ListField()
    # 当前进行的任务ID列表 （包括没完成的，完成的但还没领奖的，每种任务类型的最后一档任务）
    doing = ListField()

    meta = {
        'collection': 'task'
    }


class MongoAchievement(Document):
    id = IntField(primary_key=True)
    # 当前开始进行的，但还没完成
    # key 为成就ID， value 为值 （不一定是Int）
    doing = DictField()

    # 要显示的成就列表
    display = ListField()
    # 已完成但还没领奖的
    finished = ListField()
    # 彻底完成的
    complete = ListField()

    meta = {
        'collection': 'achievement'
    }

class MongoEmbeddedArenaBeatenRecord(EmbeddedDocument):
    name = StringField()
    old_score = IntField()
    new_score = IntField()


class MongoArena(Document):
    id = IntField(primary_key=True)
    score = IntField()
    beaten_record = ListField(EmbeddedDocumentField(MongoEmbeddedArenaBeatenRecord))

    meta = {
        'collection': 'arena',
        'indexes': ['score',]
    }

MongoArena.ensure_indexes()


class MongoAttachment(Document):
    id = IntField(primary_key=True)
    # prize_ids 保存当前所有可领取奖励的id号
    # attachments 如果保存有对应prize_id的 attachment，则直接在这里领取奖励
    # 否则就去对应的功能领取奖励
    prize_ids = ListField(IntField())
    attachments = DictField()

    meta = {
        'collection': 'attachment'
    }



class MongoStoreCharLimit(Document):
    id = IntField(primary_key=True)
    # 每人每天限量购买记录
    # 已经买过的商品，key 为id， values 为已经买的量
    limits = DictField()

    meta = {
        'collection': 'store_char'
    }


class MongoTeamBattle(Document):
    id = IntField(primary_key=True)
    battle_id = IntField()
    boss_id = IntField()
    boss_power = IntField()
    self_power = IntField()
    start_at = IntField()
    total_seconds = IntField()
    # status: 2 started, 3 reward
    status = IntField()
    # 每秒进度，是否完成就看已经经过的秒数乘以这个数值是否达到1
    step = FloatField(default=0)
    friend_ids = ListField(IntField())

    meta = {
        'collection': 'teambattle'
    }


class MongoEmbeddedHangLog(EmbeddedDocument):
    timestamp = IntField()
    tp = IntField()
    who = StringField()
    gold = IntField(default=0)
    item_text = StringField(default="")

class MongoAffairs(Document):
    id = IntField(primary_key=True)
    # 开启的战役/城镇
    opened = ListField(IntField())

    hang_city_id = IntField(default=0)
    hang_start_at = IntField(default=0)

    logs = ListField(EmbeddedDocumentField(MongoEmbeddedHangLog))

    meta = {
        'collection': 'affairs',
        'indexes': ['hang_city_id', ]
    }

MongoAffairs.ensure_indexes()


# 固定活动
class MongoActivityStatic(Document):
    id = IntField(primary_key=True)

    # 用来标识对应活动领奖次数
    # condition_id: times
    # 现在一个条件只能领奖一次，但还是记录了领的次数，
    # 防止以后出现可以领多次的情况出现
    reward_times = DictField()

    # 发送次数
    # 与上面的reward_times一样，只是这个是系统主动发送的，并不是等待玩家来领取的
    send_times = DictField()

    meta = {
        'collection': 'activity_static'
    }


# 活动记录
class MongoKeyRecord(Document):
    # 这里记录一些需求特殊记录
    # 比如活动期间还要求每天只能搞一次的!
    id = StringField(primary_key=True)
    value = IntField()

    meta = {
        'collection': 'key_record'
    }


# 直接设定的活动条件状态
class MongoActivityEnabledCondition(Document):
    id = StringField(primary_key=True)
    value = IntField()

    meta = {
        'collection': 'enabled_condition'
    }


# 坐骑
class MongoEmbeddedHorse(EmbeddedDocument):
    oid = IntField()
    attack = IntField()
    defense = IntField()
    hp = IntField()


class MongoHorse(Document):
    id = IntField(primary_key=True)
    horses = MapField(EmbeddedDocumentField(MongoEmbeddedHorse))

    # 强化的马，确认后覆盖以前马的信息
    strengthed_horse = MapField(EmbeddedDocumentField(MongoEmbeddedHorse))

    meta = {
        'collection': 'horse'
    }


# 工会
class MongoUnion(Document):
    id = IntField(primary_key=True) # 工会ID
    owner = IntField()              # 所有者ID

    name = StringField()
    bulletin = StringField(default="")
    level = IntField(default=1)
    contribute_points = IntField(default=0)

    score = IntField(default=0)

    battle_times = IntField(default=0)  # 工会战次数
    battle_records = ListField(BinaryField())    # 战斗记录

    meta = {
        'collection': 'union',
        'indexes': ['owner', 'name', 'score',]
    }

MongoUnion.ensure_indexes()

class MongoUnionMember(Document):
    id = IntField(primary_key=True)
    # 申请的
    applied = ListField(IntField())

    # 加入的，如果那个union的owner就是自己的id，那么那个union就是自己建立的
    joined = IntField(default=0)
    # 工会币
    coin = IntField(default=0)
    # 贡献度
    contribute_points = IntField(default=0)
    # 职务
    position = IntField(default=1)

    # 签到次数
    checkin_times = IntField(default=0)
    # 上次签到时间戳
    last_checkin_timestamp = IntField(default=0)

    # 购买buff的次数
    buy_buff_times = DictField()

    # 挑战boss的次数
    boss_times = IntField(default=0)

    meta = {
        'collection': 'union_members',
        'indexes': ['applied', 'joined', 'last_checkin_timestamp']
    }

MongoUnionMember.ensure_indexes()


# 开启的工会BOSS
class MongoEmbeddedUnionBossLog(EmbeddedDocument):
    char_id = IntField()
    damage = IntField()     # 造成伤害

class MongoEmbeddedUnionBoss(EmbeddedDocument):
    start_at = IntField()
    hp = IntField()         # 每被挑战一次后剩余hp
    killer = IntField(default=0)
    logs = ListField(EmbeddedDocumentField(MongoEmbeddedUnionBossLog))


class MongoUnionBoss(Document):
    # union id
    id = IntField(primary_key=True)
    # 开启的
    opened = MapField(EmbeddedDocumentField(MongoEmbeddedUnionBoss))

    meta = {
        'collection': 'union_boss',
    }



def purge_char(char_id):
    from core.union.union import Union, UnionOwner

    char_id = int(char_id)

    # 工会特殊处理
    u = Union(char_id)

    if isinstance(u, UnionOwner):
        # 要删除的人是会长
        print "process union"
        u.quit()

    char_field_records = {'MongoHero'}

    from mongoengine.base.metaclasses import TopLevelDocumentMetaclass
    records = globals()
    final_records = {}
    for name, obj in records.iteritems():
        if name.startswith('Mongo') and isinstance(obj, TopLevelDocumentMetaclass):
            final_records[name] = obj

    for name, obj in final_records.iteritems():
        if name in char_field_records:
            obj.objects.filter(char=char_id).delete()
        else:
            try:
                x = obj.objects.get(id=char_id)
                x.delete()
            except:
                pass

    # special case
    for m in MongoFriend.objects.all():

        _changed = False
        if char_id in m.friends:
            m.friends.remove(char_id)
            _changed = True
        if char_id in m.pending:
            m.pending.remove(char_id)
            _changed = True
        if char_id in m.accepting:
            m.accepting.remove(char_id)
            _changed = True

        if char_id in m.plunder_gives:
            m.plunder_gives.remove(char_id)
            _changed = True
        if char_id in m.plunder_gots:
            m.plunder_gots.remove(char_id)
            _changed = True
        if char_id in m.plunder_senders:
            m.plunder_senders.remove(char_id)
            _changed = True

        if _changed:
            m.save()

