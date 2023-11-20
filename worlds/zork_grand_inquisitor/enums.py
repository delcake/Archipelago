import enum


class ZorkGrandInquisitorEvents(enum.Enum):
    CIGAR_ACCESSIBLE = "Event: Cigar Accessible"
    DAM_DESTROYED = "Event: Dam Destroyed"
    DOOR_DRANK_MEAD = "Event: Door Drank Mead"
    DOOR_SMOKED_CIGAR = "Event: Door Smoked Cigar"
    DUNCE_LOCKER_OPENABLE = "Event: Dunce Locker Openable"
    HAS_HALF_OF_SNAVIG = "Event: Has Half of SNAVIG"
    HAS_REPAIRABLE_SNAVIG = "Event: Has Repairable SNAVIG"
    KNOWS_BEBURTT = "Event: Knows BEBURTT"
    KNOWS_SNAVIG = "Event: Knows SNAVIG"
    LANTERN_DALBOZ_ACCESSIBLE = "Event: Lantern (Dalboz) Accessible"
    ROPE_GLORFABLE = "Event: Rope GLORFable"
    SPELL_LAB_ACCESSIBLE = "Event: Spell Lab Accessible"
    VICTORY = "Victory"
    ZORKMID_BILL_ACCESSIBLE = "Event: 500 Zorkmid Bill Accessible"
    ZORK_ROCKS_ACTIVATED = "Event: Zork Rocks Activated"
    ZORK_ROCKS_SUCKABLE = "Event: Zork Rocks Suckable"


class ZorkGrandInquisitorGoals(enum.Enum):
    THREE_ARTIFACTS = 0


class ZorkGrandInquisitorItems(enum.Enum):
    FILLER_FROBOZZ_ELECTRIC_GADGET = "Frobozz Electric Gadget"
    FILLER_INQUISITION_PROPAGANDA_FLYER = "Inquisition Propaganda Flyer"
    FILLER_MAGIC_CONTRABAND = "Magic Contraband"
    FILLER_NONSENSICAL_INQUISITION_PAPERWORK = "Nonsensical Inquisition Paperwork"
    FILLER_UNREADABLE_SPELL_SCROLL = "Unreadable Spell Scroll"
    FLATHEADIA_FUDGE = "Flatheadia Fudge"
    HAMMER = "Hammer"
    HUNGUS_LARD = "Hungus Lard"
    JAR_OF_HOTBUGS = "Jar of Hotbugs"
    LANTERN = "Lantern"
    LARGE_TELEGRAPH_HAMMER = "Large Telegraph Hammer"
    LETTER_OPENER = "Letter Opener"
    MAP = "Map"
    MEAD_LIGHT = "Mead Light"
    MOSS_OF_MAREILON = "Moss of Mareilon"
    MUG = "Mug"
    OLD_SCRATCH_CARD = "Old Scratch Card"
    PERMA_SUCK_MACHINE = "Perma-Suck Machine"
    PLASTIC_SIX_PACK_HOLDER = "Plastic Six-Pack Holder"
    POUCH_OF_ZORKMIDS = "Pouch of Zorkmids"
    PROZORK_TABLET = "Prozork Tablet"
    QUELBEE_HONEYCOMB = "Quelbee Honeycomb"
    REVEALED_BROGS_TIME_TUNNEL_ITEMS = "Revealed: Brog's Time Tunnel Items"
    REVEALED_GRIFFS_TIME_TUNNEL_ITEMS = "Revealed: Griff's Time Tunnel Items"
    REVEALED_LUCYS_TIME_TUNNEL_ITEMS = "Revealed: Lucy's Time Tunnel Items"
    ROPE = "Rope"
    SHOVEL = "Shovel"
    SNAPDRAGON = "Snapdragon"
    SPELL_GLORF = "Spell: GLORF"
    SPELL_GOLGATEM = "Spell: GOLGATEM"
    SPELL_IGRAM = "Spell: IGRAM"
    SPELL_KENDALL = "Spell: KENDALL"
    SPELL_NARWILE = "Spell: NARWILE"
    SPELL_OBIDIL = "Spell: OBIDIL"
    SPELL_REZROV = "Spell: REZROV"
    SPELL_THROCK = "Spell: THROCK"
    SPELL_VOXAM = "Spell: VOXAM"
    SPELL_YASTARD = "Spell: YASTARD"
    STUDENT_ID = "Student ID"
    SUBWAY_DESTINATION_FLOOD_CONTROL_DAM = "Subway Destination: Flood Control Dam #3"
    SUBWAY_DESTINATION_HADES = "Subway Destination: Hades"
    SUBWAY_DESTINATION_MONASTERY = "Subway Destination: Monastery"
    SUBWAY_TOKEN = "Subway Token"
    SWORD = "Sword"
    TELEPORTER_DESTINATION_DM_LAIR = "Teleporter Destination: Dungeon Master's Lair"
    TELEPORTER_DESTINATION_GUE_TECH = "Teleporter Destination: GUE Tech"
    TELEPORTER_DESTINATION_HADES = "Teleporter Destination: Hades"
    TELEPORTER_DESTINATION_MONASTERY = "Teleporter Destination: Monastery Station"
    TELEPORTER_DESTINATION_SPELL_LAB = "Teleporter Destination: Spell Lab"
    TOTEM_BROG = "Totem: Brog"
    TOTEM_GRIFF = "Totem: Griff"
    TOTEM_LUCY = "Totem: Lucy"
    UNLOCKED_BLANK_SCROLL_BOX_ACCESS = "Unlocked: Blank Scroll Box Access"
    ZIMDOR_SCROLL = "ZIMDOR Scroll"
    ZORK_ROCKS = "Zork Rocks"


