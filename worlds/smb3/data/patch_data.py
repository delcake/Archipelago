patches = {
    # Worlds
    "world_1": {  # Move lock and remove item from hammer brother
        0x147CD: [0x2A],
        0x147DE: [0x16],
        0x147EF: [0x0B, 0x02],
        0x14812: [0xFE, 0xE1, 0xE1],
        0x14855: [0x80],
        0x14866: [0xB0],
        0x14877: [0x45],
        0x16192: [0x00],
        0x185EE: [0x46],
        0x18625: [0x56],
    },
    "world_2": {  # Move lock and remove items from hammer brothers
        0x147CE: [0x29],
        0x147DF: [0xC4],
        0x147F1: [0x12, 0x04],
        0x14856: [0x70],
        0x14867: [0x21],
        0x1619B: [0x00, 0x00, 0x00],
        0x186C3: [0x46],
        0x1872D: [0x54],
    },
    "world_3": {  # Move locks and remove items from hammer brothers
        0x147D0: [0x2A],
        0x147E0: [0x18, 0x14],
        0x147F3: [0x2C],
        0x147F5: [0x2A, 0x02],
        0x14819: [0x9B, 0x11, 0x84, 0xC2],
        0x1481E: [0xFE, 0xE1, 0xE1],
        0x14858: [0x80],
        0x14868: [0xC2, 0xA2],
        0x14879: [0xB7, 0x45],
        0x161A4: [0x00, 0x00],
        0x187D5: [0x45],
        0x18832: [0x46],
        0x188F6: [0x56],
        0x188F8: [0x56],
    },
    "world_4": {  # Move lock, switch which boom boom reveals the bridge and remove items from hammer brothers
        0x147E2: [0x96, 0x92],
        0x147F7: [0x0B, 0x08, 0x09],
        0x14821: [0xD4, 0xD6, 0xD5, 0xD7, 0xFE, 0xFE, 0xE1, 0xE1],
        0x14859: [0x60],
        0x1486A: [0xB0, 0x90],
        0x1487B: [0xB3, 0x45],
        0x161AD: [0x00, 0x00, 0x00],
        0x18966: [0x56],
        0x189D0: [0x45],
    },
    "world_5": {  # Remove locks, add bridge and remove items from hammer brothers
        0x147D3: [0x28, 0x2A],
        0x147E4: [0x82, 0x42],
        0x147FB: [0x01, 0x80, 0x11, 0x01],
        0x14829: [0xFE, 0xFE, 0xFE, 0xFE],
        0x1482F: [0xFE, 0xFE],
        0x1485B: [0x20, 0x90],
        0x1486C: [0x10, 0x11],
        0x1487D: [0x42, 0xD7],
        0x161B6: [0x00, 0x00, 0x00],
        0x18A81: [0xB3],
        0x18B15: [0xDA],
    },
    "world_9": {  # Make the warp zone a hub where each world is accessible at all times
        0x19085: [0x87, 0x95, 0x95, 0x95, 0x95, 0x95, 0x95, 0x95, 0x88],
        0x19095: [0x8E, 0xB4, 0xD7, 0xBB, 0xA1, 0x83, 0xA3, 0xBD, 0x94],
        0x190A6: [0xBC],
        0x190B6: [0xDB],
        0x190BA: [0xEA],
        0x190BC: [0xBE],
        0x190C6: [0xDD],
        0x190DA: [0xDB],
        0x190DC: [0xD1],
        0x190EA: [0xDD],
        0x190ED: [0xE2],
    },
    # Levels
    "world_1_level_1": {  # Remove powerups and change white platform to blue
        0x1FBB6: [0x20],
        0x1FBC2: [0x43],
        0x1FBE4: [0x20],
        0x1FC2A: [0x20],
    },
    "world_1_level_2": {  # Remove powerups
        0x20FAA: [0x20],
        0x21043: [0x31],
        0x21045: [0x60],
    },
    "world_1_level_3": {  # Remove powerups and change white platform to green
        0x1EE76: [0x10],
        0x1EE95: [0x37],
        0x1EE97: [0x40],
        0x1EEDB: [0x74],
    },
    "world_1_level_4": {  # Remove powerup
        0x23591: [0x10],
    },
    "world_1_level_4_no_autoscroll": {
        0xCC44: [0xD4, 0x01, 0x2C, 0x36, 0x17, 0x14],
        0xCC4B: [0x23, 0x16],
        0xCC4E: [0x25, 0x13],
        0xCC51: [0x27, 0x19],
        0xCC54: [0x2F, 0x15, 0x6D, 0x43],
        0xCC59: [0x36, 0x44, 0x18],
        0xCC5D: [0x4B, 0x14],
        0xCC60: [0x56, 0x16],
        0xCC63: [0x58, 0x15],
        0xCC66: [0x61, 0x13],
        0xCC69: [0x6D, 0x18],
        0xCC6C: [0x6F, 0x15],
        0xCC6F: [0x70, 0x1A, 0x6F, 0x75, 0x13, 0x6D, 0x7C, 0x16, 0xFF],
    },
    "world_1_level_5": {  # Remove powerup
        0x1ABB7: [0x20],
    },
    "world_1_level_6": {  # Remove powerup
        0x233F6: [0x20],
    },
    "world_1_fortress": {  # Remove powerups
        0x2A9CC: [0x20],
        0x2AA07: [0x20],
    },
    "world_1_fortress_alt": {  # Change chest content from warp whistle to nothing
        0xD36A: [0x00],
    },
    "world_1_ship": {  # Remove powerup
        0x2EE46: [0x20],
    },
    "world_1_hammer_bros_2": {  # Remove powerup
        0x2142C: [0x10],
    },
    "world_2_level_1": {  # Remove powerups
        0x294BF: [0x20],
        0x29504: [0x10],
        0x2957A: [0x34],
        0x2957C: [0x40],
    },
    "world_2_level_2": {  # Remove powerup
        0x21901: [0x33],
        0x21903: [0x40],
    },
    "world_2_level_3": {  # Remove powerups
        0x2994E: [0x20],
        0x2998D: [0x20],
    },
    "world_2_level_4": {  # Remove powerups
        0x29D54: [0x20],
        0x29D9F: [0x20],
        0x29E6E: [0x20],
        0x29F0B: [0x2E],
        0x29F0D: [0x60],
    },
    "world_2_level_5": {  # Remove powerups
        0x29770: [0x20],
        0x29795: [0x39],
        0x29797: [0x40],
        0x298AF: [0x20],
    },
    "world_2_level_5_alt": {  # Remove powerup
        0x29911: [0x10],
    },
    "world_2_pyramid": {  # Remove powerup
        0x205F0: [0x20],
    },
    "world_2_fortress": {  # Remove powerup
        0x29B89: [0x10],
    },
    "world_2_ship": {  # Remove powerup
        0x2EF6D: [0x20],
    },
    # Gameplay
    "gameplay_disable_bonuses": {
        0x16C63: [0xEE, 0x29, 0x07, 0x4C, 0x29, 0xCF],
        0x16C7C: [0xEC],
    },
    "gameplay_infinite_inventory_items": {
        0x3462B: [0x60, 0xEA],
    },
    "gameplay_reenter_levels": {  # Experimental. Only allow rentry to levels with the M tile and fortress rubble. We might need more entries if that messes something up. Alternative would be for people to use the warp whistle and come back
        0x14ED8: [0x04],
        0x14EDA: [0xC0, 0xDD],
        0x15DD0: [0x80, 0x00, 0xC0, 0x40, 0x60],
    },
    "gameplay_infinite_lives": {
        0x5D99: [0xEA, 0xEA, 0xEA],
        0xEB0F: [0xEA, 0xEA, 0xEA],
        0x12085: [0xEA, 0xEA, 0xEA, 0xEA, 0xEA, 0xEA, 0xEA, 0xEA, 0xEA, 0xEA],
        0x2CD78: [0xEA, 0xEA, 0xEA],
        0x2D2BE: [0xEA, 0xEA, 0xEA],
        0x2DD50: [0xEA, 0xEA, 0xEA],
        0x308E1: [0xFB],
        0x30D47: [0xEA, 0xEA, 0xEA],
        0x30D7A: [0xEA, 0xEA, 0xEA],
        0x350A7: [0xEA, 0xEA, 0xEA],
        0x3D133: [0xEA, 0xEA, 0xEA, 0xEA, 0xEA],
        0x3D2D6: [0xFB],
    },
    "gameplay_infinite_lives_death_counter": {
        0x5D99: [0xEA, 0xEA, 0xEA],
        0xEB0F: [0xEA, 0xEA, 0xEA],
        0x12085: [0xEA, 0xEA, 0xEA, 0xEA, 0xEA, 0xEA, 0xEA, 0xEA, 0xEA, 0xEA],
        0x2CD78: [0xEA, 0xEA, 0xEA],
        0x2D2BE: [0xEA, 0xEA, 0xEA],
        0x2DD50: [0xEA, 0xEA, 0xEA],
        0x308E1: [0x00],
        0x30D47: [0xEA, 0xEA, 0xEA],
        0x30D7A: [0xEA, 0xEA, 0xEA],
        0x350A7: [0xEA, 0xEA, 0xEA],
        0x3D133: [0xFE],
        0x3D2D6: [0x00],
    },
    # Game Difficulty
    "game_donut_blocks_fall_faster": {
        0xE0CC: [0x08],
    },
    "game_poison_1up_mushrooms": {
        0x20F3: [0x10],
        0x27AA: [0x20, 0xD3, 0xD9, 0xEA, 0xEA],
    },
    "game_faster_tighter_timers": {
        0x2B2A6: [0x03],
        0x34FC6: [0x14],
        0x3C517: [0x14],
        0x3D7B8: [0x02, 0x03, 0x01],
    },
    "game_one_hit_small_mario": {
        0x19F9: [0xEA, 0xEA, 0xEA],
    },
    "game_one_hit_ko": {
        0x19FA: [0x7A],
    },
    "game_end_cards_cycle_faster": {
        0x5B63: [0x01],
    },
    "game_half_duration_p_switch": {
        0x11653: [0x40],
    },
    "game_random_powerup_direction": {
        0x295C: [0xBD, 0x82, 0x07, 0x29, 0x01, 0xD0, 0x03, 0xC8, 0xEA, 0xEA],
    },
    "game_matching_end_cards_cap": {
        0x5CB8: [0x01, 0x01, 0x01],
        0x5D55: [0xB1, 0xB1, 0xB1],
    },
    "game_no_consecutive_stomps": {
        0xEA95: [0x01],
        0xEA99: [0x00],
    },
    "game_always_somersault": {
        0x10C5C: [0xEA, 0xEA],
        0x10C63: [0xEA, 0xEA],
        0x10C68: [0xEA, 0xEA],
        0x11C68: [0xEA, 0xEA, 0xEA],
    },
    # Enemy Difficulty
    "enemies_faster_boss_bass": {
        0x585E: [0x3E, 0x42],
    },
    "enemies_faster_boss_bass_respawn": {
        0x58A2: [0x80],
    },
    "enemies_faster_cheep_cheep": {
        0x5A1A: [0x30, 0x50],
    },
    "enemies_early_angry_sun": {
        0xAD81: [0x00],
    },
    "enemies_faster_boom_boom": {
        0x6A10: [0x2C, 0xD4, 0x3C, 0xC4, 0x3C, 0xC4],
        0x6C7A: [0x2C, 0xD4],
        0x6E8D: [0x10],
    },
    "enemies_faster_koopalings": {
        0x2FCD: [0x20],
        0x2FD2: [0xE0],
        0x319E: [0x50],
        0x37AA: [0xD8, 0x28],
    },
    "enemies_faster_more_random_hammer_bros": {
        0x84E8: [0x20],
        0x84F2: [0xF4],
        0x84F6: [0x0C],
        0x851D: [0x3F],
        0x854C: [0x08],
        0x8550: [0x20],
        0x8554: [0xF8],
        0x8576: [0x4B],
        0x85F4: [0x18, 0xE8],
        0x862C: [0x30, 0xD0],
        0x8662: [0x2C],
        0x8983: [0xF4],
        0x89A5: [0x0C],
        0x8A53: [0x2F],
        0x8B11: [0xFA],
        0x8B36: [0x06],
    },
    "enemies_smarter_lakitu": {
         0x8E9B: [0xBD],
    },
    "enemies_chain_chomps_break_free": {
        0x9AD2: [0x02],
        0x9CB6: [0x01],
    },
    "enemies_faster_bob_omb_explosions": {
        0x675E: [0x80],
    },
    "enemies_faster_boo": {
        0x48DF: [0x18, 0xE8],
    },
    "enemies_boo_always_chases": {
        0x48E6: [0xEA, 0xEA, 0xEA, 0xEA, 0xEA, 0xEA, 0xEA, 0xEA],
    },
    "enemies_faster_dry_bones_respawn": {
        0x567F: [0x55],
    },
    "enemies_faster_fire_jets": {
        0xA453: [0x3C],
    },
    "enemies_faster_thwomp": {
        0x86DE: [0x20],
        0x87AA: [0x20],
    },
    "enemies_faster_bullet_bill": {
        0x9165: [0x24, 0xDC],
        0xFF39: [0x24, 0xDC],
    },
    "enemies_more_random_podoboos": {
        0xA2D2: [0x5F],
        0xA2D4: [0x20],
    },
    "enemies_piranha_plants_always_emerge": {
        0x981A: [0x01],
        0x981C: [0x00],
        0xA882: [0x01],
        0xA884: [0x02],
    },
    # Tweaks & Fixes
    "tweak_kuribo_shoe_on_stomp": {
        0x50F4: [0x00],
        0x5137: [0x9C, 0xB0],
    },
    "tweak_faster_mushroom_houses": {
        0x1E3F: [0x5F],
        0x5234: [0x7F],
    },
    "tweak_unlimited_statue_time": {
        0x11005: [0xEA, 0xEA, 0xEA],
    },
    "tweak_easier_spade_game": {
        0x2D0A9: [0x00],
        0x2D0AB: [0x00],
        0x2D0C5: [0x00],
        0x2D0C7: [0x00],
        0x2D0E1: [0x00],
        0x2D0E3: [0x00],
    },
    "tweak_instant_title_screen": {
        0x30953: [0x00],
        0x309A0: [0xA9, 0x06, 0x85, 0xDE, 0x60],
        0x309AD: [0xA9, 0x06, 0x85, 0xDE, 0x60, 0xEA],
        0x30C35: [0x00],
        0x30C39: [0xFF],
    },
    "tweak_reduce_flashing": {
        0xE19C: [0x26, 0x26, 0x26],
        0x16348: [0x10],
        0x361B9: [0x0F],
    },
    "tweak_no_letter_rewards_on_world_end": {
        0x360DE: [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    },
    "fix_koopaling_softlock": {
        0x2816: [0x09],
    },
    "fix_bowser_hitbox": {
        0x2D4: [0x04, 0x11, 0x12, 0x13],
        0x31C: [0x04],
        0xE681: [0x32],
        0xE691: [0x18],
    },
    "fix_bowser_star_softlock": {
        0x3EB4: [0xA9, 0x02, 0x9D, 0x61, 0x06, 0xEA, 0xEA],
    },
    # Graphics
    "gfx_title_screen": {
        0x32B12: [0x0A, 0x0B, 0x0C, 0x0D, 0x0B, 0x5C, 0x0C, 0x1A],
        0x32B1B: [0x0A, 0x1B, 0x1B, 0x1E],
        0x32B22: [0x5C],
        0x32B24: [0x5C, 0x5C, 0x5C, 0x5C, 0x5C, 0x5C],
        0x32B2B: [0x5C, 0x5C, 0x5C, 0x5C],
        0x45EB3: [0x24, 0x24, 0x24, 0x24, 0x3C],
        0x45EBB: [0x18, 0x18, 0x18, 0x18, 0x00],
        0x45F60: [0xFE, 0x82, 0x9E],
        0x45F64: [0x71, 0x71],
        0x45F67: [0xFE, 0x00, 0x7C, 0x60],
        0x45F6C: [0x0E, 0x0E],
        0x45F6F: [0x00],
        0x5E0B1: [0x82, 0x9E, 0x83, 0x71, 0x71, 0x83, 0xFE],
        0x5E0BA: [0x60, 0x7C, 0x0E, 0x0E, 0x7C],
        0x5E0C0: [0xFF, 0x81, 0xE7, 0x24, 0x24, 0x24, 0x24, 0x3C],
        0x5E0C9: [0x7E, 0x18, 0x18, 0x18, 0x18, 0x18],
        0x5E1B0: [0xFE, 0x83],
        0x5E1B3: [0x99, 0x83, 0x9E, 0x90, 0xF0],
        0x5E1B9: [0x7C],
        0x5E1BB: [0x66, 0x7C, 0x60, 0x60],
        0x5E1D0: [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
        0x5E1D9: [0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
        0x5E1F0: [0xFC, 0x86, 0x93, 0x99, 0x99, 0x99, 0x83, 0xFE],
        0x5E1F9: [0x78, 0x6C, 0x66, 0x66, 0x66, 0x7C],
        0x5ECF1: [0xE0, 0xA0, 0xEE, 0xAA, 0xAE],
        0x5ED03: [0x00, 0x00, 0x00, 0x00, 0x00],
        0x5EE00: [0x00, 0x00, 0x00]
    }
    # ... Maybe replace warp zone banner text?
}
