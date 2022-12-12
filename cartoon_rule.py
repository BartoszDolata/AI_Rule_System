def get_rules():
    RULE = [
        """
        (defrule cartoon-finder_rule
          =>
          (bind ?answer (polar-question "A cartoon based on video game?"))
          (assert (based_on_game ?answer)))
        """,
        """
        (defrule nintendo_fernichise_rule
          (based_on_game "Yes")
          =>
          (bind ?answer (polar-question "A Nintendo fernichse?"))
          (assert (nintendo_fernichse ?answer)))
        """,
        """
        (defrule nintendo_fernichise_result 
        (based_on_game "Yes") 
        (nintendo_fernichse "Yes")
        => 
        (result "The Super Mario Bros Super Show, Capitan N The Game Master, The Adventures of Super Mario Bros. 3, Super Mario World, The Legend of Zelda, Pokemon"))
        """
        ,
        """
        (defrule no_nintendo_fernichise_result 
        (based_on_game "Yes") 
        (nintendo_fernichse "No")
        => 
        (result "Adventures of Sonic the Hedgehog, Mega Man, Mortal Kombat Fefenders of the Realm, Double Dragon, Wing Commander Academy, Street Fighter"))
        """,
        """
        (defrule celebrity_rule
          (based_on_game "No")
          =>
          (bind ?answer (polar-question "A celebrity?"))
          (assert (celebrity ?answer)))
        """,
        """
        (defrule celebrity_result
          (based_on_game "No")
          (celebrity "Yes")
          =>
          (result "Chuck Norris: Karate Kommandos, Mister T"))
        """


        ]
    return RULE;