class ZorkGrandInquisitorLocations(enum.Enum):
    ARREST_THE_VANDAL = "Arrest the Vandal!"
    ARTIFACTS_EXPLAINED = "Artifacts, Explained"
    A_SMALLWAY = "A Smallway"
    BEAUTIFUL_THATS_PLENTY = "Beautiful, That's Plenty!"
    BEBURTT_DEMYSTIFIED = "BEBURTT, Demystified"
    BROG_DO_GOOD = "Brog Do Good!"
    BROG_MUCH_BETTER_AT_THIS_GAME = "Brog Much Better at This Game"
    CRISIS_AVERTED = "Crisis Averted"
    DEATH_ARRESTED_WITH_JACK = "Death: Arrested With Jack"
    DEATH_ATTACKED_THE_QUELBEES = "Death: Attacked the Quelbees"
    DEATH_CLIMBED_OUT_OF_THE_WELL = "Death: Climbed Out of the Well"
    DEATH_EATEN_BY_A_GRUE = "Death: Eaten by a Grue"
    DEATH_JUMPED_IN_BOTTOMLESS_PIT = "Death: Jumped in Bottomless Pit"
    DEATH_LOST_GAME_OF_STRIP_GRUE_FIRE_WATER = "Death: Lost Game of Strip Grue, Fire, Water"
    DEATH_LOST_SOUL_TO_OLD_SCRATCH = "Death: Lost Soul to Old Scratch"
    DEATH_OUTSMARTED_BY_THE_QUELBEES = "Death: Outsmarted by the Quelbees"
    DEATH_SLICED_UP_BY_THE_INVISIBLE_GUARD = "Death: Sliced up by the Invisible Guard"
    DEATH_STEPPED_INTO_THE_INFINITE = "Death: Step Into the Infinite"
    DEATH_SWALLOWED_BY_A_DRAGON = "Death: Swallowed by a Dragon"
    DEATH_THROCKED_THE_GRASS = "Death: THROCKed the Grass"
    DEATH_TOTEMIZED = "Death: Totemized?"
    DEATH_TOTEMIZED_PERMANENTLY = "Death: Totemized... Permanently"
    DEATH_YOURE_NOT_CHARON = "Death: You're Not Charon!?"
    DEATH_ZORK_ROCKS_EXPLODED = "Death: Zork Rocks Exploded"
    DRAGON_ARCHIPELAGO_TIME_TUNNEL = "Dragon Archipelago Time Tunnel"
    DUNCE_LOCKER = "Dunce Locker"
    ELSEWHERE = "Elsewhere"
    ENJOY_YOUR_TRIP = "Enjoy Your Trip!"
    GETTING_SOME_CHANGE = "Getting Some Change"
    GUE_TECH_ENTRANCE_EXAM = "GUE Tech Entrance Exam"
    HAVE_A_HELL_OF_A_DAY = "Have a Hell of a Day!"
    HELP_ME_CANT_BREATHE = "Help... Me. Can't... Breathe"
    HEY_FREE_DIRT = "Hey, Free Dirt!"
    IMBUE_BEBURTT = "Imbue BEBURTT"
    INTO_THE_FOLIAGE = "Into the Foliage"
    IN_CASE_OF_ADVENTURE = "In Case of Adventure, Break Glass!"
    IN_MAGIC_WE_TRUST = "In Magic We Trust"
    I_HOPE_YOU_CAN_CLIMB_UP_THERE = "I Hope You Can Climb Up There With All This Junk"
    I_LIKE_YOUR_STYLE = "I Like Your Style!"
    MAGIC_FOREVER = "Magic Forever!"
    NATIONAL_TREASURE = "300 Year Old National Treasure"
    NOOOOOOOOOOOOO = "NOOOOOOOOOOOOO!"
    NOTHIN_LIKE_A_GOOD_STOGIE = "Nothin' Like a Good Stogie"
    OH_DEAR_GOD_ITS_A_DRAGON = "Oh Dear God, It's a Dragon!"
    OLD_SCRATCH_WINNER = "Old Scratch Winner!"
    OPEN_THE_GATES_OF_HELL = "Open the Gates of Hell"
    OUTSMART_THE_QUELBEES = "Outsmart the Quelbees"
    PLANETFALL = "Planetfall"
    PLANTS_ARE_MANS_BEST_FRIEND = "Plants Are Man's Best Friend"
    PORT_FOOZLE_TIME_TUNNEL = "Port Foozle Time Tunnel"
    PROZORKED = "Prozorked"
    REASSEMBLE_SNAVIG = "Reassemble SNAVIG"
    SNAVIG_REPAIRED = "SNAVIG, Repaired"
    SOUVENIR = "Souvenir"
    STRIP_GRUE_FIRE_WATER = "Strip Grue, Fire, Water"
    SUCKING_ROCKS = "Sucking Rocks"
    THAR_SHE_BLOWS = "Thar She Blows!"
    THATS_THE_SPIRIT = "That's the Spirit!"
    THE_UNDERGROUND_UNDERGROUND = "The Underground Underground"
    TOTEMIZED_DAILY_BILLBOARD = "Totemized Daily Billboard Functioning Correctly"
    UMBRELLA_FLOWERS = "Umbrella Flowers"
    USELESS_BUT_FUN = "Useless, But Fun"
    WANT_SOME_RYE_COURSE_YA_DO = "Want Some Rye? Course Ya Do!"
    WE_GOT_A_HIGH_ROLLER = "We Got a High Roller!"
    WHITE_HOUSE_TIME_TUNNEL = "White House Time Tunnel"
    WOW_IVE_NEVER_GONE_INSIDE_HIM_BEFORE = "Wow! I've Never Gone Inside Him Before!"
    YOU_GAINED_86_EXPERIENCE_POINTS = "You Gained 86 Experience Points"


