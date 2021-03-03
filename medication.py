def asberin_p(BW):
    dose = str(round(0.05 * BW, 1))
    return "アスベリンDS2%(20mg/g)" + "  " + dose + "g\n" + "用量: " + "1-2mg/kg/日分3　極量：3g/日\nコメント：シロップもある、錠剤もある"

def asberin_s(BW):
    dose = str(round(0.2 * BW, 1))
    return "アスベリンシロップ0.5%(5mg/mL)" + "  " + dose + "mL\n" + "用量: " + "1-2mg/kg/日分3　極量：3g/日\nコメント：シロップもある、錠剤もある"

def mukodain_p(BW):
    dose = str(round(0.06 * BW, 1))
    return "ムコダインDS50%(500mg/g)" + "  " + dose + "g\n" + "用量: " + "30mg/kg/日分3　極量：3g/日\nコメント：シロップもある、錠剤もある"

def mukodain_s(BW):
    dose = str(round(0.6 * BW, 1))
    return "ムコダインシロップ5%(50mg/mL)" + "  " + dose + "mL\n" + "用量: " + "30mg/kg/日分3　極量：3g/日\nコメント：シロップもある、錠剤もある"

def hokunarin(age):
    if age < 3:
        return "ホクナリンテープ0.5mg\n" + "用量: " + "3才未満は0.5mg、3-9才は1mg、9才以上は2mgを使用\nコメント：貼付剤"
    elif age >= 3 and age < 9:
        return "ホクナリンテープ1mg\n" + "用量: " + "3才未満は0.5mg、3-9才は1mg、9才以上は2mgを使用\nコメント：貼付剤"
    else:
        return "ホクナリンテープ2mg\n" + "用量: " + "3才未満は0.5mg、3-9才は1mg、9才以上は2mgを使用\nコメント：貼付剤"
