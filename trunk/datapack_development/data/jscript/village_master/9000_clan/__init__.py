#
# Created by DraX on 2005.08.12
#

print "importing village master data: clan                   ...done"

import sys

from net.sf.l2j.gameserver.model.quest        import State
from net.sf.l2j.gameserver.model.quest        import QuestState
from net.sf.l2j.gameserver.model.quest.jython import QuestJython as JQuest

GRAND_MASTER_BITZ       = 7026
HIGH_PRIEST_BIOTIN      = 7031
HIGH_PRIESTESS_LEVIAN   = 7037
GRAND_MASTER_PABRIS     = 7066
HIGH_PRIEST_SYLVAIN     = 7070
GRAND_MASTER_HANNAVALT  = 7109
GRAND_MAGISTER_JUREK    = 7115
HIGH_PRIEST_MAXIMILIAN  = 7120
HIERARCH_ASTERIOS       = 7154
GRAND_MAGISTER_ARKENIAS = 7174
GRAND_MAGISTER_FAIREN   = 7175
GRAND_MAGISTER_VALLERIA = 7176
GRAND_MASTER_BLACKBIRD  = 7187
HIGH_PRIEST_HOLLINT     = 7191
GRAND_MASTER_BRECSON    = 7195
GRAND_MASTER_RAINS      = 7288
HIGH_PRIEST_RAYMOND     = 7289
GRAND_MASTER_XENOS      = 7290
GRAND_MASTER_TOBIAS     = 7297
TETRARCH_THIFIELL       = 7358
GRAND_MASTER_RAMOS      = 7373
GRAND_MASTER_TRONIX     = 7462
GRAND_MASTER_ANGUS      = 7474
WAREHOUSE_CHIEF_MOKE    = 7498
HEAD_BLACKSMITH_TAPOY   = 7499
HIGH_PREFECT_OSBORN     = 7500
WAREHOUSE_CHIEF_RIKADIO = 7503
HEAD_BLACKSMITH_MENDIO  = 7504
HIGH_PREFECT_DRIKUS     = 7505
HIGH_PREFECT_CASTOR     = 7508
WAREHOUSE_CHIEF_GESTO   = 7511
HEAD_BLACKSMITH_KUSTO   = 7512
HIGH_PREFECT_PENATUS    = 7513
WAREHOUSE_CHIEF_REED    = 7520
HEAD_BLACKSMITH_BRONK   = 7525
KAKAI_LORD_OF_FLAME     = 7565
WAREHOUSE_CHIEF_RANSPO  = 7594
HEAD_BLACKSMITH_OPIX    = 7595
WAREHOUSE_CHIEF_CROOP   = 7676
HEAD_BLACKSMITH_FLUTTER = 7677
HIGH_PREFECT_KARIA      = 7681
WAREHOUSE_CHIEF_BRAXT   = 7685
HEAD_BLACKSMITH_VERGARA = 7687
GRAND_MASTER_SIRIA      = 7689
GRAND_MAGISTER_SCRAIDE  = 7694
GRAND_MASTER_MEDOWN     = 7699
HIGH_PREFECT_GARVARENTZ = 7704
WAREHOUSE_CHIEF_KLUMP   = 7845
HEAD_BLACKSMITH_FERRIS  = 7847
GRAND_MASTER_SEDRICK    = 7849
GRAND_MAGISTER_DRIKIYAN = 7854
HIGH_PRIEST_ORVEN       = 7857
GRAND_MASTER_OLTLIN     = 7862
HIGH_PREFECT_LADANZA    = 7865
WAREHOUSE_CHIEF_NATOOLS = 7894
HEAD_BLACKSMITH_ROMAN   = 7897
GRAND_MASTER_MARCUS     = 7900
HIGH_PRIEST_SQUILLARI   = 7905
GRAND_MASTER_XAIRAKIN   = 7910
HIGH_PREFECT_TUSHKU     = 7913

