from src.constants import *
from colorama import init, Fore, Back, Style

init()

# Spells class
class Spells:
    def __init__(this):
        this.__damage = 2
        this.__speed = 2
        this.__health = 1.5
        this.__ragerem = 1
        this.__healrem = 1

    # encapsulation
    def ret_damage(this):
        return this.__damage

    def ret_speed(this):
        return this.__speed

    def ret_health(this):
        return this.__health

    def ret_ragerem(this):
        return this.__ragerem

    def upd_ragerem(this, x):
        this.__ragerem = x

    def ret_healrem(this):
        return this.__healrem

    def upd_healrem(this, x):
        this.__healrem = x

    """
    Polymorphism implemented (same function name, different number of arguments)
    """
    # Rage/Heal Spell
    def spell(this, barbarian1, barbarian2, barbarian3, king, archer1, archer2, archer3, balloon1, balloon2, balloon3, heal=0):
        x = this.ret_healrem()
        if heal == 1:
            if x > 0:
                this.upd_healrem(x - 1)
                h_king = king.ret_health()
                h_king = h_king * this.ret_health()
                if h_king > king.ret_total_health():
                    h_king = king.ret_total_health()
                king.upd_health(h_king)

                if barbarian1.ret_active():
                    health = barbarian1.ret_health()
                    health = health * this.ret_health()
                    if health > barbarian1.ret_total_health():
                        health = barbarian1.ret_total_health()
                    barbarian1.upd_health(health)
                if barbarian2.ret_active():
                    health = barbarian2.ret_health()
                    health = health * this.ret_health()
                    if health > barbarian2.ret_total_health():
                        health = barbarian2.ret_total_health()
                    barbarian2.upd_health(health)
                if barbarian3.ret_active():
                    health = barbarian3.ret_health()
                    health = health * this.ret_health()
                    if health > barbarian3.ret_total_health():
                        health = barbarian3.ret_total_health()
                    barbarian3.upd_health(health)
                if archer1.ret_active():
                    health = archer1.ret_health()
                    health = health * this.ret_health()
                    if health > archer1.ret_total_health():
                        health = archer1.ret_total_health()
                    archer1.upd_health(health)
                if archer2.ret_active():
                    health = archer2.ret_health()
                    health = health * this.ret_health()
                    if health > archer2.ret_total_health():
                        health = archer2.ret_total_health()
                    archer2.upd_health(health)
                if archer3.ret_active():
                    health = archer3.ret_health()
                    health = health * this.ret_health()
                    if health > archer3.ret_total_health():
                        health = archer3.ret_total_health()
                    archer3.upd_health(health)
                if balloon1.ret_active():
                    health = balloon1.ret_health()
                    health = health * this.ret_health()
                    if health > balloon1.ret_total_health():
                        health = balloon1.ret_total_health()
                    balloon1.upd_health(health)
                if balloon2.ret_active():
                    health = balloon2.ret_health()
                    health = health * this.ret_health()
                    if health > balloon2.ret_total_health():
                        health = balloon2.ret_total_health()
                    balloon2.upd_health(health)
                if balloon3.ret_active():
                    health = balloon3.ret_health()
                    health = health * this.ret_health()
                    if health > balloon3.ret_total_health():
                        health = balloon3.ret_total_health()
                    balloon3.upd_health(health)
                    
        else:
            x = this.ret_ragerem()
            if x > 0:
                this.upd_ragerem(x - 1)
                damage = king.ret_damage()
                damage = damage * this.ret_damage()
                king.upd_damage(damage)
                speed = king.ret_speed()
                speed = speed * this.ret_speed()
                king.upd_speed(speed)

                if barbarian1.ret_active() == 1:
                    damage = barbarian1.ret_damage()
                    damage = damage * this.ret_damage()
                    speed = barbarian1.ret_speed()
                    speed = speed * this.ret_speed()
                    barbarian1.upd_damage(damage)
                    barbarian1.upd_speed(speed)
                if barbarian2.ret_active() == 1:
                    damage = barbarian2.ret_damage()
                    damage = damage * this.ret_damage()
                    speed = barbarian2.ret_speed()
                    speed = speed * this.ret_speed()
                    barbarian2.upd_damage(damage)
                    barbarian2.upd_speed(speed)
                if barbarian3.ret_active() == 1:
                    damage = barbarian3.ret_damage()
                    damage = damage * this.ret_damage()
                    speed = barbarian3.ret_speed()
                    speed = speed * this.ret_speed()
                    barbarian3.upd_damage(damage)
                    barbarian3.upd_speed(speed)
                if archer1.ret_active() == 1:
                    damage = archer1.ret_damage()
                    damage = damage * this.ret_damage()
                    speed = archer1.ret_speed()
                    speed = speed * this.ret_speed()
                    archer1.upd_damage(damage)
                    archer1.upd_speed(speed)
                if archer2.ret_active() == 1:
                    damage = archer2.ret_damage()
                    damage = damage * this.ret_damage()
                    speed = archer2.ret_speed()
                    speed = speed * this.ret_speed()
                    archer2.upd_damage(damage)
                    archer2.upd_speed(speed)
                if archer3.ret_active() == 1:
                    damage = archer3.ret_damage()
                    damage = damage * this.ret_damage()
                    speed = archer3.ret_speed()
                    speed = speed * this.ret_speed()
                    archer3.upd_damage(damage)
                    archer3.upd_speed(speed)
                if balloon1.ret_active() == 1:
                    damage = balloon1.ret_damage()
                    damage = damage * this.ret_damage()
                    speed = balloon1.ret_speed()
                    speed = speed * this.ret_speed()
                    balloon1.upd_damage(damage)
                    balloon1.upd_speed(speed)
                if balloon2.ret_active() == 1:
                    damage = balloon2.ret_damage()
                    damage = damage * this.ret_damage()
                    speed = balloon2.ret_speed()
                    speed = speed * this.ret_speed()
                    balloon2.upd_damage(damage)
                    balloon2.upd_speed(speed)
                if balloon3.ret_active() == 1:
                    damage = balloon3.ret_damage()
                    damage = damage * this.ret_damage()
                    speed = balloon3.ret_speed()
                    speed = speed * this.ret_speed()
                    balloon3.upd_damage(damage)
                    balloon3.upd_speed(speed)