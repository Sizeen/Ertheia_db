### ---------------------------------------------------------------------------
### <history>
###		[TI]Blue blue@teamimprovision.com	7/26/2005	Created
### </history>
### ---------------------------------------------------------------------------

### Settings
NPC         = [7098]
QuestId     = 5002
QuestName   = "jewel"
QuestDesc   = "luxury_shop"
InitialHtml = "1.htm"

### Items - Format [name, giveItemId, giveItemQty, takeItem1Id, takeItem1Qty, takeItem2Id, takeItem2Qty]
Items       = [
["Moonstone Earring", 852, 1, 1459, 79, 1458, 195],
["Shield", 854, 1, 1459, 45, 1458, 370],
["Shield", 883, 1, 1459, 26, 1458, 130],
["Ring of Ages", 885, 1, 1459, 49, 1458, 245],
["Aquastone Necklace", 915, 1, 1459, 52, 1458, 260],
["Necklace of Mermaid", 917, 1, 1459, 99, 1458, 495]
]

### ---------------------------------------------------------------------------
### DO NOT MODIFY BELOW THIS LINE
### ---------------------------------------------------------------------------

print "importing " + QuestDesc + ": " + str(QuestId) + ": " + QuestName + ": " + str(len(Items)) + " item(s)",
import sys
from net.sf.l2j.gameserver.model.quest import State
from net.sf.l2j.gameserver.model.quest import QuestState
from net.sf.l2j.gameserver.model.quest.jython import QuestJython as JQuest

### doRequestedEvent
def do_RequestedEvent(event, st, giveItemId, giveItemQty, takeItem1Id, takeItem1Qty, takeItem2Id, takeItem2Qty) :
    if st.getQuestItemsCount(takeItem1Id) >= takeItem1Qty and st.getQuestItemsCount(takeItem2Id) >= takeItem2Qty :
        st.takeItems(takeItem1Id, takeItem1Qty)
        st.takeItems(takeItem2Id, takeItem2Qty)
        st.giveItems(giveItemId, giveItemQty)
        st.exitQuest(True)
        return event + ".htm" 
    else :
        return "You do not have enough crystals."

### main code
class Quest (JQuest) :

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

 def onEvent (self,event,st) :
    htmltext = event

    if event == "0":
        return InitialHtml

    for item in Items:
        if event == str(item[1]):
            htmltext = do_RequestedEvent(event, st, item[1], item[2], item[3], item[4], item[5], item[6])

    return htmltext

 def onTalk (Self,npcId,st):
   htmltext = "<html><head><body>I have nothing to say with you</body></html>"
   id = st.getState()
   if id == CREATED :
     st.setState(COMPLETED)
   return InitialHtml

### Quest class and state definition
QUEST       = Quest(QuestId,str(QuestId) + "_" + QuestName,QuestDesc)
CREATED     = State('Start',     QUEST)
STARTED     = State('Started',   QUEST)
COMPLETED   = State('Completed', QUEST)

### Quest initialization
QUEST.setInitialState(CREATED)

for item in NPC:
### Quest NPC starter initialization
   QUEST.addStartNpc(item)

### Quest NPC initialization
   STARTED.addTalkId(item)

print "...done"