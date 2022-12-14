;test 3 options

(defrule nintendo_fernichise_test
(based-on-game Yes)
(nintendo_fernichse IDK)
=>
(result "Test" "Passed")
)

(defrule start
=>
(show "Welcome in Cartoons' System. We want to get an answer for a question:What 80s/90s cartoon should I watch?")
(assert (start))
(assert (answers "Yes" "No"))

)


(defrule cartoon-finder_rule
(start)
(answers $?ans)
=>
(polar-question "A cartoon based on video game?" "based-on-game" $?ans)
)



(defrule nintendo_franchise_rule
(based-on-game Yes)
(answers $?ans)
=>
(polar-question "A Nintendo fernichse?" "nintendo_fernichse" $?ans)
)



(defrule nintendo_fernichise_result
(based-on-game Yes)
(nintendo_fernichse Yes)

=>
(result "The Super Mario Bros Super Show" "Capitan N The Game Master" "The Adventures of Super Mario Bros. 3" "Super Mario World" "The Legend of Zelda" "Pokemon")
)

(defrule no_nintendo_fernichise_result
(based-on-game Yes)
(nintendo_fernichse No)
=>
(result "Adventures of Sonic the Hedgehog" "Mega Man" "Mortal Kombat Fefenders of the Realm" "Double Dragon" "Wing Commander Academy" "Street Fighter"))

(defrule celebrity_rule
(based-on-game No)
(answers $?ans)
=>
(polar-question "A celebrity?" "celebrity" $?ans))


(defrule celebrity_result
(based-on-game No)
(celebrity Yes)
=>
(result "Chuck Norris: Karate Kommandos" "Mister T"))

(defrule animal_furries_rule
(based-on-game No)
(celebrity No)
(answers $?ans)
=>
(polar-question "Animal furries, and the like?" "animal-furies" $?ans))

(defrule cats_rule
(based-on-game No)
(celebrity No)
(animal-furies Yes)
(answers $?ans)
=>
(polar-question "Cats?" "cats" $?ans))

(defrule cats_result
(based-on-game No)
(celebrity No)
(animal-furies Yes)
(cats Yes)
=>
(result "ThunderCats" "Swat Kats"))

(defrule rodents_rule
(based-on-game No)
(celebrity No)
(animal-furies Yes)
(cats No)
(answers $?ans)
=>
(polar-question "Rodents?" "rodents" $?ans))

(defrule rodents_result
(based-on-game No)
(celebrity No)
(animal-furies Yes)
(cats No)
(rodents Yes)
=>
(result "Biker Mice from Mars" "Danger Mause" "Chip N Dale Rescue Rangers"))

(defrule dinosaurs_rule
(based-on-game No)
(celebrity No)
(animal-furies Yes)
(cats No)
(rodents No)
(answers $?ans)
=>
(polar-question "Dinosaurs?" "dinosaurs" $?ans))

(defrule dinosaurs_result
(based-on-game No)
(celebrity No)
(animal-furies Yes)
(cats No)
(rodents No)
(dinosaurs Yes)
=>
(result "Cadilacs and Dinosaurs" "Extreme Dinosaurs" "Dino Riders" "Dinosausers"))

(defrule duck_rule
(based-on-game No)
(celebrity No)
(animal-furies Yes)
(cats No)
(rodents No)
(dinosaurs No)
(answers $?ans)
=>
(polar-question "Ducks?" "ducks" $?ans))


(defrule ducks_result
(based-on-game No)
(celebrity No)
(animal-furies Yes)
(cats No)
(rodents No)
(dinosaurs No)
(ducks Yes)
=>
(result "Count Duckula" "DuckTales" "Darkwing Duck"))

(defrule bear_rule
(based-on-game No)
(celebrity No)
(animal-furies Yes)
(cats No)
(rodents No)
(dinosaurs No)
(ducks No)
(answers $?ans)
=>
(polar-question "Bears?" "bears" $?ans))


(defrule ducks_result
(based-on-game No)
(celebrity No)
(animal-furies Yes)
(cats No)
(rodents No)
(dinosaurs No)
(ducks No)
(bears Yes)
=>
(result "TaleSpin" "Disney's Adventurs of the Gummi Bears"))

