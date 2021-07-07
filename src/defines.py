from enum import Enum

class CardStatus(Enum):
    Null = 0
    Peng = 1
    Gang = 2

class HuType(Enum):
    NotComplete = 0
    SevenPairs = 1
    Normal = 2

g_HuMap = {
    HuType.NotComplete : "没胡"
    , HuType.Normal : "胡"
    , HuType.SevenPairs : "七小对"
}

class CardType(Enum):
    Unknow = -1

    TIAO = 10
    TIAO_1 = 11
    TIAO_2 = 12
    TIAO_3 = 13
    TIAO_4 = 14
    TIAO_5 = 15
    TIAO_6 = 16
    TIAO_7 = 17
    TIAO_8 = 18
    TIAO_9 = 19

    TONG = 20
    TONG_1 = 21
    TONG_2 = 22
    TONG_3 = 23
    TONG_4 = 24
    TONG_5 = 25
    TONG_6 = 26
    TONG_7 = 27
    TONG_8 = 28
    TONG_9 = 29

    OTHER = 90
    ZHONG = 91
    FA = 92
    BAI = 93


g_CardsMap = {
    -1 : "未知"
    # 条
    , 10 : "条", 11 : "一条", 12 : "二条", 13 : "三条", 14 : "四条", 15 : "五条"
    , 16 : "六条", 17 : "七条", 18 : "八条", 19 : "九条"
    # 筒
    , 20 : "筒", 21 : "一筒", 22 : "二筒", 23 : "三筒", 24 : "四筒", 25 : "五筒"
    , 26 : "六筒", 27 : "七筒", 28 : "八筒", 29 : "九筒"
    # 字
    , 90 : "字", 91 : "红中", 92 : "发财", 93 : "白板"
}

g_CheckList = (
    (CardType.TONG.value, CardType.TONG_1.value, CardType.TONG_9.value)
    , (CardType.TIAO.value, CardType.TIAO_1.value, CardType.TIAO_9.value)
)