class Quest (JQuest) :

 def onEvent (self,event,st):
   
   htmltext     = event
   Level        = st.getPlayer().getLevel()
   ClanLeader   = st.player.isClanLeader()
   PlayerinClan = st.player.getClanId()

   if event == "9000-01.htm":
     st.exitQuest(1)
     return "9000-01.htm"

   # Player must be Level 10 or above! (so cannot create clan)
   if event == "9000-02.htm" and Level <= 9:
     st.exitQuest(1)
     return "9000-06.htm"

   # player is always clanleader! (so cannot create clan)
   if event == "9000-02.htm" and ClanLeader == 1:
     st.exitQuest(1)
     return "9000-07.htm"

   # player is always in a clan! (so cannot create clan)
   if event == "9000-02.htm" and PlayerinClan != 0:
     st.exitQuest(1)
     return "9000-09.htm"
   
   # always shown the clan raise page!
   if event == "9000-03.htm":
     st.exitQuest(1)
     return "9000-03.htm"

   # player must be clanleader to dissolve clan!
   if event == "9000-04.htm" and ClanLeader == 1:
     st.exitQuest(1)
     return "9000-04.htm"

   # player must be clanleader to dissolve clan! 
   if event == "9000-04.htm" and PlayerinClan != 0:
     st.exitQuest(1)
     return "9000-08.htm"

   # player must be in a clan to dissolve clan! 
   if event == "9000-04.htm" and PlayerinClan == 0:
     st.exitQuest(1)
     return "9000-11.htm"

   if event == "9000-05.htm":
     st.exitQuest(1)
     return "9000-05.htm"

   else:
     st.exitQuest(1)
     return "9000-02.htm"

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

 def onTalk (Self,npcId,st):
   
   if npcId == GRAND_MASTER_TOBIAS or GRAND_MASTER_BITZ or HIGH_PRIEST_BIOTIN or HIERARCH_ASTERIOS or TETRARCH_THIFIELL or WAREHOUSE_CHIEF_REED or HEAD_BLACKSMITH_BRONK or KAKAI_LORD_OF_FLAME or GRAND_MASTER_RAINS or HIGH_PRIEST_RAYMOND or WAREHOUSE_CHIEF_RIKADIO or HEAD_BLACKSMITH_MENDIO or HIGH_PREFECT_DRIKUS or GRAND_MASTER_XENOS or GRAND_MASTER_RAMOS or HIGH_PRIESTESS_LEVIAN or WAREHOUSE_CHIEF_MOKE or HEAD_BLACKSMITH_TAPOY or HIGH_PREFECT_OSBORN or HIGH_PRIEST_SYLVAIN or GRAND_MASTER_TRONIX or GRAND_MASTER_PABRIS or HIGH_PREFECT_CASTOR or HEAD_BLACKSMITH_OPIX or WAREHOUSE_CHIEF_RANSPO or GRAND_MASTER_ANGUS or GRAND_MASTER_BRECSON or GRAND_MASTER_MEDOWN or GRAND_MASTER_OLTLIN or GRAND_MASTER_XAIRAKIN or HIGH_PREFECT_PENATUS or HIGH_PREFECT_GARVARENTZ or HIGH_PREFECT_KARIA or HIGH_PREFECT_LADANZA or HIGH_PREFECT_TUSHKU or WAREHOUSE_CHIEF_GESTO or WAREHOUSE_CHIEF_BRAXT or WAREHOUSE_CHIEF_CROOP or WAREHOUSE_CHIEF_KLUMP or WAREHOUSE_CHIEF_NATOOLS or HEAD_BLACKSMITH_KUSTO or HEAD_BLACKSMITH_VERGARA or HEAD_BLACKSMITH_FLUTTER or HEAD_BLACKSMITH_FERRIS or HEAD_BLACKSMITH_ROMAN or GRAND_MASTER_HANNAVALT or GRAND_MASTER_SIRIA or GRAND_MASTER_BLACKBIRD or GRAND_MASTER_SEDRICK or GRAND_MASTER_MARCUS or HIGH_PRIEST_MAXIMILIAN or HIGH_PRIEST_HOLLINT or HIGH_PRIEST_ORVEN or HIGH_PRIEST_SQUILLARI or GRAND_MAGISTER_JUREK or GRAND_MAGISTER_SCRAIDE or GRAND_MAGISTER_DRIKIYAN or GRAND_MAGISTER_VALLERIA or GRAND_MAGISTER_FAIREN or GRAND_MAGISTER_ARKENIAS:
     st.exitQuest(1)
     return "9000-01.htm"

QUEST   = Quest(9000,"9000_clan","village_master")
CREATED = State('Start',QUEST)

QUEST.setInitialState(CREATED)