(defrule monkeys_rule
(based-on-game No)
(celebrity No)
(animal-furies Yes)
(cats No)
(rodents No)
(dinosaurs No)
(ducks No)
(bears No)
(answers $?ans)
=>
(polar-question "Monkeys?" "monkeys" $?ans))


(defrule monkeys_result
(based-on-game No)
(celebrity No)
(animal-furies Yes)
(cats No)
(rodents No)
(dinosaurs No)
(ducks No)
(bears No)
(monkeys Yes)
=>
(result "Capitan Simian and the Space Mokeys"))

(defrule cows_rule
(based-on-game No)
(celebrity No)
(animal-furies Yes)
(cats No)
(rodents No)
(dinosaurs No)
(ducks No)
(monkeys No)
(answers $?ans)
=>
(polar-question "Cows?" "cows" $?ans))

(defrule cows_result
(based-on-game No)
(celebrity No)
(animal-furies Yes)
(cats No)
(rodents No)
(dinosaurs No)
(ducks No)
(bears No)
(cows Yes)
=>
(result "Wild West Cowboys of Moo Mesa"))

(defrule godless_abominations_rule
(based-on-game No)
(celebrity No)
(animal-furies Yes)
(cats No)
(rodents No)
(dinosaurs No)
(ducks No)
(monkeys No)
(cows No)
(answers $?ans)
=>
(polar-question "Godless abominations?" "godless-ab" $?ans))


(defrule godless_abominations_result_n
(based-on-game No)
(celebrity No)
(animal-furies Yes)
(cats No)
(rodents No)
(dinosaurs No)
(ducks No)
(bears No)
(cows No)
(godless-ab No)
=>
(result "Teenage Mutant Ninja Turtles" "Street Sharks" "Gorgoyles"))

(defrule godless_abominations_result
(based-on-game No)
(celebrity No)
(animal-furies Yes)
(cats No)
(rodents No)
(dinosaurs No)
(ducks No)
(bears No)
(cows No)
(godless-ab Yes)
=>
(result "Smurfs" "Snorks"))

(defrule dig-robots_rule
(based-on-game No)
(celebrity No)
(animal-furies No)
(answers $?ans)
=>
(polar-question "Do you dig giant robots?" "dig-robots" $?ans))


(defrule dig-robots_result
(based-on-game No)
(celebrity No)
(animal-furies No)
(dig-robots Yes)
=>
(result "Robotech" "Voltron" "Transformers" "Change of the GoBots"))

(defrule cartoon_movie_based_rule
(based-on-game No)
(celebrity No)
(animal-furies No)
(dig-robots No)
(answers $?ans)
=>
(polar-question "A cartoon based on a movie?" "movie-based" $?ans))


(defrule movie_rrated_rule
(based-on-game No)
(celebrity No)
(animal-furies No)
(dig-robots No)
(movie-based Yes)
(answers $?ans)
=>
(polar-question "A R-rated movie?" "movie-r-rated" $?ans))


(defrule r_rated_result_no
(based-on-game No)
(celebrity No)
(animal-furies No)
(dig-robots No)
(movie-based Yes)
(movie-r-rated No)
=>
(result "Star Wars: Ewoks" "Star Wars: Droids" "Extreme Ghostbusters" "James Bond Jr." "The Real Ghostbusters"))

(defrule r_rated_result_yes
(based-on-game No)
(celebrity No)
(animal-furies No)
(dig-robots No)
(movie-based Yes)
(movie-r-rated Yes)
=>
(result "Rambo and the Force of Freedom" "Robocop: The Animated Series" "Highlander: The Animated Series"))

(defrule post_apocaliptic_rule
(based-on-game No)
(celebrity No)
(animal-furies No)
(dig-robots No)
(movie-based No)
(answers $?ans)
=>
(polar-question "Do you want a post-apocalyptic setting?" "post-apocaliptic" $?ans))

(defrule post_apocaliptic_result
(based-on-game No)
(celebrity No)
(animal-furies No)
(dig-robots No)
(movie-based No)
(post-apocaliptic Yes)
=>
(result "Highlander: The Animated Series" "Cadillacs and Dinosaurs" "Thundarr the Barbarian" "Spiral Zone"))

