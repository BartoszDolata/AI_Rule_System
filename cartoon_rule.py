def get_rules():
    RULE = [
        """
        (defrule start
          =>
          (show "Welcome in Cartoons' System. We want to get an answer for a question:What 80s/90s cartoon should I watch?")
          (assert (start)))
        """,
        """
        (defrule cartoon-finder_rule
          (start)
          =>
          (bind ?answer (polar-question "A cartoon based on video game?"))
          (assert (based-on-game ?answer)))
        """,
        """
        (defrule nintendo_fernichise_rule
          (based-on-game "Yes")
          =>
          (bind ?answer (polar-question "A Nintendo fernichse?"))
          (assert (nintendo_fernichse ?answer)))
        """,
        """
        (defrule nintendo_fernichise_result 
        (based-on-game "Yes") 
        (nintendo_fernichse "Yes")
        => 
        (result "The Super Mario Bros Super Show, Capitan N The Game Master, The Adventures of Super Mario Bros. 3, Super Mario World, The Legend of Zelda, Pokemon"))
        """
        ,
        """
        (defrule no_nintendo_fernichise_result 
        (based-on-game "Yes") 
        (nintendo_fernichse "No")
        => 
        (result "Adventures of Sonic the Hedgehog, Mega Man, Mortal Kombat Fefenders of the Realm, Double Dragon, Wing Commander Academy, Street Fighter"))
        """,
        """
        (defrule celebrity_rule
          (based-on-game "No")
          =>
          (bind ?answer (polar-question "A celebrity?"))
          (assert (celebrity ?answer)))
        """,
        """
        (defrule celebrity_result
          (based-on-game "No")
          (celebrity "Yes")
          =>
          (result "Chuck Norris: Karate Kommandos, Mister T"))
        """
        ,
        """
        (defrule animal_furries_rule
          (based-on-game "No")
          (celebrity "No")
          =>
            (bind ?answer (polar-question "Animal furries, and the like?"))
            (assert (animal-furies ?answer)))
        """
        ,
        """
        (defrule cats_rule
          (based-on-game "No")
          (celebrity "No")
          (animal-furies "Yes")
          =>
            (bind ?answer (polar-question "Cats?"))
            (assert (cats ?answer)))
        """
        ,
        """
        (defrule cats_result
          (based-on-game "No")
          (celebrity "No")
          (animal-furies "Yes")
          (cats "Yes")
          =>
            (result "ThunderCats, Swat Kats"))
        """
        ,
        """
        (defrule rodents_rule
          (based-on-game "No")
          (celebrity "No")
          (animal-furies "Yes")
          (cats "No")
          =>
            (bind ?answer (polar-question "Rodents?"))
            (assert (rodents ?answer)))
        """
        ,
        """
        (defrule rodents_result
          (based-on-game "No")
          (celebrity "No")
          (animal-furies "Yes")
          (cats "No")
          (rodents "Yes")
          =>
            (result "Biker Mice from Mars, Danger Mause, Chip N Dale Rescue Rangers"))
        """
        ,
        """
        (defrule dinosaurs_rule
          (based-on-game "No")
          (celebrity "No")
          (animal-furies "Yes")
          (cats "No")
          (rodents "No")
          =>
            (bind ?answer (polar-question "Dinosaurs?"))
            (assert (dinosaurs ?answer)))
        """
        ,
        """
        (defrule dinosaurs_result
          (based-on-game "No")
          (celebrity "No")
          (animal-furies "Yes")
          (cats "No")
          (rodents "No")
          (dinosaurs "Yes")
          =>
            (result "Cadilacs and Dinosaurs, Extreme Dinosaurs, Dino Riders, Dinosausers"))
        """
        ,
        """
        (defrule duck_rule
          (based-on-game "No")
          (celebrity "No")
          (animal-furies "Yes")
          (cats "No")
          (rodents "No")
          (dinosaurs "No")
          =>
            (bind ?answer (polar-question "Ducks?"))
            (assert (ducks ?answer)))
        """
        ,
        """
        (defrule ducks_result
          (based-on-game "No")
          (celebrity "No")
          (animal-furies "Yes")
          (cats "No")
          (rodents "No")
          (dinosaurs "No")
          (ducks "Yes")
          =>
            (result "Count Duckula, DuckTales, Darkwing Duck"))
        """
        ,
        """
        (defrule bear_rule
          (based-on-game "No")
          (celebrity "No")
          (animal-furies "Yes")
          (cats "No")
          (rodents "No")
          (dinosaurs "No")
          (ducks "No")
          =>
            (bind ?answer (polar-question "Bears?"))
            (assert (bears ?answer)))
        """
        ,
        """
        (defrule ducks_result
          (based-on-game "No")
          (celebrity "No")
          (animal-furies "Yes")
          (cats "No")
          (rodents "No")
          (dinosaurs "No")
          (ducks "No")
          (bears "Yes")
          =>
            (result "TaleSpin, Disney's Adventurs of the Gummi Bears"))
        """
        ,
        """
        (defrule monkeys_rule
          (based-on-game "No")
          (celebrity "No")
          (animal-furies "Yes")
          (cats "No")
          (rodents "No")
          (dinosaurs "No")
          (ducks "No")
          (bears "No")
          =>
            (bind ?answer (polar-question "Monkeys?"))
            (assert (monkeys ?answer)))
        """
        ,
        """
        (defrule monkeys_result
          (based-on-game "No")
          (celebrity "No")
          (animal-furies "Yes")
          (cats "No")
          (rodents "No")
          (dinosaurs "No")
          (ducks "No")
          (bears "No")
          (monkeys "Yes")
          =>
            (result "Capitan Simian and the Space Mokeys"))
        """
        ,
        """
        (defrule cows_rule
          (based-on-game "No")
          (celebrity "No")
          (animal-furies "Yes")
          (cats "No")
          (rodents "No")
          (dinosaurs "No")
          (ducks "No")
          (monkeys "No")
          =>
            (bind ?answer (polar-question "Cows?"))
            (assert (cows ?answer)))
        """
        ,
        """
        (defrule cows_result
          (based-on-game "No")
          (celebrity "No")
          (animal-furies "Yes")
          (cats "No")
          (rodents "No")
          (dinosaurs "No")
          (ducks "No")
          (bears "No")
          (cows "Yes")
          =>
            (result "Wild West Cowboys of Moo Mesa"))
        """
        ,
        """
        (defrule godless_abominations_rule
          (based-on-game "No")
          (celebrity "No")
          (animal-furies "Yes")
          (cats "No")
          (rodents "No")
          (dinosaurs "No")
          (ducks "No")
          (monkeys "No")
          (cows "No")
          =>
            (bind ?answer (polar-question "Godless abominations?"))
            (assert (godless-ab ?answer)))
        """
        ,
        """
        (defrule godless_abominations_result_n
          (based-on-game "No")
          (celebrity "No")
          (animal-furies "Yes")
          (cats "No")
          (rodents "No")
          (dinosaurs "No")
          (ducks "No")
          (bears "No")
          (cows "No")
          (godless-ab "No")
          =>
            (result "Teenage Mutant Ninja Turtles, Street Sharks, Gorgoyles"))
        """
        ,
        """
        (defrule godless_abominations_result
          (based-on-game "No")
          (celebrity "No")
          (animal-furies "Yes")
          (cats "No")
          (rodents "No")
          (dinosaurs "No")
          (ducks "No")
          (bears "No")
          (cows "No")
          (godless-ab "Yes")
          =>
            (result "Smurfs, Snorks"))
        """
        ,
        """
        (defrule dig-robots_rule
          (based-on-game "No")
          (celebrity "No")
          (animal-furies "No")
          =>
            (bind ?answer (polar-question "Do you dig giant robots?"))
            (assert (dig-robots ?answer)))
        """
        ,
        """
        (defrule dig-robots_result
          (based-on-game "No")
          (celebrity "No")
          (animal-furies "No")
          (dig-robots "Yes")
          =>
            (result "Robotech, Voltron, Transformers, Change of the GoBots"))
        """
        ,
        """
        (defrule cartoon_movie_based_rule
          (based-on-game "No")
          (celebrity "No")
          (animal-furies "No")
          (dig-robots "No")
          =>
            (bind ?answer (polar-question "A cartoon based on a movie?"))
            (assert (movie-based ?answer)))
        """
        ,
        """
        (defrule movie_rrated_rule
          (based-on-game "No")
          (celebrity "No")
          (animal-furies "No")
          (dig-robots "No")
          (movie-based "Yes")
          =>
            (bind ?answer (polar-question "A R-rated movie?"))
            (assert (movie-r-rated ?answer)))
        """
        ,
        """
        (defrule r_rated_result_no
          (based-on-game "No")
          (celebrity "No")
          (animal-furies "No")
          (dig-robots "No")
          (movie-based "Yes")
          (movie-r-rated "No")
          =>
            (result "Star Wars: Ewoks, Star Wars: Droids, Extreme Ghostbusters, James Bond Jr., The Real Ghostbusters"))
        """
        ,
        """
        (defrule r_rated_result_yes
          (based-on-game "No")
          (celebrity "No")
          (animal-furies "No")
          (dig-robots "No")
          (movie-based "Yes")
          (movie-r-rated "Yes")
          =>
            (result "Rambo and the Force of Freedom, Robocop: The Animated Series, Highlander: The Animated Series"))
        """

        ,
        """
        (defrule post_apocaliptic_rule
          (based-on-game "No")
          (celebrity "No")
          (animal-furies "No")
          (dig-robots "No")
          (movie-based "No")
          =>
            (bind ?answer (polar-question "Do you want a post-apocalyptic setting?"))
            (assert (post-apocaliptic ?answer)))
        """
        ,
        """
        (defrule post_apocaliptic_result
          (based-on-game "No")
          (celebrity "No")
          (animal-furies "No")
          (dig-robots "No")
          (movie-based "No")
          (post-apocaliptic "Yes")
          =>
            (result "Highlander: The Animated Series, Cadillacs and Dinosaurs, Thundarr the Barbarian, Spiral Zone"))
        """
        ,
        """
        (defrule sword_sorcery_rule
          (based-on-game "No")
          (celebrity "No")
          (animal-furies "No")
          (dig-robots "No")
          (movie-based "No")
          (post-apocaliptic "No")
          =>
          (bind ?answer (polar-question "Swords and sorcery?"))
          (assert (sword-sorcery ?answer)))
        """
        ,
        """
       (defrule sword_sorcery_result
         (based-on-game "No")
         (celebrity "No")
         (animal-furies "No")
         (dig-robots "No")
         (movie-based "No")
         (post-apocaliptic "No")
         (sword-sorcery "Yes")
         =>
         (result "The Pirates of Dark Water, Thundarr the Barabian, Visionaries, Dungeon & Dragons, She-Ra. Princess of Power, He-Man and Masters of the Universe, King Arthur and the Kights of Justice"))
       """
        ,
        """
       (defrule military_law_enforcement_rule
         (based-on-game "No")
         (celebrity "No")
         (animal-furies "No")
         (dig-robots "No")
         (movie-based "No")
         (post-apocaliptic "No")
         (sword-sorcery "No")
         =>
         (bind ?answer (polar-question "Military and law enforcement?"))
         (assert (military-law ?answer)))
        """
        ,
        """
       (defrule military_law_enforcement_result
         (based-on-game "No")
         (celebrity "No")
         (animal-furies "No")
         (dig-robots "No")
         (movie-based "No")
         (post-apocaliptic "No")
         (sword-sorcery "No")
         (military-law "Yes")
         =>
         (result "Rambo and the Force of Freedom, Roocop: The Animated Series, M.A.S.K, G.I. Joe, C.O.P.S., Exosquad, Spiral Zone, SilverHawks, Centurions, Sky Commanders, Sam & Max: Freelance Police, Inspector Gadget, The Adventures of the Galaxy Rangers, Brave Starr"))
        """
        ,
        """
              (defrule space_rule
                (based-on-game "No")
                (celebrity "No")
                (animal-furies "No")
                (dig-robots "No")
                (movie-based "No")
                (post-apocaliptic "No")
                (sword-sorcery "No")
                (military-law "No")
                =>
                (bind ?answer (polar-question "Space?"))
                (assert (space ?answer)))
               """
        ,
        """
       (defrule space_result
         (based-on-game "No")
         (celebrity "No")
         (animal-furies "No")
         (dig-robots "No")
         (movie-based "No")
         (post-apocaliptic "No")
         (sword-sorcery "No")
         (military-law "No")
         (space "Yes")
         =>
         (result "Capitan Simian and the Space Mokeys, Jayce and the Wheeled Warriors, Exosquad, SilverHawks, The Adventures of the Galaxy Rangers, Brave Starr"))
        """
        ,
        """
          (defrule cowboys
            (based-on-game "No")
            (celebrity "No")
            (animal-furies "No")
            (dig-robots "No")
            (movie-based "No")
            (post-apocaliptic "No")
            (sword-sorcery "No")
            (military-law "No")
            (space "No")
            =>
            (bind ?answer (polar-question "Cowboys?"))
            (assert (cowboys ?answer)))
           """
        ,
        """
       (defrule cowboys_result
         (based-on-game "No")
         (celebrity "No")
         (animal-furies "No")
         (dig-robots "No")
         (movie-based "No")
         (post-apocaliptic "No")
         (sword-sorcery "No")
         (military-law "No")
         (space "No")
         (cowboys "Yes")
         =>
         (result "Wild West Cowboys of Moo Mesa, The Adventures of the Galaxy Rangers, Brave Starr"))
        """
        ,
        """
      (defrule understand_rule
        (based-on-game "No")
         (celebrity "No")
         (animal-furies "No")
         (dig-robots "No")
         (movie-based "No")
         (post-apocaliptic "No")
         (sword-sorcery "No")
         (military-law "No")
         (space "No")
         (cowboys "No")
        =>
        (bind ?answer (polar-question "Do you want to understand what's going on?"))
        (assert (understand ?answer)))
       """
        ,
        """
      (defrule understand_rule_no
        (based-on-game "No")
        (celebrity "No")
        (animal-furies "No")
        (dig-robots "No")
        (movie-based "No")
        (post-apocaliptic "No")
        (sword-sorcery "No")
        (military-law "No")
        (space "No")
        (cowboys "No")
        (understand "No")
        =>
        (bind ?answer (polar-question "In an awesome way?"))
        (assert (way ?answer)))
        """
        ,
        """
      (defrule understand_rule_yes
        (based-on-game "No")
        (celebrity "No")
        (animal-furies "No")
        (dig-robots "No")
        (movie-based "No")
        (post-apocaliptic "No")
        (sword-sorcery "No")
        (military-law "No")
        (space "No")
        (cowboys "No")
        (understand "Yes")
        =>
        (bind ?answer (polar-question "Kids doing awesome stuff?"))
        (assert (kids-stuff ?answer)))
        """
        ,
        """
       (defrule way_result_no
         (based-on-game "No")
         (celebrity "No")
         (animal-furies "No")
         (dig-robots "No")
         (movie-based "No")
         (post-apocaliptic "No")
         (sword-sorcery "No")
         (military-law "No")
         (space "No")
         (cowboys "No")
         (way "No")
         =>
         (result "Inhumanoids"))
        """
        ,
        """
       (defrule way_result_yes
         (based-on-game "No")
         (celebrity "No")
         (animal-furies "No")
         (dig-robots "No")
         (movie-based "No")
         (post-apocaliptic "No")
         (sword-sorcery "No")
         (military-law "No")
         (space "No")
         (cowboys "No")
         (way "Yes")
         =>
         (result "Aeon Flux"))
        """
        ,
        """
      (defrule kids_stuff_rule_yes
        (based-on-game "No")
        (celebrity "No")
        (animal-furies "No")
        (dig-robots "No")
        (movie-based "No")
        (post-apocaliptic "No")
        (sword-sorcery "No")
        (military-law "No")
        (space "No")
        (cowboys "No")
        (understand "Yes")
        (kids-stuff "Yes")
        =>
        (bind ?answer (polar-question "In an educational manner?"))
        (assert (educational-manner ?answer)))
        """
        ,
        """
      (defrule kids_stuff_result_yes
        (based-on-game "No")
        (celebrity "No")
        (animal-furies "No")
        (dig-robots "No")
        (movie-based "No")
        (post-apocaliptic "No")
        (sword-sorcery "No")
        (military-law "No")
        (space "No")
        (cowboys "No")
        (understand "Yes")
        (kids-stuff "Yes")
        (educational-manner "Yes")
        =>
       (result "The Magic School Bus, Capitan Planet and the Planeteers"))
        """
        ,
        """
      (defrule kids_stuff_result_no
        (based-on-game "No")
        (celebrity "No")
        (animal-furies "No")
        (dig-robots "No")
        (movie-based "No")
        (post-apocaliptic "No")
        (sword-sorcery "No")
        (military-law "No")
        (space "No")
        (cowboys "No")
        (understand "Yes")
        (kids-stuff "Yes")
        (educational-manner "No")
        =>
       (result "Bionic Six, Mighty Max, The Real Adventures of Jonny Quest"))
        """
        ,
        """
      (defrule computers_rule
        (based-on-game "No")
        (celebrity "No")
        (animal-furies "No")
        (dig-robots "No")
        (movie-based "No")
        (post-apocaliptic "No")
        (sword-sorcery "No")
        (military-law "No")
        (space "No")
        (cowboys "No")
        (understand "Yes")
        (kids-stuff "No")
        =>
        (bind ?answer (polar-question "Do you like computers"))
        (assert (computers ?answer)))
        """
        ,
        """
      (defrule computers_result
        (based-on-game "No")
        (celebrity "No")
        (animal-furies "No")
        (dig-robots "No")
        (movie-based "No")
        (post-apocaliptic "No")
        (sword-sorcery "No")
        (military-law "No")
        (space "No")
        (cowboys "No")
        (understand "Yes")
        (kids-stuff "No")
        (computers "Yes")
        =>
       (result "ReBoot"))
        """
        ,
        """
      (defrule outrageous_rule
        (based-on-game "No")
        (celebrity "No")
        (animal-furies "No")
        (dig-robots "No")
        (movie-based "No")
        (post-apocaliptic "No")
        (sword-sorcery "No")
        (military-law "No")
        (space "No")
        (cowboys "No")
        (understand "Yes")
        (kids-stuff "No")
        (computers "No")
        =>
        (bind ?answer (polar-question "Something truly outrageous?"))
        (assert (outrageous ?answer)))
        """
        ,
        """
         (defrule outrageous_result
           (based-on-game "No")
           (celebrity "No")
           (animal-furies "No")
           (dig-robots "No")
           (movie-based "No")
           (post-apocaliptic "No")
           (sword-sorcery "No")
           (military-law "No")
           (space "No")
           (cowboys "No")
           (understand "Yes")
           (kids-stuff "No")
           (computers "No")
           (outrageous "Yes")
           =>
           (result "Jem"))
           """
        ,
        """
      (defrule undead_rule
        (based-on-game "No")
        (celebrity "No")
        (animal-furies "No")
        (dig-robots "No")
        (movie-based "No")
        (post-apocaliptic "No")
        (sword-sorcery "No")
        (military-law "No")
        (space "No")
        (cowboys "No")
        (understand "Yes")
        (kids-stuff "No")
        (computers "No")
        (outrageous "No")
        =>
        (bind ?answer (polar-question "The undead?"))
        (assert (undead ?answer)))
        """
        ,
        """
      (defrule undead_result_yes
        (based-on-game "No")
        (celebrity "No")
        (animal-furies "No")
        (dig-robots "No")
        (movie-based "No")
        (post-apocaliptic "No")
        (sword-sorcery "No")
        (military-law "No")
        (space "No")
        (cowboys "No")
        (understand "Yes")
        (kids-stuff "No")
        (computers "No")
        (outrageous "No")
        (undead "No")
        =>
        (result "The World of David the Gnome"))
        """
        ,
        """
      (defrule undead_result_yes
        (based-on-game "No")
        (celebrity "No")
        (animal-furies "No")
        (dig-robots "No")
        (movie-based "No")
        (post-apocaliptic "No")
        (sword-sorcery "No")
        (military-law "No")
        (space "No")
        (cowboys "No")
        (understand "Yes")
        (kids-stuff "No")
        (computers "No")
        (outrageous "No")
        (undead "Yes")
        =>
        (result "Mummies Alive, Skeleton Warriors"))
        """
    ]
    return RULE
