# Created by Ham Wong on 2007.02.28
import sys

from net.sf.l2j.gameserver.model.quest        import State
from net.sf.l2j.gameserver.model.quest        import QuestState
from net.sf.l2j.gameserver.model.quest.jython import QuestJython as JQuest


NPC=[30006,30059,30080,30134,30146,30177,30233,30256,30320,30540,30576,30836,30848,30878,30899,31275,31320,31964]

class Quest (JQuest) :

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

 def onTalk (Self,npc,st):
    if st.getPlayer().isNoble() == 1 :
      htmltext="noble.htm"
    else :
      htmltext="nobleteleporter-no.htm"
    st.exitQuest(1)
    return htmltext

QUEST       = Quest(2000,"2000_NoblesseTeleport","Teleports")
CREATED     = State('Start', QUEST)

QUEST.setInitialState(CREATED)

for item in NPC:
   QUEST.addStartNpc(item)
   CREATED.addTalkId(item)

print "importing teleport data: 2000_NoblesseTeleport"
