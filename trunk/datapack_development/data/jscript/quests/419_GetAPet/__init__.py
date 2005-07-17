#
# Quest generated by L2J Jython Quest generator V 0.43 Beta
#

print "importing quests: 419: Get a Pet"
import sys
from net.sf.l2j.gameserver.model.quest import State
from net.sf.l2j.gameserver.model.quest import QuestState
from net.sf.l2j.gameserver.model.quest.jython import QuestJython as JQuest

# variable definition part
POISON_SPIDER_LEG1 = 1173
POISON_SPIDER = 38
POISON_SPIDER_LEG1_DROP = 500000
WOLF_COLLAR = 2375
PET_MANAGER_MARTIN = 7731
ANIMAL_SLAYER_LIST1 = 3418

# Count Code part
def getCount_1173(st) :
  return st.getQuestItemsCount(POISON_SPIDER_LEG1)

# Complete code part
def completed(st) :
  st.setState(COMPLETED)
  st.clearQuestDrops()
  st.takeItems(POISON_SPIDER_LEG1,-1)
  st.giveItems(WOLF_COLLAR,1)
  st.addExpAndSp(5000,5000)
  st.exitQuest(True)
  return

def check(st) :
  if getCount_1173(st) >= 15 : 
    completed(st)
    return "<HTML><BODY>You''ve got all items, here is your reward</BODY></HTML>"
  return "<HTML><BODY>You don''t have enough item, continue your quest</BODY></HTML>"
# Condition check for the Quest
def st_check(st) :
  if st.getPlayer().getLevel() < 15 :
    st.exitQuest(True)
    return "<HTML><BODY>Sorry, your level is too low for this quest</BODY></HTML>"
  return "Start.htm"

# Main Quest Code
class Quest (JQuest):

  def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

  def onEvent (self,event,st):
    id = st.getState()
    if   id == CREATED  :
      if event == "agree" :
        st.setState(STARTED)
        st.set("cnt","0")
        return "<HTML><BODY>Quest initialized</BODY></HTML>"
      return st_check(st)
    elif id == COMPLETED: pass
    elif id == STARTED  :
      return check(st)
      return

  def onTalk (self,npcid,st):
    if npcid == PET_MANAGER_MARTIN : 
        st.giveItems(ANIMAL_SLAYER_LIST1,1)
    return

# Quest class and state definition
QUEST     = Quest(419, "419_GetAPet", "Wolf Collar")
CREATED   = State('Start',     QUEST)
STARTED   = State('Started',   QUEST)
COMPLETED = State('Completed', QUEST)
# Quest initialization
QUEST.setInitialState(CREATED)

# Quest NPC starter initialization
QUEST.addStartNpc(7731)

# Quest Item Drop initialization
STARTED.addQuestDrop(POISON_SPIDER,POISON_SPIDER_LEG1,POISON_SPIDER_LEG1_DROP)

# Quest mob initialization
STARTED.addKillId(POISON_SPIDER)

# Quest NPC initialization
STARTED.addTalkId(7731)
#
# L2J Jython Quest generator V 0.43 Beta created by LightofLife
#
