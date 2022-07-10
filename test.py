class unit :
  def __init__(self, name, hp) :
    self.name = name
    self.hp = hp
    print(self.name, "유닛이 생성되었습니다.")
    print("체력", self.hp)

class attackunit(unit) :
  def __init__(self, name, hp, damage) :
    unit.__init__(self, name, hp)
    self.damagfe = damage
    print("데미지는 : ", self.damage)
    print("살려줘 씹")
    print("second_commit")
wr1 = attackunit("레이스", 50, 40)