(defrule sword_sorcery_rule
(based-on-game No)
(celebrity No)
(animal-furies No)
(dig-robots No)
(movie-based No)
(post-apocaliptic No)
(answers $?ans)
=>
(polar-question "Swords and sorcery?" "sword-sorcery" $?ans))


(defrule sword_sorcery_result
(based-on-game No)
(celebrity No)
(animal-furies No)
(dig-robots No)
(movie-based No)
(post-apocaliptic No)
(sword-sorcery Yes)
=>
(result "The Pirates of Dark Water" "Thundarr the Barabian" "Visionaries" "Dungeon & Dragons" "She-Ra. Princess of Power" "He-Man and Masters of the Universe" "King Arthur and the Kights of Justice"))

(defrule military_law_enforcement_rule
(based-on-game No)
(celebrity No)
(animal-furies No)
(dig-robots No)
(movie-based No)
(post-apocaliptic No)
(sword-sorcery No)
(answers $?ans)
=>
(polar-question "Military and law enforcement?" "military-law" $?ans))

(defrule military_law_enforcement_result
(based-on-game No)
(celebrity No)
(animal-furies No)
(dig-robots No)
(movie-based No)
(post-apocaliptic No)
(sword-sorcery No)
(military-law Yes)
=>
(result "Rambo and the Force of Freedom" "Roocop: The Animated Series" "M.A.S.K" "G.I. Joe" "C.O.P.S." "Exosquad" "Spiral Zone" "SilverHawks" "Centurions" "Sky Commanders" "Sam & Max: Freelance Police" "Inspector Gadget" "The Adventures of the Galaxy Rangers" "Brave Starr"))

(defrule space_rule
(based-on-game No)
(celebrity No)
(animal-furies No)
(dig-robots No)
(movie-based No)
(post-apocaliptic No)
(sword-sorcery No)
(military-law No)
(answers $?ans)
=>
(polar-question "Space?" "space" $?ans))



(defrule space_result
(based-on-game No)
(celebrity No)
(animal-furies No)
(dig-robots No)
(movie-based No)
(post-apocaliptic No)
(sword-sorcery No)
(military-law No)
(space Yes)
=>
(result "Capitan Simian and the Space Mokeys" "Jayce and the Wheeled Warriors" "Exosquad" "SilverHawks" "The Adventures of the Galaxy Rangers" "Brave Starr"))

(defrule cowboys
(based-on-game No)
(celebrity No)
(animal-furies No)
(dig-robots No)
(movie-based No)
(post-apocaliptic No)
(sword-sorcery No)
(military-law No)
(space No)
(answers $?ans)
=>
(polar-question "Cowboys?" "cowboys" $?ans))


(defrule cowboys_result
(based-on-game No)
(celebrity No)
(animal-furies No)
(dig-robots No)
(movie-based No)
(post-apocaliptic No)
(sword-sorcery No)
(military-law No)
(space No)
(cowboys Yes)
=>
(result "Wild West Cowboys of Moo Mesa" "The Adventures of the Galaxy Rangers" "Brave Starr"))

(defrule understand_rule
(based-on-game No)
(celebrity No)
(animal-furies No)
(dig-robots No)
(movie-based No)
(post-apocaliptic No)
(sword-sorcery No)
(military-law No)
(space No)
(cowboys No)
(answers $?ans)
=>
(polar-question "Do you want to understand what's going on?" "understand" $?ans))

(defrule understand_rule_no
(based-on-game No)
(celebrity No)
(animal-furies No)
(dig-robots No)
(movie-based No)
(post-apocaliptic No)
(sword-sorcery No)
(military-law No)
(space No)
(cowboys No)
(understand No)
(answers $?ans)
=>
(polar-question "In an awesome way?" "way" $?ans))


(defrule understand_rule_yes
(based-on-game No)
(celebrity No)
(animal-furies No)
(dig-robots No)
(movie-based No)
(post-apocaliptic No)
(sword-sorcery No)
(military-law No)
(space No)
(cowboys No)
(understand Yes)
(answers $?ans)
=>
(polar-question "Kids doing awesome stuff?" "kids-stuff" $?ans))


(defrule way_result_no
(based-on-game No)
(celebrity No)
(animal-furies No)
(dig-robots No)
(movie-based No)
(post-apocaliptic No)
(sword-sorcery No)
(military-law No)
(space No)
(cowboys No)
(way No)
=>
(result "Inhumanoids"))