class ZorkGrandInquisitorRegions(enum.Enum):
    CROSSROADS = "Crossroads"
    DM_LAIR = "Dungeon Master's Lair"
    DM_LAIR_INTERIOR = "Dungeon Master's Lair - Interior"
    DRAGON_ARCHIPELAGO = "Dragon Archipelago"
    ENDGAME = "Endgame"
    GUE_TECH = "GUE Tech"
    GUE_TECH_HALLWAY = "GUE Tech - Hallway"
    HADES = "Hades"
    HADES_BEYOND_GATES = "Hades - Beyond Gates"
    HADES_SHORE = "Hades - Shore"
    MENU = "Menu"
    MONASTERY = "Monastery"
    PORT_FOOZLE = "Port Foozle"
    PORT_FOOZLE_JACKS_SHOP = "Port Foozle - Jack's Shop"
    PORT_FOOZLE_PAST = "Port Foozle - Past"
    SPELL_LAB = "Spell Lab"
    SPELL_LAB_BRIDGE = "Spell Lab - Bridge"
    SUBWAY_CROSSROADS = "Subway Platform - Crossroads"
    SUBWAY_FLOOD_CONTROL_DAM = "Subway Platform - Flood Control Dam #3"
    SUBWAY_MONASTERY = "Subway Platform - Monastery"
    WALKING_CASTLE = "Walking Castle"
    WHITE_HOUSE = "White House"


class ZorkGrandInquisitorTags(enum.Enum):
    CORE = "Core"
    DEATHSANITY = "Deathsanity"
    FILLER = "Filler"
    INVENTORY_ITEM = "Inventory Item"
    REVEALED = "Revealed"
    SPELL = "Spell"
    SUBWAY_DESTINATION = "Subway Destination"
    TELEPORTER_DESTINATION = "Teleporter Destination"
    TOTEM = "Totem"
    UNLOCKED = "Unlocked"
