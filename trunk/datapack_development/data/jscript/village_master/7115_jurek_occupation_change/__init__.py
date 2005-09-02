#
# Created by DraX on 2005.08.23
#

print "importing village master data: Ivory Tower            ...done"

import sys

from net.sf.l2j.gameserver.model.quest        import State
from net.sf.l2j.gameserver.model.quest        import QuestState
from net.sf.l2j.gameserver.model.quest.jython import QuestJython as JQuest

MARK_OF_SCHOLAR_ID      = 2674
MARK_OF_TRUST_ID        = 2734
MARK_OF_MAGUS_ID        = 2840
MARK_OF_LIFE_ID         = 3140
MARK_OF_WITCHCRFAT_ID   = 3307
MARK_OF_SUMMONER_ID     = 3336
GRAND_MAGISTER_JUREK    = 7115
GRAND_MAGISTER_ARKENIAS = 7174
GRAND_MAGISTER_VALLERIA = 7176
GRAND_MAGISTER_SCRAIDE  = 7694
GRAND_MAGISTER_DRIKIYAN = 7854

class Quest (JQuest) :

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

 def onEvent (self,event,st):
   
   htmltext = event
   Race     = st.getPlayer().getRace()
   ClassId  = st.getPlayer().getClassId()
   Level    = st.getPlayer().getLevel()

   if event == "7115-01.htm":
     st.exitQuest(1)
     return "7115-01.htm"

   if event == "7115-02.htm":
     st.exitQuest(1)
     return "7115-02.htm"

   if event == "7115-03.htm":
     st.exitQuest(1)
     return "7115-03.htm"

   if event == "7115-04.htm":
     st.exitQuest(1)
     return "7115-04.htm"

   if event == "7115-05.htm":
     st.exitQuest(1)
     return "7115-05.htm"

   if event == "7115-06.htm":
     st.exitQuest(1)
     return "7115-06.htm"

   if event == "7115-07.htm":
     st.exitQuest(1)
     return "7115-07.htm"

   if event == "7115-08.htm":
     st.exitQuest(1)
     return "7115-08.htm"

   if event == "7115-09.htm":
     st.exitQuest(1)
     return "7115-09.htm"

   if event == "7115-10.htm":
     st.exitQuest(1)
     return "7115-10.htm"

   if event == "7115-11.htm":
     st.exitQuest(1)
     return "7115-11.htm"

   if event == "7115-12.htm":
     st.exitQuest(1)
     return "7115-12.htm"

   if event == "7115-13.htm":
     st.exitQuest(1)
     return "7115-13.htm"

   if event == "7115-14.htm":
     st.exitQuest(1)
     return "7115-14.htm"

   if event == "7115-15.htm":
     st.exitQuest(1)
     return "7115-15.htm"

   if event == "7115-16.htm":
     st.exitQuest(1)
     return "7115-16.htm"

   if event == "7115-17.htm":
     st.exitQuest(1)
     return "7115-17.htm"

   if event == "class_change_27":
     if ClassId in [ClassId.elvenWizard]:
        if Level <= 39:
          if st.getQuestItemsCount(MARK_OF_SCHOLAR_ID) == 0 or st.getQuestItemsCount(MARK_OF_LIFE_ID) == 0 or st.getQuestItemsCount(MARK_OF_MAGUS_ID) == 0:
            st.exitQuest(1)
            return "7115-18.htm"
          else:
            st.exitQuest(1)
            return "7115-19.htm"
        else:
          if st.getQuestItemsCount(MARK_OF_SCHOLAR_ID) == 0 or st.getQuestItemsCount(MARK_OF_LIFE_ID) == 0 or st.getQuestItemsCount(MARK_OF_MAGUS_ID) == 0:
            st.exitQuest(1)
            return "7115-20.htm"
          else:
            st.takeItems(MARK_OF_SCHOLAR_ID,1)
            st.takeItems(MARK_OF_LIFE_ID,1)
            st.takeItems(MARK_OF_MAGUS_ID,1)
            st.player.setClassId(27)
            st.player.broadcastUserInfo()
            st.playSound("ItemSound.quest_fanfare_2")
            st.exitQuest(1)
            return "7115-21.htm"

   if event == "class_change_28":
     if ClassId in [ClassId.elvenWizard]:
        if Level <= 39:
          if st.getQuestItemsCount(MARK_OF_SCHOLAR_ID) == 0 or st.getQuestItemsCount(MARK_OF_LIFE_ID) == 0 or st.getQuestItemsCount(MARK_OF_SUMMONER_ID) == 0:
            st.exitQuest(1)
            return "7115-22.htm"
          else:
            st.exitQuest(1)
            return "7115-23.htm"
        else:
          if st.getQuestItemsCount(MARK_OF_SCHOLAR_ID) == 0 or st.getQuestItemsCount(MARK_OF_LIFE_ID) == 0 or st.getQuestItemsCount(MARK_OF_SUMMONER_ID) == 0:
            st.exitQuest(1)
            return "7115-24.htm"
          else:
            st.takeItems(MARK_OF_SCHOLAR_ID,1)
            st.takeItems(MARK_OF_LIFE_ID,1)
            st.takeItems(MARK_OF_SUMMONER_ID,1)
            st.player.setClassId(28)
            st.player.broadcastUserInfo()
            st.playSound("ItemSound.quest_fanfare_2")
            st.exitQuest(1)
            return "7115-25.htm"

   if event == "class_change_12":
     if ClassId in [ClassId.wizard]:
        if Level <= 39:
          if st.getQuestItemsCount(MARK_OF_SCHOLAR_ID) == 0 or st.getQuestItemsCount(MARK_OF_TRUST_ID) == 0 or st.getQuestItemsCount(MARK_OF_MAGUS_ID) == 0:
            st.exitQuest(1)
            return "7115-26.htm"
          else:
            st.exitQuest(1)
            return "7115-27.htm"
        else:
          if st.getQuestItemsCount(MARK_OF_SCHOLAR_ID) == 0 or st.getQuestItemsCount(MARK_OF_TRUST_ID) == 0 or st.getQuestItemsCount(MARK_OF_MAGUS_ID) == 0:
            st.exitQuest(1)
            return "7115-28.htm"
          else:
            st.takeItems(MARK_OF_SCHOLAR_ID,1)
            st.takeItems(MARK_OF_TRUST_ID,1)
            st.takeItems(MARK_OF_MAGUS_ID,1)
            st.player.setClassId(12)
            st.player.broadcastUserInfo()
            st.playSound("ItemSound.quest_fanfare_2")
            st.exitQuest(1)
            return "7115-29.htm"

   if event == "class_change_13":
     if ClassId in [ClassId.wizard]:
        if Level <= 39:
          if st.getQuestItemsCount(MARK_OF_SCHOLAR_ID) == 0 or st.getQuestItemsCount(MARK_OF_TRUST_ID) == 0 or st.getQuestItemsCount(MARK_OF_WITCHCRFAT_ID) == 0:
            st.exitQuest(1)
            return "7115-30.htm"
          else:
            st.exitQuest(1)
            return "7115-31.htm"
        else:
          if st.getQuestItemsCount(MARK_OF_SCHOLAR_ID) == 0 or st.getQuestItemsCount(MARK_OF_TRUST_ID) == 0 or st.getQuestItemsCount(MARK_OF_WITCHCRFAT_ID) == 0:
            st.exitQuest(1)
            return "7115-32.htm"
          else:
            st.takeItems(MARK_OF_SCHOLAR_ID,1)
            st.takeItems(MARK_OF_TRUST_ID,1)
            st.takeItems(MARK_OF_WITCHCRFAT_ID,1)
            st.player.setClassId(13)
            st.player.broadcastUserInfo()
            st.playSound("ItemSound.quest_fanfare_2")
            st.exitQuest(1)
            return "7115-33.htm"

   if event == "class_change_14":
     if ClassId in [ClassId.wizard]:
        if Level <= 39:
          if st.getQuestItemsCount(MARK_OF_SCHOLAR_ID) == 0 or st.getQuestItemsCount(MARK_OF_TRUST_ID) == 0 or st.getQuestItemsCount(MARK_OF_SUMMONER_ID) == 0:
            st.exitQuest(1)
            return "7115-34.htm"
          else:
            st.exitQuest(1)
            return "7115-35.htm"
        else:
          if st.getQuestItemsCount(MARK_OF_SCHOLAR_ID) == 0 or st.getQuestItemsCount(MARK_OF_TRUST_ID) == 0 or st.getQuestItemsCount(MARK_OF_SUMMONER_ID) == 0:
            st.exitQuest(1)
            return "7115-36.htm"
          else:
            st.takeItems(MARK_OF_SCHOLAR_ID,1)
            st.takeItems(MARK_OF_TRUST_ID,1)
            st.takeItems(MARK_OF_SUMMONER_ID,1)
            st.player.setClassId(14)
            st.player.broadcastUserInfo()
            st.playSound("ItemSound.quest_fanfare_2")
            st.exitQuest(1)
            return "7115-37.htm"


 def onTalk (Self,npcId,st):
   
   Race    = st.getPlayer().getRace()
   ClassId = st.getPlayer().getClassId()
   
   # Elf�s and Humans�s got accepted
   if npcId == GRAND_MAGISTER_JUREK or GRAND_MAGISTER_SCRAIDE or GRAND_MAGISTER_DRIKIYAN or GRAND_MAGISTER_VALLERIA or GRAND_MAGISTER_ARKENIAS and Race in [Race.elf, Race.human]:
     if ClassId in [ClassId.elvenWizard]:
       st.exitQuest(1)
       return "7115-01.htm"
     elif ClassId in [ClassId.wizard]:
       st.exitQuest(1)
       return "7115-08.htm"
     elif ClassId in [ClassId.oracle, ClassId.cleric]:
       st.exitQuest(1)
       return "7115-40.htm"
     elif ClassId in [ClassId.elder, ClassId.bishop, ClassId.prophet, ClassId.plainsWalker]:
       st.exitQuest(1)
       return "7115-40.htm"
     elif ClassId in [ClassId.swordSinger, ClassId.silverRanger, ClassId.elvenKnight]:
       st.exitQuest(1)
       return "7115-40.htm"
     elif ClassId in [ClassId.sorceror, ClassId.necromancer, ClassId.warlock]:
       st.exitQuest(1)
       return "7115-39.htm"
     elif ClassId in [ClassId.spellsinger, ClassId.elementalSummoner]:
       st.exitQuest(1)
       return "7115-39.htm"
     elif ClassId in [ClassId.warrior, ClassId.knight, ClassId.rogue, ClassId.warlord, ClassId.paladin]:
       st.exitQuest(1)
       return "7115-40.htm"
     elif ClassId in [ClassId.treasureHunter, ClassId.gladiator, ClassId.darkAvenger, ClassId.hawkeye]:
       st.exitQuest(1)
       return "7115-40.htm"
     elif ClassId in [ClassId.fighter, ClassId.elvenFighter, ClassId.elvenScout, ClassId.templeKnight]:
       st.exitQuest(1)
       return "7115-40.htm"
     elif ClassId in [ClassId.elvenMage] or Race not in [Race.darkelf, Race.orc, Race.dwarf]:
       st.exitQuest(1)
       return "7115-38.htm"
     else:
       st.exitQuest(1)
       return "7115-40.htm"

   # All other Races must be out
   else:
     st.exitQuest(1)
     return "7115-40.htm"

QUEST   = Quest(7115,"7115_jurek_occupation_change","village_master")
CREATED = State('Start',QUEST)

QUEST.setInitialState(CREATED)

QUEST.addStartNpc(7115)
QUEST.addStartNpc(7174)
QUEST.addStartNpc(7176)
QUEST.addStartNpc(7694)
QUEST.addStartNpc(7854)

STARTED.addTalkId(7115)
STARTED.addTalkId(7174)
STARTED.addTalkId(7176)
STARTED.addTalkId(7694)
STARTED.addTalkId(7854)