(defrule way_result_yes
(based-on-game No)
(celebrity No)
(animal-furies No)
(dig-robots No)
(movie-based No)
(post-apocaliptic No)
(sword-sorcery No)
(military-law No)
(space No)
(cowboys No)
(way Yes)
=>
(result "Aeon Flux"))

(defrule kids_stuff_rule_yes
(based-on-game No)
(celebrity No)
(animal-furies No)
(dig-robots No)
(movie-based No)
(post-apocaliptic No)
(sword-sorcery No)
(military-law No)
(space No)
(cowboys No)
(understand Yes)
(kids-stuff Yes)
(answers $?ans)
=>
(polar-question "In an educational manner?" "educational-manner" $?ans))

(defrule kids_stuff_result_yes
(based-on-game No)
(celebrity No)
(animal-furies No)
(dig-robots No)
(movie-based No)
(post-apocaliptic No)
(sword-sorcery No)
(military-law No)
(space No)
(cowboys No)
(understand Yes)
(kids-stuff Yes)
(educational-manner Yes)
=>
(result "The Magic School Bus" "Capitan Planet and the Planeteers"))

(defrule kids_stuff_result_no
(based-on-game No)
(celebrity No)
(animal-furies No)
(dig-robots No)
(movie-based No)
(post-apocaliptic No)
(sword-sorcery No)
(military-law No)
(space No)
(cowboys No)
(understand Yes)
(kids-stuff Yes)
(educational-manner No)
=>
(result "Bionic Six" "Mighty Max" "The Real Adventures of Jonny Quest"))

(defrule computers_rule
(based-on-game No)
(celebrity No)
(animal-furies No)
(dig-robots No)
(movie-based No)
(post-apocaliptic No)
(sword-sorcery No)
(military-law No)
(space No)
(cowboys No)
(understand Yes)
(kids-stuff No)
(answers $?ans)
=>
(polar-question "Do you like computers" "computers" $?ans))


(defrule computers_result
(based-on-game No)
(celebrity No)
(animal-furies No)
(dig-robots No)
(movie-based No)
(post-apocaliptic No)
(sword-sorcery No)
(military-law No)
(space No)
(cowboys No)
(understand Yes)
(kids-stuff No)
(computers Yes)
=>
(result "ReBoot"))

(defrule outrageous_rule
(based-on-game No)
(celebrity No)
(animal-furies No)
(dig-robots No)
(movie-based No)
(post-apocaliptic No)
(sword-sorcery No)
(military-law No)
(space No)
(cowboys No)
(understand Yes)
(kids-stuff No)
(computers No)
(answers $?ans)
=>
(polar-question "Something truly outrageous?" "outrageous" $?ans))


(defrule outrageous_result
(based-on-game No)
(celebrity No)
(animal-furies No)
(dig-robots No)
(movie-based No)
(post-apocaliptic No)
(sword-sorcery No)
(military-law No)
(space No)
(cowboys No)
(understand Yes)
(kids-stuff No)
(computers No)
(outrageous Yes)
=>
(result "Jem"))

(defrule undead_rule
(based-on-game No)
(celebrity No)
(animal-furies No)
(dig-robots No)
(movie-based No)
(post-apocaliptic No)
(sword-sorcery No)
(military-law No)
(space No)
(cowboys No)
(understand Yes)
(kids-stuff No)
(computers No)
(outrageous No)
(answers $?ans)
=>
(polar-question "The undead?" "undead" $?ans))


(defrule undead_result_yes
(based-on-game No)
(celebrity No)
(animal-furies No)
(dig-robots No)
(movie-based No)
(post-apocaliptic No)
(sword-sorcery No)
(military-law No)
(space No)
(cowboys No)
(understand Yes)
(kids-stuff No)
(computers No)
(outrageous No)
(undead No)
=>
(result "The World of David the Gnome"))

(defrule undead_result_yes
(based-on-game No)
(celebrity No)
(animal-furies No)
(dig-robots No)
(movie-based No)
(post-apocaliptic No)
(sword-sorcery No)
(military-law No)
(space No)
(cowboys No)
(understand Yes)
(kids-stuff No)
(computers No)
(outrageous No)
(undead Yes)
=>
(result "Mummies Alive" "Skeleton Warriors"))