QUEST.addStartNpc(7026)
QUEST.addStartNpc(7031)
QUEST.addStartNpc(7037)
QUEST.addStartNpc(7066)
QUEST.addStartNpc(7070)
QUEST.addStartNpc(7109)
QUEST.addStartNpc(7115)
QUEST.addStartNpc(7120)
QUEST.addStartNpc(7154)
QUEST.addStartNpc(7174)
QUEST.addStartNpc(7175)
QUEST.addStartNpc(7176)
QUEST.addStartNpc(7187)
QUEST.addStartNpc(7191)
QUEST.addStartNpc(7195)
QUEST.addStartNpc(7288)
QUEST.addStartNpc(7289)
QUEST.addStartNpc(7290)
QUEST.addStartNpc(7297)
QUEST.addStartNpc(7358)
QUEST.addStartNpc(7373)
QUEST.addStartNpc(7462)
QUEST.addStartNpc(7474)
QUEST.addStartNpc(7498)
QUEST.addStartNpc(7499)
QUEST.addStartNpc(7500)
QUEST.addStartNpc(7503)
QUEST.addStartNpc(7504)
QUEST.addStartNpc(7505)
QUEST.addStartNpc(7508)
QUEST.addStartNpc(7511)
QUEST.addStartNpc(7512)
QUEST.addStartNpc(7513)
QUEST.addStartNpc(7520)
QUEST.addStartNpc(7525)
QUEST.addStartNpc(7565)
QUEST.addStartNpc(7594)
QUEST.addStartNpc(7595)
QUEST.addStartNpc(7676)
QUEST.addStartNpc(7677)
QUEST.addStartNpc(7681)
QUEST.addStartNpc(7685)
QUEST.addStartNpc(7687)
QUEST.addStartNpc(7689)
QUEST.addStartNpc(7694)
QUEST.addStartNpc(7699)
QUEST.addStartNpc(7704)
QUEST.addStartNpc(7845)
QUEST.addStartNpc(7847)
QUEST.addStartNpc(7849)
QUEST.addStartNpc(7854)
QUEST.addStartNpc(7857)
QUEST.addStartNpc(7862)
QUEST.addStartNpc(7865)
QUEST.addStartNpc(7894)
QUEST.addStartNpc(7897)
QUEST.addStartNpc(7900)
QUEST.addStartNpc(7905)
QUEST.addStartNpc(7910)
QUEST.addStartNpc(7913)

STARTED.addTalkId(7026)
STARTED.addTalkId(7031)
STARTED.addTalkId(7037)
STARTED.addTalkId(7066)
STARTED.addTalkId(7070)
STARTED.addTalkId(7109)
STARTED.addTalkId(7115)
STARTED.addTalkId(7120)
STARTED.addTalkId(7154)
STARTED.addTalkId(7174)
STARTED.addTalkId(7175)
STARTED.addTalkId(7176)
STARTED.addTalkId(7187)
STARTED.addTalkId(7191)
STARTED.addTalkId(7195)
STARTED.addTalkId(7288)
STARTED.addTalkId(7289)
STARTED.addTalkId(7290)
STARTED.addTalkId(7297)
STARTED.addTalkId(7358)
STARTED.addTalkId(7373)
STARTED.addTalkId(7462)
STARTED.addTalkId(7474)
STARTED.addTalkId(7498)
STARTED.addTalkId(7499)
STARTED.addTalkId(7500)
STARTED.addTalkId(7503)
STARTED.addTalkId(7504)
STARTED.addTalkId(7505)
STARTED.addTalkId(7508)
STARTED.addTalkId(7511)
STARTED.addTalkId(7512)
STARTED.addTalkId(7513)
STARTED.addTalkId(7520)
STARTED.addTalkId(7525)
STARTED.addTalkId(7565)
STARTED.addTalkId(7594)
STARTED.addTalkId(7595)
STARTED.addTalkId(7676)
STARTED.addTalkId(7677)
STARTED.addTalkId(7681)
STARTED.addTalkId(7685)
STARTED.addTalkId(7687)
STARTED.addTalkId(7689)
STARTED.addTalkId(7694)
STARTED.addTalkId(7699)
STARTED.addTalkId(7704)
STARTED.addTalkId(7845)
STARTED.addTalkId(7847)
STARTED.addTalkId(7849)
STARTED.addTalkId(7854)
STARTED.addTalkId(7857)
STARTED.addTalkId(7862)
STARTED.addTalkId(7865)
STARTED.addTalkId(7894)
STARTED.addTalkId(7897)
STARTED.addTalkId(7900)
STARTED.addTalkId(7905)
STARTED.addTalkId(7910)
STARTED.addTalkId(7913)