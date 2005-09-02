#
# Created by DraX on 2005.08.15
#

import sys

from net.sf.l2j.gameserver.model.quest        import State
from net.sf.l2j.gameserver.model.quest        import QuestState
from net.sf.l2j.gameserver.model.quest.jython import QuestJython as JQuest

RING_OF_RAVEN_ID        = 1642
WAREHOUSE_CHIEF_MOKE    = 7498

class Quest (JQuest) :

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

 def onEvent (self,event,st):
   
   htmltext = event
   Race     = st.getPlayer().getRace()
   ClassId  = st.getPlayer().getClassId()
   Level    = st.getPlayer().getLevel()

   if event == "7498-01.htm":
     st.exitQuest(1)
     return "7498-01.htm"

   if event == "7498-02.htm":
     st.exitQuest(1)
     return "7498-02.htm"

   if event == "7498-03.htm":
     st.exitQuest(1)
     return "7498-03.htm"

   if event == "7498-04.htm":
     st.exitQuest(1)
     return "7498-04.htm"

   if event == "class_change_54":
     if ClassId in [ClassId.dwarvenFighter]:
        if Level <= 19 and st.getQuestItemsCount(RING_OF_RAVEN_ID) == 0:
          st.exitQuest(1)
          return "7498-05.htm"
        if Level <= 19 and st.getQuestItemsCount(RING_OF_RAVEN_ID) >= 1:
          st.exitQuest(1)
          return "7498-06.htm"
        if Level >= 20 and st.getQuestItemsCount(RING_OF_RAVEN_ID) == 0:
          st.exitQuest(1)
          return "7498-07.htm"
        if Level >= 20 and st.getQuestItemsCount(RING_OF_RAVEN_ID) >= 1:
          st.takeItems(RING_OF_RAVEN_ID,1)
          st.player.setClassId(54)
          st.player.broadcastUserInfo()
          st.playSound("ItemSound.quest_fanfare_2")
          st.exitQuest(1)
          return "7498-08.htm"

 def onTalk (Self,npcId,st):
   
   Race    = st.getPlayer().getRace()
   ClassId = st.getPlayer().getClassId()
   
   # Dwarf�s got accepted
   if npcId == WAREHOUSE_CHIEF_MOKE and Race in [Race.dwarf]:
     if ClassId in [ClassId.dwarvenFighter]:
       st.exitQuest(1)
       return "7498-01.htm"
     if ClassId in [ClassId.scavenger, ClassId.artisan]:
       st.exitQuest(1)
       return "7498-09.htm"
     if ClassId in [ClassId.bountyHunter, ClassId.warsmith]:
       st.exitQuest(1)
       return "7498-10.htm"

   # All other Races must be out
   if npcId == WAREHOUSE_CHIEF_MOKE and Race in [Race.elf, Race.darkelf, Race.orc, Race.human]:
     st.exitQuest(1)
     return "7498-11.htm"

QUEST   = Quest(7498,"7498_moke_occupation_change","village_master")
CREATED = State('Start',QUEST)

QUEST.setInitialState(CREATED)

QUEST.addStartNpc(7498)

STARTED.addTalkId(7498)