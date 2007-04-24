#
# Created by DraX on 2005.08.08
#

print "importing village master data: Gludin Village         ...done"

import sys

from net.sf.l2j.gameserver.model.quest        import State
from net.sf.l2j.gameserver.model.quest        import QuestState
from net.sf.l2j.gameserver.model.quest.jython import QuestJython as JQuest
qn = "30290_xenos_occupation_change"
GAZE_OF_ABYSS_ID     = 1244
IRON_HEART_ID        = 1252
JEWEL_OF_DARKNESS_ID = 1261
ORB_OF_ABYSS_ID      = 1270
GRAND_MASTER_XENOS   = 30290

class Quest (JQuest) :

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

 def onEvent (self,event,st):
   
   htmltext = "No Quest"
   
   Race     = st.getPlayer().getRace()
   ClassId  = st.getPlayer().getClassId()
   Level    = st.getPlayer().getLevel()

   if event == "30290-01.htm":
     return "30290-01.htm"

   if event == "30290-02.htm":
     return "30290-02.htm"

   if event == "30290-03.htm":
     return "30290-03.htm"

   if event == "30290-04.htm":
     return "30290-04.htm"

   if event == "30290-05.htm":
     return "30290-05.htm"

   if event == "30290-06.htm":
     return "30290-06.htm"

   if event == "30290-07.htm":
     return "30290-07.htm"

   if event == "30290-08.htm":
     return "30290-08.htm"

   if event == "30290-09.htm":
     return "30290-09.htm"

   if event == "30290-10.htm":
     return "30290-10.htm"

   if event == "30290-11.htm":
     return "30290-11.htm"

   if event == "30290-12.htm":
     return "30290-12.htm"

   if event == "30290-13.htm":
     return "30290-13.htm"

   if event == "30290-14.htm":
     return "30290-14.htm"

   if event == "class_change_32":
     if ClassId in [ClassId.darkFighter]:
        if Level <= 19 and st.getQuestItemsCount(GAZE_OF_ABYSS_ID) == 0:
          htmltext = "30290-15.htm"
        if Level <= 19 and st.getQuestItemsCount(GAZE_OF_ABYSS_ID) >= 1:
          htmltext = "30290-16.htm"
        if Level >= 20 and st.getQuestItemsCount(GAZE_OF_ABYSS_ID) == 0:
          htmltext = "30290-17.htm"
        if Level >= 20 and st.getQuestItemsCount(GAZE_OF_ABYSS_ID) >= 1:
          st.takeItems(GAZE_OF_ABYSS_ID,1)
          st.getPlayer().setClassId(32)
          st.getPlayer().setBaseClass(32)
          st.getPlayer().broadcastUserInfo()
          st.playSound("ItemSound.quest_fanfare_2")
          htmltext = "30290-18.htm"

   if event == "class_change_35":
     if ClassId in [ClassId.darkFighter]:
        if Level <= 19 and st.getQuestItemsCount(IRON_HEART_ID) == 0:
          htmltext = "30290-19.htm"
        if Level <= 19 and st.getQuestItemsCount(IRON_HEART_ID) >= 1:
          htmltext = "30290-20.htm"
        if Level >= 20 and st.getQuestItemsCount(IRON_HEART_ID) == 0:
          htmltext = "30290-21.htm"
        if Level >= 20 and st.getQuestItemsCount(IRON_HEART_ID) >= 1:
          st.takeItems(IRON_HEART_ID,1)
          st.getPlayer().setClassId(35)
          st.getPlayer().setBaseClass(35)
          st.getPlayer().broadcastUserInfo()
          st.playSound("ItemSound.quest_fanfare_2")
          htmltext = "30290-22.htm"

   if event == "class_change_39":
     if ClassId in [ClassId.darkMage]:
        if Level <= 19 and st.getQuestItemsCount(JEWEL_OF_DARKNESS_ID) == 0:
          htmltext = "30290-23.htm"
        if Level <= 19 and st.getQuestItemsCount(JEWEL_OF_DARKNESS_ID) >= 1:
          htmltext = "30290-24.htm"
        if Level >= 20 and st.getQuestItemsCount(JEWEL_OF_DARKNESS_ID) == 0:
          htmltext = "30290-25.htm"
        if Level >= 20 and st.getQuestItemsCount(JEWEL_OF_DARKNESS_ID) >= 1:
          st.takeItems(JEWEL_OF_DARKNESS_ID,1)
          st.getPlayer().setClassId(39)
          st.getPlayer().setBaseClass(39)
          st.getPlayer().broadcastUserInfo()
          st.playSound("ItemSound.quest_fanfare_2")
          htmltext = "30290-26.htm"

   if event == "class_change_42":
     if ClassId in [ClassId.darkMage]:
        if Level <= 19 and st.getQuestItemsCount(ORB_OF_ABYSS_ID) == 0:
          htmltext = "30290-27.htm"
        if Level <= 19 and st.getQuestItemsCount(ORB_OF_ABYSS_ID) >= 1:
          htmltext = "30290-28.htm"
        if Level >= 20 and st.getQuestItemsCount(ORB_OF_ABYSS_ID) == 0:
          htmltext = "30290-29.htm"
        if Level >= 20 and st.getQuestItemsCount(ORB_OF_ABYSS_ID) >= 1:
          st.takeItems(ORB_OF_ABYSS_ID,1)
          st.getPlayer().setClassId(42)
          st.getPlayer().setBaseClass(42)
          st.getPlayer().broadcastUserInfo()
          st.playSound("ItemSound.quest_fanfare_2")
          htmltext = "30290-30.htm"
          
   st.setState(COMPLETED)
   st.exitQuest(1)
   return htmltext


 def onTalk (Self,npc,player):
   st = player.getQuestState(qn)
   npcId = npc.getNpcId()
   
   Race    = st.getPlayer().getRace()
   ClassId = st.getPlayer().getClassId()
   
   # DarkElfs got accepted
   if npcId == GRAND_MASTER_XENOS and Race in [Race.darkelf]:
     if ClassId in [ClassId.darkFighter]:
       st.setState(STARTED)
       return "30290-01.htm"
     if ClassId in [ClassId.darkMage]:
       st.setState(STARTED)
       return "30290-08.htm"
     if ClassId in [ClassId.palusKnight, ClassId.assassin, ClassId.darkWizard, ClassId.shillienOracle]:
       st.setState(COMPLETED)
       st.exitQuest(1)
       return "30290-31.htm"
     if ClassId in [ClassId.shillienKnight, ClassId.abyssWalker, ClassId.bladedancer, ClassId.phantomRanger]:
       st.setState(COMPLETED)
       st.exitQuest(1)
       return "30290-32.htm"
     if ClassId in [ClassId.spellhowler, ClassId.shillenElder, ClassId.phantomSummoner]:
       st.setState(COMPLETED)
       st.exitQuest(1)
       return "30290-32.htm"

   # All other Races must be out
   if npcId == GRAND_MASTER_XENOS and Race in [Race.dwarf, Race.human, Race.elf, Race.orc]:
     st.setState(COMPLETED)
     st.exitQuest(1)
     return "30290-33.htm"

QUEST     = Quest(30290,qn,"village_master")
CREATED   = State('Start',     QUEST)
STARTED   = State('Started',   QUEST)
COMPLETED = State('Completed', QUEST)

QUEST.setInitialState(CREATED)

QUEST.addStartNpc(30290)

QUEST.addTalkId(30290)
