1261 CONSTANT Jewel_of_darkness
39 CONSTANT deDarkWizard_ClassId

: to_deDarkWizard
    player@ level@ 20 < if
        "You have not enough level" .
        exit
    then
  Jewel_of_darkness player@ inventory? 0 > if
		Jewel_of_darkness 1 player@ inventory-! drop
		deDarkWizard_ClassId player@ class!
		exit
	then
;
