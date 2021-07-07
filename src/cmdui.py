g_CMDUI = """\
              |---------------------北--------------------|
              | CPQ001 CPQ002 CPQ003 CPQ004 CPQ005 CPQ006 |
              |                                           |
              | CPQ007 CPQ008 CPQ009 CPQ010 CPQ011 CPQ012 |
玩家：Test001 |                                           |  玩家：Test003
              | CPQ013 CPQ014 CPQ015 CPQ016 CPQ017 CPQ018 |             
手牌数: CARDS1|                                           |  手牌数: CARDS3
              | CPQ019 CPQ020 CPQ021 CPQ022 CPQ023 CPQ024 |
碰牌:         |                                           |  碰牌: 
   PP11 PP12 西 CPQ025 CPQ026 CPQ027 CPQ028 CPQ029 CPQ030 东    PP31 PP32
   PP13 PP14  |                                           |     PP33 PP34
杠牌:         | CPQ031 CPQ032 CPQ033 CPQ034 CPQ035 CPQ036 |  杠牌:
   GP11 GP12  |                                           |     GP31 GP32
   GP13 GP14  | CPQ037 CPQ038 CPQ039 CPQ040 CPQ041 CPQ042 |     GP33 GP34
              |                                           |
              | CPQ043 CPQ044 CPQ045                      | 
              |---------------------南--------------------|

                      玩家：Test002     手牌数:CARDS2
                      碰牌：PP21 PP22 PP23 PP24
                      杠牌：GP21 GP22 GP23 GP24
${GameLog1}
${GameLog2}
${GameLog3}
"""

# 渲染命令行界面
def RendenerCmdGui(dInfo, dUsedCard, sLogList = None):
    sGui = g_CMDUI
    for i in range(1, 4):
        # 渲染玩家数据
        sGui = sGui.replace("Test00%s"%(i), dInfo[i]["Name"].ljust(7, " "))
        sGui = sGui.replace("CARDS%s"%(i), str(dInfo[i]["Cards"]).ljust(6, " "))
       
        # 渲染碰牌数据
        for iPengIndex in range(1, 5):
            if iPengIndex > len(dInfo[i]["Peng"]):
                sPeng = "    "
            else:
                sPeng = dInfo[i]["Peng"][iPengIndex - 1]
            sGui = sGui.replace("PP%s%s"%(i, iPengIndex), sPeng)
            
        # 渲染杠牌数据
        for iGangIndex in range(1, 5):
            if iGangIndex > len(dInfo[i]["Gang"]):
                sGang = "    "
            else:
                sGang = dInfo[i]["Gang"][iGangIndex - 1]
            sGui = sGui.replace("GP%s%s"%(i, iGangIndex), sGang)

    # 渲染已经打出的牌的数据
    for i in range(0, 45):
        sIndex = str(i + 1).rjust(3, "0")
        if i >= len(dUsedCard):
            sCard = "    "
        else:
            sCard = dUsedCard[i]
        sGui = sGui.replace("CPQ%s "%sIndex, " %s  "%sCard)

    # 渲染游戏日志
    for i in range(1, 4):
        if sLogList == None or 3 > len(sLogList):
            sGui = sGui.replace("${GameLog%s}"%i, "")
        else:
            sHead = "[Msg] "
            if 1 == i:
                sHead = "[New] "
            sGui = sGui.replace("${GameLog%s}"%i, sHead + sLogList[i - 1])

    return sGui

def CleanScreen():
    import os, sys
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")