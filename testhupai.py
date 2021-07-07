#encoding:utf-8
import pprint

from src.listener import CListener
from src.major import CCard \
, CCardsContainer, CardType \
, g_CardsMap, PrintCards, g_HuMap, HuType\
, CMahjongTable, CardStatus
 
# =================检查胡牌============= Begin ================

# 二万，三万，四万，五万，六万，七万，八万，九万，二筒，二筒，三条，三条，三条
Hupai_1 = {"Pai": (CardType.TONG_1
            , CardType.TONG_2
            , CardType.TONG_3
            , CardType.TONG_4
            , CardType.TONG_5
            , CardType.TONG_6
            , CardType.TONG_7
            , CardType.TONG_8
            , CardType.TONG_9
            , CardType.TONG_2
            , CardType.TONG_2
            , CardType.TIAO_3
            , CardType.TIAO_3
            , CardType.TIAO_3),
            "C": HuType.Normal
}

# 一万，一万，一筒，一筒，一条，一条，东，东，西，西，中，中，白，白 七小对
Hupai_3 = {"Pai": (CardType.TONG_1
            , CardType.TONG_1
            , CardType.TONG_5
            , CardType.TONG_5
            , CardType.TIAO_1
            , CardType.TIAO_1
            , CardType.TIAO_2
            , CardType.TIAO_2
            , CardType.TIAO_3
            , CardType.TIAO_3
            , CardType.ZHONG
            , CardType.ZHONG
            , CardType.BAI
            , CardType.BAI),
            "C": HuType.SevenPairs
}

Hupai_4 = {"Pai": (
    (CardType.TONG_3, CardStatus.Null)
    , (CardType.TONG_5, CardStatus.Peng)
    , (CardType.TONG_5, CardStatus.Peng)
    , (CardType.TONG_5, CardStatus.Peng)
    , (CardType.TONG_6, CardStatus.Peng)
    , (CardType.TONG_6, CardStatus.Peng)
    , (CardType.TONG_6, CardStatus.Peng)
    , (CardType.TIAO_3, CardStatus.Null)
    , (CardType.TIAO_4, CardStatus.Null)
    , (CardType.TIAO_5, CardStatus.Null)
    , (CardType.TIAO_6, CardStatus.Gang)
    , (CardType.TIAO_6, CardStatus.Gang)
    , (CardType.TIAO_6, CardStatus.Gang)
    , (CardType.TIAO_6, CardStatus.Gang)
    ),
    "C": HuType.NotComplete
}
# =================检查听牌============= Begin ================

# 一万，一万，一筒，一筒，一条，一条，东，东，西，西，中，中，白 缺一个 七小对
class TestTing1:
    m_Cards = (CardType.TONG_1
            , CardType.TONG_1
            , CardType.TONG_1
            , CardType.TONG_1
            , CardType.TIAO_1
            , CardType.TIAO_1
            , CardType.TIAO_2
            , CardType.TIAO_2
            , CardType.TIAO_3
            , CardType.TIAO_3
            , CardType.ZHONG
            , CardType.ZHONG
            , CardType.BAI)
    m_Needs = [CardType.BAI, ]

# 一万，九万，一筒，九筒，一条，东，南，西，北，中，发，白，白  缺个9条，国士无双，十三幺
class TestTing2:
    m_Cards = (CardType.TONG_1
            , CardType.TONG_9
            , CardType.TONG_1
            , CardType.TONG_9
            , CardType.TIAO_1
            , CardType.TIAO_2
            , CardType.TIAO_2
            , CardType.TIAO_3
            , CardType.TIAO_3
            , CardType.ZHONG
            , CardType.FA
            , CardType.BAI
            , CardType.BAI)
    m_Needs = [CardType.TIAO_9,]

# 一万，九万，一筒，九筒，一条，东，南，西，北，中，发，白，白  缺个9条，国士无双，十三幺
class TestTing3:
    m_Cards = (CardType.TONG_3
            , CardType.TONG_4
            , CardType.TONG_9
            , CardType.TONG_9
            , CardType.TIAO_1
            , CardType.TIAO_2
            , CardType.TIAO_3
            , CardType.TIAO_5
            , CardType.TIAO_5
            , CardType.TIAO_5
            , CardType.BAI
            , CardType.BAI
            , CardType.BAI)
    m_Needs = [CardType.TONG_2, CardType.TONG_5]

class TestTing4:
    m_Cards = (
            CardType.TONG_3
            , CardType.TONG_4
            , CardType.TONG_5
            , CardType.TONG_9
            , CardType.TONG_9
            , CardType.TIAO_1
            , CardType.TIAO_2
            , CardType.TIAO_3
            , CardType.TIAO_5
            , CardType.TIAO_5
            , CardType.TIAO_5
            , CardType.BAI
            , CardType.BAI
            )
    m_Needs = [CardType.TONG_9, CardType.BAI]

def DebugPrintCards(contai):
    print("牌数:%s"%contai.m_Count)
    print("{")
    for k in contai.m_Cards.keys():
        print("    %s: {"%(g_CardsMap[k]))
        for k1 in contai.m_Cards[k].keys():
            sList = []
            for oCard in contai.m_Cards[k][k1]:
                sList.append(g_CardsMap[oCard.Value()])
            print("        %s: %s,"%(k1, sList))
        print("    },")
    print("}")

contai = CCardsContainer()

for dInfo in (Hupai_1, Hupai_3, Hupai_4):
    cards = dInfo["Pai"]
    ctype = dInfo["C"]
    contai.Cleanup()
    ganglist = []
    penglist = []
    for cardinfo in cards:
        if type(cardinfo) == tuple:
            card = cardinfo[0]
            if cardinfo[1] == CardStatus.Peng:
                penglist.append(card)
            elif cardinfo[1] == CardStatus.Gang:
                ganglist.append(card)
        else:
            card = cardinfo
        contai.AddCard(CCard(card))
    for pc in penglist:
        contai.Peng(pc)
    for gc in ganglist:
        contai.Gang(gc)
    if type(cards[0]) == tuple:
        contai.AddCard(CCard(CardType.TONG_5))
    ret = contai.CheckCompleted()
    PrintCards(contai.m_Cards)
    if ret == ctype:
        rls = True
    else:
        rls = False
    print("|---------------------------------------------------------------------|")
    print(str("结果:%s 测试通过:%s"%(g_HuMap[ret], rls)).rjust(40, " "))
    print("|---------------------------------------------------------------------|\n")


for testcls in (TestTing1, TestTing2, TestTing3, TestTing4):
    contai.Cleanup()
    for card in testcls.m_Cards:
        contai.AddCard(CCard(card))
    PrintCards(contai.m_Cards)
    sResult = ""
    oCards = contai.GetListenCard()
    for oCard in oCards:
        if sResult:
            sResult += ", "
        sResult += g_CardsMap[oCard.value]
    rls = True
    for ctype in testcls.m_Needs:
        if ctype in oCards:
            continue
        rls = False
    print("听牌：", sResult, "测试结果:", rls)